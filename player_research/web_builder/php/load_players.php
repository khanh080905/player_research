<?php
declare(strict_types=1);

require_once __DIR__ . '/config.php';

function players_normalize(string $value): string
{
    $value = trim(mb_strtolower($value, 'UTF-8'));
    $transliterated = @iconv('UTF-8', 'ASCII//TRANSLIT//IGNORE', $value);
    if ($transliterated !== false && $transliterated !== '') {
        $value = $transliterated;
    }
    $value = preg_replace('/[^a-z0-9]+/i', ' ', $value) ?? $value;
    return trim($value);
}

function players_load_all(): array
{
    static $cache = null;
    if ($cache !== null) {
        return $cache;
    }

    if (!is_readable(PLAYERS_CSV)) {
        throw new RuntimeException('Không đọc được file dữ liệu: ' . PLAYERS_CSV);
    }

    $handle = fopen(PLAYERS_CSV, 'r');
    if ($handle === false) {
        throw new RuntimeException('Không mở được CSV cầu thủ.');
    }

    $headers = fgetcsv($handle);
    if ($headers === false) {
        fclose($handle);
        throw new RuntimeException('CSV không có dòng tiêu đề.');
    }
    $headers[0] = preg_replace('/^\xEF\xBB\xBF/', '', (string) $headers[0]) ?? $headers[0];

    $players = [];
    while (($row = fgetcsv($handle)) !== false) {
        if (count($row) !== count($headers)) {
            continue;
        }
        $player = array_combine($headers, $row);
        if ($player === false) {
            continue;
        }
        $player['search_blob'] = players_normalize(implode(' ', [
            $player['player_name'] ?? '',
            $player['fbref_name'] ?? '',
            $player['national_team'] ?? '',
            $player['club'] ?? '',
            $player['position'] ?? '',
        ]));
        $players[] = $player;
    }
    fclose($handle);

    $cache = $players;
    return $cache;
}

function players_public_fields(array $player): array
{
    $matched = (string) ($player['is_matched'] ?? '0') === '1';
    return [
        'player_id' => $player['player_id'] ?? '',
        'player_name' => $player['player_name'] ?? '',
        'fbref_name' => $matched ? ($player['fbref_name'] ?? '') : '',
        'national_team' => $player['national_team'] ?? '',
        'nationality' => $player['nationality'] ?? '',
        'club' => $player['club'] ?? '',
        'position' => $player['position'] ?? '',
        'position_group' => $player['position_group'] ?? '',
        'age' => $player['age'] ?? '',
        'height_cm' => $player['height_cm'] ?? '',
        'is_matched' => $matched,
        'minutes' => $player['minutes'] ?? '0',
        'goals' => $player['goals'] ?? '0',
        'assists' => $player['assists'] ?? '0',
        'overall_rating' => $player['overall_rating'] ?? '',
        'goals_p90' => $player['goals_p90'] ?? '0',
        'assists_p90' => $player['assists_p90'] ?? '0',
        'tackles_won' => $player['tackles_won'] ?? '0',
        'save_pct' => $player['save_pct'] ?? '0',
    ];
}

function players_search(string $query, string $team = '', string $position = '', string $matched = '', int $limit = SEARCH_LIMIT): array
{
    $needle = players_normalize($query);
    $teamNorm = players_normalize($team);
    $positionNorm = players_normalize($position);
    $results = [];
    $limit = max(1, $limit);

    foreach (players_load_all() as $player) {
        if ($teamNorm !== '' && players_normalize((string) ($player['national_team'] ?? '')) !== $teamNorm) {
            continue;
        }
        if ($positionNorm !== '' && players_normalize((string) ($player['position_group'] ?? '')) !== $positionNorm) {
            continue;
        }
        if ($matched === '1' && (string) ($player['is_matched'] ?? '0') !== '1') {
            continue;
        }
        if ($matched === '0' && (string) ($player['is_matched'] ?? '0') !== '0') {
            continue;
        }
        if ($needle !== '' && strpos((string) ($player['search_blob'] ?? ''), $needle) === false) {
            continue;
        }
        $results[] = players_public_fields($player);
        if (count($results) >= $limit) {
            break;
        }
    }

    return $results;
}

function players_suggest(string $query, string $team = '', string $position = '', string $matched = ''): array
{
    $needle = players_normalize($query);
    if (mb_strlen($needle, 'UTF-8') < SEARCH_MIN_CHARS) {
        return [];
    }

    $ranked = [];
    foreach (players_search($query, $team, $position, $matched, 80) as $player) {
        $name = players_normalize((string) ($player['player_name'] ?? ''));
        $fbref = players_normalize((string) ($player['fbref_name'] ?? ''));
        $score = 2;
        if (str_starts_with($name, $needle) || ($fbref !== '' && str_starts_with($fbref, $needle))) {
            $score = 0;
        } elseif (strpos($name, $needle) !== false || ($fbref !== '' && strpos($fbref, $needle) !== false)) {
            $score = 1;
        }
        $ranked[] = ['score' => $score, 'player' => $player];
    }

    usort($ranked, static function (array $a, array $b): int {
        return $a['score'] <=> $b['score'];
    });

    $suggestions = [];
    foreach (array_slice($ranked, 0, SUGGEST_LIMIT) as $item) {
        $player = $item['player'];
        $suggestions[] = [
            'player_id' => $player['player_id'],
            'player_name' => $player['player_name'],
            'national_team' => $player['national_team'],
            'club' => $player['club'],
            'position' => $player['position'],
            'overall_rating' => $player['overall_rating'],
        ];
    }

    return $suggestions;
}

function players_filters(): array
{
    $teams = [];
    $positions = [];
    foreach (players_load_all() as $player) {
        $team = trim((string) ($player['national_team'] ?? ''));
        $pos = trim((string) ($player['position_group'] ?? ''));
        if ($team !== '') {
            $teams[$team] = true;
        }
        if ($pos !== '') {
            $positions[$pos] = true;
        }
    }
    $teamList = array_keys($teams);
    sort($teamList, SORT_NATURAL | SORT_FLAG_CASE);
    $posList = array_keys($positions);
    sort($posList, SORT_NATURAL | SORT_FLAG_CASE);
    return ['teams' => $teamList, 'positions' => $posList];
}
