<?php
$title = "TRA CỨU & TÌM KIẾM CẦU THỦ";
?>
<!doctype html>
<html lang="vi">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="description" content="FIFA World Cup 2026 - Player Search Database">
    <title><?= $title ?> — Football ML</title>
    
    <!-- Google Fonts & FontAwesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&family=Cinzel:wght@500;700;900&family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- CSS Styles -->
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/voyage-style.css">

    <style>
        :root {
            --bg-dark: #06080b;
            --surface: #0d1220;
            --card-bg: rgba(17, 24, 39, 0.75);
            --card-border: rgba(255, 255, 255, 0.08);
            --accent-gold: #e2b775;
            --accent-cyan: #00f0ff;
            --accent-green: #22c55e;
            --text-sub: #94a3b8;
            --text-muted: #64748b;
        }

        body {
            background-color: var(--bg-dark);
            color: #ffffff;
            font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
            min-height: 100vh;
        }

        .app-header {
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 40px;
            background: rgba(6, 8, 11, 0.9);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        .player-hero {
            position: relative;
            padding: 60px 40px;
            background: linear-gradient(180deg, rgba(6, 8, 11, 0.6) 0%, rgba(6, 8, 11, 0.95) 100%),
                        url('images/world_map_bg.png') center/cover no-repeat;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        .hero-container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .eyebrow-tag {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-family: 'Space Grotesk', monospace;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.2em;
            color: var(--accent-gold);
            text-transform: uppercase;
            margin-bottom: 12px;
        }

        .hero-title {
            font-family: 'Cinzel', 'Barlow Condensed', serif;
            font-size: clamp(32px, 4vw, 54px);
            font-weight: 800;
            line-height: 1.15;
            color: #ffffff;
            margin-bottom: 16px;
        }

        .hero-desc {
            font-size: 15px;
            line-height: 1.6;
            color: var(--text-sub);
            max-width: 760px;
            margin-bottom: 28px;
        }

        .search-toolbar {
            max-width: 1400px;
            margin: 0 auto 30px auto;
            padding: 20px 24px;
            background: rgba(13, 18, 32, 0.8);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
        }

        .search-input-wrap {
            flex: 1;
            min-width: 280px;
            position: relative;
        }

        .search-input-wrap i {
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
        }

        .search-input {
            width: 100%;
            background: #06080b;
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #fff;
            padding: 12px 16px 12px 44px;
            border-radius: 10px;
            font-family: inherit;
            font-size: 14px;
            outline: none;
            transition: all 0.3s ease;
        }

        .search-input:focus {
            border-color: var(--accent-gold);
            box-shadow: 0 0 16px rgba(226, 183, 117, 0.25);
        }

        .pos-pills {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .pos-pill {
            background: #06080b;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text-sub);
            padding: 10px 18px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.25s ease;
        }

        .pos-pill:hover {
            color: #fff;
            border-color: rgba(255, 255, 255, 0.25);
        }

        .pos-pill.active {
            background: var(--accent-gold);
            color: #000;
            border-color: var(--accent-gold);
            box-shadow: 0 0 14px rgba(226, 183, 117, 0.35);
        }

        .players-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 40px 60px 40px;
        }

        .count-bar {
            font-family: 'Space Grotesk', monospace;
            font-size: 13px;
            color: var(--text-sub);
            margin-bottom: 20px;
        }

        .players-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }

        .player-card {
            background: rgba(13, 18, 32, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 20px;
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1);
            position: relative;
            overflow: hidden;
            text-decoration: none;
            color: inherit;
            display: block;
        }

        .player-card:hover {
            transform: translateY(-6px);
            border-color: rgba(226, 183, 117, 0.45);
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.7), 0 0 20px rgba(226, 183, 117, 0.15);
        }

        .card-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 14px;
        }

        .flag-tag {
            font-family: 'Space Grotesk', monospace;
            font-size: 11px;
            font-weight: 700;
            background: #06080b;
            color: var(--text-sub);
            padding: 3px 8px;
            border-radius: 4px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .badge-pos {
            font-size: 10px;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: 4px;
            letter-spacing: 0.05em;
        }

        .badge-pos.FW { background: rgba(255, 69, 0, 0.15); color: #ff5533; border: 1px solid rgba(255, 69, 0, 0.35); }
        .badge-pos.MF { background: rgba(34, 197, 94, 0.15); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.35); }
        .badge-pos.DF { background: rgba(0, 240, 255, 0.15); color: #00f0ff; border: 1px solid rgba(0, 240, 255, 0.35); }
        .badge-pos.GK { background: rgba(226, 183, 117, 0.15); color: #e2b775; border: 1px solid rgba(226, 183, 117, 0.35); }

        .card-rating {
            text-align: right;
        }

        .card-rating .num {
            font-family: 'Space Grotesk', monospace;
            font-size: 24px;
            font-weight: 900;
            color: var(--accent-gold);
            display: block;
            line-height: 1;
        }

        .card-rating .lbl {
            font-size: 9px;
            color: var(--text-muted);
            font-weight: 700;
            letter-spacing: 0.1em;
        }

        .shirt-avatar {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: #06080b;
            border: 2px solid var(--accent-gold);
            margin: 10px auto 14px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Space Grotesk', monospace;
            font-size: 22px;
            font-weight: 900;
            color: var(--accent-gold);
            box-shadow: 0 0 16px rgba(226, 183, 117, 0.2);
        }

        .player-name {
            font-size: 15px;
            font-weight: 800;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            margin-bottom: 4px;
            text-align: center;
        }

        .player-sub {
            font-size: 12px;
            color: var(--text-sub);
            text-align: center;
            margin-bottom: 14px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .card-stats {
            display: grid;
            grid-template-columns: 1fr 1fr 1.2fr;
            gap: 6px;
            background: #06080b;
            padding: 10px 12px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            font-size: 11px;
            margin-bottom: 14px;
        }

        .card-stats small {
            display: block;
            color: var(--text-muted);
            font-size: 10px;
        }

        .card-stats b {
            color: #fff;
        }

        .btn-profile {
            width: 100%;
            padding: 10px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: var(--text-sub);
            border-radius: 8px;
            font-family: 'Space Grotesk', monospace;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.08em;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }

        .player-card:hover .btn-profile {
            background: var(--accent-gold);
            color: #000;
            border-color: var(--accent-gold);
        }
    </style>
</head>

<body>

    <header class="app-header">
        <a class="brand" href="index.php"><b>FM</b><span>FOOTBALL<small>ML ANALYTICS</small></span></a>
        <nav id="nav">
            <a href="index.php">Trang chủ</a>
            <a href="countries.php">Châu lục</a>
            <a class="active" href="players.php">Cầu thủ</a>
            <a href="ml-analysis.php" style="color:var(--accent-cyan);font-weight:700;">ML Analysis ⚡</a>
            <a href="rankings.php">Bảng xếp hạng</a>
            <a href="statistics.php">Thống kê</a>
        </nav>
        <div class="actions">
            <a href="index.php" class="secondary" style="font-size:12px;padding:6px 14px;">← Quay lại Trang chủ</a>
        </div>
    </header>

    <section class="player-hero">
        <div class="hero-container">
            <div class="eyebrow-tag">● FIFA WORLD CUP 2026 · PLAYER SEARCH DATABASE</div>
            <h1 class="hero-title">TRA CỨU &amp; TÌM KIẾM CẦU THỦ</h1>
            <p class="hero-desc">
                Hệ thống danh sách <strong>888 cầu thủ đã match thông tin</strong> tham dự FIFA World Cup 2026. Lọc theo tên cầu thủ, vị trí thi đấu, câu lạc bộ và đội tuyển quốc gia để xem hồ sơ sinh trắc học chi tiết.
            </p>
        </div>
    </section>

    <main class="players-container">
        <div class="search-toolbar">
            <div class="search-input-wrap">
                <i class="fa-solid fa-magnifying-glass"></i>
                <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm tên cầu thủ, quốc gia, câu lạc bộ... (VD: Vinicius, BRA, Real Madrid...)" oninput="filterPlayers()">
            </div>
            <div class="pos-pills">
                <button class="pos-pill active" data-pos="ALL" onclick="selectPosFilter(this)">TẤT CẢ (888)</button>
                <button class="pos-pill" data-pos="FW" onclick="selectPosFilter(this)">⚽ FW TIỀN ĐẠO</button>
                <button class="pos-pill" data-pos="MF" onclick="selectPosFilter(this)">🔄 MF TIỀN VỆ</button>
                <button class="pos-pill" data-pos="DF" onclick="selectPosFilter(this)">🛡 DF HẬU VỆ</button>
                <button class="pos-pill" data-pos="GK" onclick="selectPosFilter(this)">🧤 GK THỦ MÔN</button>
            </div>
        </div>

        <div class="count-bar" id="countBar">Đang tải dữ liệu 888 cầu thủ...</div>
        <div class="players-grid" id="playersGrid"></div>
    </main>

    <script>
        let allPlayersData = [];
        let filteredPlayers = [];
        let currentPosFilter = 'ALL';

        fetch('assets/js/players_full_data.json')
            .then(res => res.json())
            .then(data => {
                allPlayersData = data;
                
                const urlParams = new URLSearchParams(window.location.search);
                const initialQuery = urlParams.get('q') || '';
                const initialPos = urlParams.get('position') || 'ALL';

                if (initialQuery) {
                    document.getElementById('searchInput').value = initialQuery;
                }
                if (initialPos && initialPos !== 'ALL') {
                    currentPosFilter = initialPos.toUpperCase();
                    document.querySelectorAll('.pos-pill').forEach(btn => {
                        btn.classList.toggle('active', btn.dataset.pos === currentPosFilter);
                    });
                }

                filterPlayers();
            })
            .catch(err => {
                console.error("Lỗi khi tải dữ liệu cầu thủ:", err);
                document.getElementById('countBar').textContent = "Không thể tải dữ liệu cầu thủ.";
            });

        function selectPosFilter(btn) {
            document.querySelectorAll('.pos-pill').forEach(p => p.classList.remove('active'));
            btn.classList.add('active');
            currentPosFilter = btn.dataset.pos;
            filterPlayers();
        }

        function filterPlayers() {
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            filteredPlayers = allPlayersData.filter(p => {
                const matchPos = currentPosFilter === 'ALL' || p.pos === currentPosFilter;
                const matchQuery = !query ||
                    p.name.toLowerCase().includes(query) ||
                    p.team.toLowerCase().includes(query) ||
                    p.club.toLowerCase().includes(query);
                return matchPos && matchQuery;
            });
            renderPlayersGrid();
        }

        function renderPlayersGrid() {
            const grid = document.getElementById('playersGrid');
            const countBar = document.getElementById('countBar');

            countBar.textContent = `Hiển thị ${filteredPlayers.length} / ${allPlayersData.length} cầu thủ`;

            if (!filteredPlayers.length) {
                grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:40px;color:var(--text-muted);">Không tìm thấy cầu thủ phù hợp.</div>`;
                return;
            }

            grid.innerHTML = filteredPlayers.slice(0, 120).map(p => `
                <a href="player.php?id=${p.id}" class="player-card">
                    <div class="card-top">
                        <span class="flag-tag">${p.flag_code}</span>
                        <span class="badge-pos ${p.pos}">${p.pos}</span>
                        <div class="card-rating">
                            <span class="num">${p.rating.toFixed(1)}</span>
                            <span class="lbl">RATING</span>
                        </div>
                    </div>
                    <div class="shirt-avatar">${p.shirt}</div>
                    <div class="player-name">${p.name}</div>
                    <div class="player-sub">${p.team} · ${p.club}</div>
                    <div class="card-stats">
                        <div><small>Tuổi</small><b>${p.age}</b></div>
                        <div><small>Chiều cao</small><b>${p.height}cm</b></div>
                        <div><small>Số trận</small><b>${p.matches}</b></div>
                    </div>
                    <div class="btn-profile">XEM HỒ SƠ ↗</div>
                </a>
            `).join('');
        }
    </script>
</body>

</html>