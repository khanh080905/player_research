<?php
/**
 * Tìm kiếm cầu thủ World Cup 2026
 * Dữ liệu: football_ml/data/players_database.csv
 */

$dataFile = __DIR__ . '/football_ml/data/players_database.csv';

$query      = trim($_GET['q'] ?? '');
$position   = trim($_GET['position'] ?? '');
$team       = trim($_GET['team'] ?? '');
$results    = [];
$allTeams   = [];
$totalRows  = 0;
$error      = null;

function loadPlayers(string $path): array
{
    if (!is_readable($path)) {
        throw new RuntimeException('Không đọc được file dữ liệu: ' . $path);
    }

    $handle = fopen($path, 'r');
    if ($handle === false) {
        throw new RuntimeException('Không mở được file CSV.');
    }

    $headers = fgetcsv($handle);
    if ($headers === false) {
        fclose($handle);
        throw new RuntimeException('File CSV trống hoặc không hợp lệ.');
    }

    $headers = array_map('trim', $headers);
    $players = [];

    while (($row = fgetcsv($handle)) !== false) {
        if (count($row) < count($headers)) {
            $row = array_pad($row, count($headers), '');
        }
        $player = array_combine($headers, array_slice($row, 0, count($headers)));
        if ($player === false) {
            continue;
        }
        $players[] = $player;
    }

    fclose($handle);
    return $players;
}

function matchesFilter(array $player, string $query, string $position, string $team): bool
{
    if ($position !== '' && strcasecmp((string)($player['position'] ?? ''), $position) !== 0) {
        return false;
    }

    if ($team !== '') {
        $nt = (string)($player['national_team'] ?? '');
        $nat = (string)($player['nationality'] ?? '');
        if (strcasecmp($nt, $team) !== 0 && strcasecmp($nat, $team) !== 0) {
            return false;
        }
    }

    if ($query === '') {
        return true;
    }

    $haystack = strtolower(implode(' ', [
        $player['player_name'] ?? '',
        $player['club'] ?? '',
        $player['national_team'] ?? '',
        $player['nationality'] ?? '',
        $player['position'] ?? '',
    ]));

    return str_contains($haystack, strtolower($query));
}

try {
    $players = loadPlayers($dataFile);
    $totalRows = count($players);

    foreach ($players as $p) {
        $code = trim((string)($p['national_team'] ?? ''));
        $name = trim((string)($p['nationality'] ?? ''));
        if ($code !== '') {
            $allTeams[$code] = $name !== '' ? "$name ($code)" : $code;
        }
    }
    asort($allTeams, SORT_NATURAL | SORT_FLAG_CASE);

    $hasFilter = ($query !== '' || $position !== '' || $team !== '');
    if ($hasFilter) {
        foreach ($players as $p) {
            if (matchesFilter($p, $query, $position, $team)) {
                $results[] = $p;
            }
        }
    }
} catch (Throwable $e) {
    $error = $e->getMessage();
}

$positions = ['GK' => 'Thủ môn (GK)', 'DF' => 'Hậu vệ (DF)', 'MF' => 'Tiền vệ (MF)', 'FW' => 'Tiền đạo (FW)'];
$resultCount = count($results);
$hasFilter = ($query !== '' || $position !== '' || $team !== '');
?>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tìm kiếm cầu thủ | World Cup 2026</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="main-wrapper">

        <section id="header">
            <a href="index.html">
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/67/2026_FIFA_World_Cup_logo.svg" class="logo" alt="World Cup 2026 Logo">
            </a>

            <div>
                <ul id="navbar">
                    <li><a href="index.html">Trang chủ</a></li>
                    <li><a href="standings.html">Bảng xếp hạng</a></li>
                    <li><a class="active" href="players.php">Tìm kiếm cầu thủ</a></li>
                    <li><a href="matches.html">Trận đấu</a></li>
                    <li><a href="predict.html">Dự đoán cầu thủ</a></li>
                    <li id="lg-bag">
                        <a href="#"><i class="fa-solid fa-trophy"></i></a>
                    </li>
                </ul>
            </div>
        </section>

        <section id="content-section" class="search-page">
            <div class="search-intro">
                <h2>Tìm kiếm cầu thủ</h2>
                <p>Danh sách <?php echo number_format($totalRows); ?> cầu thủ đăng ký World Cup 2026. Tìm theo tên, CLB, đội tuyển hoặc vị trí.</p>
            </div>

            <form class="search-form" method="get" action="players.php">
                <div class="search-row">
                    <div class="search-field search-field--grow">
                        <label for="q">Từ khóa</label>
                        <input
                            type="text"
                            id="q"
                            name="q"
                            value="<?php echo htmlspecialchars($query, ENT_QUOTES, 'UTF-8'); ?>"
                            placeholder="Tên cầu thủ, CLB, đội tuyển..."
                            autocomplete="off"
                        >
                    </div>

                    <div class="search-field">
                        <label for="position">Vị trí</label>
                        <select id="position" name="position">
                            <option value="">Tất cả</option>
                            <?php foreach ($positions as $code => $label): ?>
                                <option value="<?php echo htmlspecialchars($code); ?>" <?php echo $position === $code ? 'selected' : ''; ?>>
                                    <?php echo htmlspecialchars($label); ?>
                                </option>
                            <?php endforeach; ?>
                        </select>
                    </div>

                    <div class="search-field">
                        <label for="team">Đội tuyển</label>
                        <select id="team" name="team">
                            <option value="">Tất cả</option>
                            <?php foreach ($allTeams as $code => $label): ?>
                                <option value="<?php echo htmlspecialchars($code); ?>" <?php echo $team === $code ? 'selected' : ''; ?>>
                                    <?php echo htmlspecialchars($label); ?>
                                </option>
                            <?php endforeach; ?>
                        </select>
                    </div>

                    <div class="search-actions">
                        <button type="submit" class="btn-search">
                            <i class="fa-solid fa-magnifying-glass"></i> Tìm kiếm
                        </button>
                        <a href="players.php" class="btn-reset">Xóa lọc</a>
                    </div>
                </div>
            </form>

            <?php if ($error): ?>
                <div class="search-message search-message--error">
                    <?php echo htmlspecialchars($error, ENT_QUOTES, 'UTF-8'); ?>
                </div>
            <?php elseif (!$hasFilter): ?>
                <div class="search-message">
                    Nhập từ khóa hoặc chọn bộ lọc rồi nhấn <strong>Tìm kiếm</strong>.
                </div>
            <?php elseif ($resultCount === 0): ?>
                <div class="search-message">
                    Không tìm thấy cầu thủ nào phù hợp.
                </div>
            <?php else: ?>
                <div class="search-meta">
                    Tìm thấy <strong><?php echo number_format($resultCount); ?></strong> cầu thủ
                </div>

                <div class="table-wrap">
                    <table class="players-table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Cầu thủ</th>
                                <th>Đội tuyển</th>
                                <th>CLB</th>
                                <th>Vị trí</th>
                                <th>Tuổi</th>
                                <th>Chiều cao</th>
                                <th>Bàn chân</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($results as $i => $p): ?>
                                <tr>
                                    <td><?php echo $i + 1; ?></td>
                                    <td class="col-name"><?php echo htmlspecialchars($p['player_name'] ?? '', ENT_QUOTES, 'UTF-8'); ?></td>
                                    <td>
                                        <?php
                                        $nat = trim((string)($p['nationality'] ?? ''));
                                        $code = trim((string)($p['national_team'] ?? ''));
                                        echo htmlspecialchars($nat !== '' ? "$nat ($code)" : $code, ENT_QUOTES, 'UTF-8');
                                        ?>
                                    </td>
                                    <td><?php echo htmlspecialchars($p['club'] ?? '—', ENT_QUOTES, 'UTF-8'); ?></td>
                                    <td><span class="pos-badge pos-<?php echo htmlspecialchars(strtolower($p['position'] ?? ''), ENT_QUOTES, 'UTF-8'); ?>"><?php echo htmlspecialchars($p['position'] ?? '—', ENT_QUOTES, 'UTF-8'); ?></span></td>
                                    <td><?php echo htmlspecialchars(($p['age'] ?? '') !== '' ? $p['age'] : '—', ENT_QUOTES, 'UTF-8'); ?></td>
                                    <td><?php echo htmlspecialchars(($p['height_cm'] ?? '') !== '' ? $p['height_cm'] . ' cm' : '—', ENT_QUOTES, 'UTF-8'); ?></td>
                                    <td><?php echo htmlspecialchars(($p['foot'] ?? '') !== '' ? $p['foot'] : '—', ENT_QUOTES, 'UTF-8'); ?></td>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            <?php endif; ?>
        </section>

    </div>

</body>
</html>
