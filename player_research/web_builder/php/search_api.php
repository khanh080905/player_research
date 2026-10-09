<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');

require_once __DIR__ . '/load_players.php';

try {
    $query = isset($_GET['q']) ? trim((string) $_GET['q']) : '';
    $team = isset($_GET['team']) ? trim((string) $_GET['team']) : '';
    $position = isset($_GET['position']) ? trim((string) $_GET['position']) : '';
    $matched = isset($_GET['matched']) ? trim((string) $_GET['matched']) : '';
    $mode = isset($_GET['mode']) ? trim((string) $_GET['mode']) : 'search';

    if ($query !== '' && mb_strlen($query, 'UTF-8') < SEARCH_MIN_CHARS) {
        echo json_encode([
            'ok' => true,
            'count' => 0,
            'query' => $query,
            'min_chars' => SEARCH_MIN_CHARS,
            'suggestions' => [],
            'players' => [],
        ], JSON_UNESCAPED_UNICODE);
        return;
    }

    if ($mode === 'suggest') {
        $suggestions = players_suggest($query, $team, $position, $matched);
        echo json_encode([
            'ok' => true,
            'count' => count($suggestions),
            'query' => $query,
            'min_chars' => SEARCH_MIN_CHARS,
            'suggestions' => $suggestions,
        ], JSON_UNESCAPED_UNICODE);
        return;
    }

    $players = players_search($query, $team, $position, $matched);

    echo json_encode([
        'ok' => true,
        'count' => count($players),
        'query' => $query,
        'players' => $players,
    ], JSON_UNESCAPED_UNICODE);
} catch (Throwable $e) {
    http_response_code(500);
    echo json_encode([
        'ok' => false,
        'error' => $e->getMessage(),
        'players' => [],
    ], JSON_UNESCAPED_UNICODE);
}
