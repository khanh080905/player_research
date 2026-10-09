<?php
declare(strict_types=1);

require_once __DIR__ . '/php/load_players.php';

$query = isset($_GET['q']) ? trim((string) $_GET['q']) : '';
$team = isset($_GET['team']) ? trim((string) $_GET['team']) : '';
$position = isset($_GET['position']) ? trim((string) $_GET['position']) : '';
$matched = isset($_GET['matched']) ? trim((string) $_GET['matched']) : '';

$error = '';
$players = [];
$filters = ['teams' => [], 'positions' => []];

try {
    $filters = players_filters();
    $queryReady = $query !== '' && mb_strlen($query, 'UTF-8') >= SEARCH_MIN_CHARS;
    if ($queryReady || $team !== '' || $position !== '' || $matched !== '') {
        $players = $query !== '' && !$queryReady
            ? []
            : players_search($query, $team, $position, $matched);
    }
} catch (Throwable $e) {
    $error = $e->getMessage();
}

function h(?string $value): string
{
    return htmlspecialchars((string) $value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
?>
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tìm kiếm cầu thủ — Voyage WC26</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header class="navbar">
    <div class="nav-container">
      <a href="index.html" class="brand-logo">VOYAGE</a>
      <nav class="nav-links">
        <a class="nav-link-btn" href="index.html">HOME</a>
        <a class="nav-link-btn" href="index.html#panel-destinations">DESTINATIONS</a>
        <a class="nav-link-btn is-active" href="search.php">PLAYERS</a>
        <a class="nav-link-btn" href="index.html#panel-services">ENQUIRE</a>
      </nav>
      <div class="nav-actions">
        <a class="icon-btn" href="search.php" aria-label="Search"><i class="fa-solid fa-magnifying-glass"></i></a>
      </div>
    </div>
  </header>

  <main class="player-search-page">
    <section class="player-search-hero">
      <span class="location-tag">WORLD CUP 2026 / FOOTBALL_ML</span>
      <h1 class="main-title">PLAYERS</h1>
      <p class="description">Tìm cầu thủ từ master dataset, đã khớp với hồ sơ FBref khi có dữ liệu thống kê.</p>

      <form class="player-search-form" id="player-search-page-form" method="get" action="search.php">
        <div class="player-search-field">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input id="player-search-input" type="search" name="q" value="<?php echo h($query); ?>" placeholder="Gõ ít nhất 3 chữ để hiện gợi ý..." autocomplete="off" minlength="3" autofocus>
          <ul class="player-suggest-list" id="player-suggest-list" hidden></ul>
        </div>
        <select id="player-search-team" name="team" aria-label="Đội tuyển">
          <option value="">Tất cả đội tuyển</option>
          <?php foreach ($filters['teams'] as $option): ?>
            <option value="<?php echo h($option); ?>" <?php echo $team === $option ? 'selected' : ''; ?>><?php echo h($option); ?></option>
          <?php endforeach; ?>
        </select>
        <select id="player-search-position" name="position" aria-label="Vị trí">
          <option value="">Tất cả vị trí</option>
          <?php foreach ($filters['positions'] as $option): ?>
            <option value="<?php echo h($option); ?>" <?php echo $position === $option ? 'selected' : ''; ?>><?php echo h($option); ?></option>
          <?php endforeach; ?>
        </select>
        <select id="player-search-matched" name="matched" aria-label="Trạng thái khớp">
          <option value="">Tất cả hồ sơ</option>
          <option value="1" <?php echo $matched === '1' ? 'selected' : ''; ?>>Đã khớp FBref</option>
          <option value="0" <?php echo $matched === '0' ? 'selected' : ''; ?>>Chưa khớp</option>
        </select>
        <button class="btn-explore" type="submit"><span>TÌM KIẾM</span><i class="fa-solid fa-arrow-right"></i></button>
      </form>
    </section>

    <?php if ($error !== ''): ?>
      <p class="player-search-error"><?php echo h($error); ?></p>
    <?php elseif ($query !== '' && mb_strlen($query, 'UTF-8') < SEARCH_MIN_CHARS): ?>
      <p class="player-search-hint">Nhập ít nhất <?php echo SEARCH_MIN_CHARS; ?> chữ cái để hiện gợi ý và tìm kiếm.</p>
    <?php elseif ($query === '' && $team === '' && $position === '' && $matched === ''): ?>
      <p class="player-search-hint">Gõ ít nhất <?php echo SEARCH_MIN_CHARS; ?> chữ cái để hiện gợi ý cầu thủ.</p>
    <?php elseif (!$players): ?>
      <p class="player-search-hint">Không tìm thấy cầu thủ phù hợp.</p>
    <?php else: ?>
      <p class="player-search-hint"><?php echo count($players); ?> kết quả (tối đa <?php echo SEARCH_LIMIT; ?>).</p>
      <div class="player-results">
        <?php foreach ($players as $player): ?>
          <article class="player-card">
            <div class="player-card-top">
              <span class="card-country"><?php echo h($player['national_team']); ?> / <?php echo h($player['position']); ?></span>
              <span class="player-rating"><?php echo h($player['overall_rating']); ?></span>
            </div>
            <h2 class="card-name"><?php echo h($player['player_name']); ?></h2>
            <p class="player-meta"><?php echo h($player['club']); ?> · <?php echo h($player['age']); ?> tuổi · <?php echo h($player['height_cm']); ?> cm</p>
            <p class="player-match <?php echo $player['is_matched'] ? 'is-matched' : 'is-unmatched'; ?>">
              <?php echo $player['is_matched']
                ? 'Khớp FBref: ' . h($player['fbref_name'])
                : 'Chưa có dữ liệu FBref'; ?>
            </p>
            <dl class="player-stats">
              <div><dt>Bàn</dt><dd><?php echo h($player['goals']); ?></dd></div>
              <div><dt>Kiến tạo</dt><dd><?php echo h($player['assists']); ?></dd></div>
              <div><dt>Phút</dt><dd><?php echo h($player['minutes']); ?></dd></div>
              <div><dt>G+A/90</dt><dd><?php echo h((string) ((float) $player['goals_p90'] + (float) $player['assists_p90'])); ?></dd></div>
            </dl>
          </article>
        <?php endforeach; ?>
      </div>
    <?php endif; ?>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-brand">
        <span class="logo">VOYAGE</span>
        <p>Tra cứu cầu thủ World Cup 2026 từ football_ml.</p>
      </div>
      <div class="footer-meta">
        <p>&copy; 2026 VOYAGE. Dữ liệu: players_master_dataset.csv</p>
      </div>
    </div>
  </footer>
  <script src="js/player-search.js"></script>
</body>
</html>
