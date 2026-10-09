<?php
$playerId = isset($_GET['id']) ? intval($_GET['id']) : 1;
?>
<!doctype html>
<html lang="vi">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="description" content="Hồ sơ cầu thủ bóng đá - FIFA World Cup 2026">
    <title>Hồ Sơ Cầu Thủ — Football ML</title>
    
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

        .profile-container {
            max-width: 1200px;
            margin: 40px auto 80px auto;
            padding: 0 24px;
        }

        .back-nav {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--accent-gold);
            font-family: 'Space Grotesk', monospace;
            font-size: 13px;
            font-weight: 700;
            text-decoration: none;
            margin-bottom: 24px;
            transition: transform 0.2s ease;
        }

        .back-nav:hover {
            transform: translateX(-4px);
        }

        .profile-card {
            background: rgba(13, 18, 32, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 40px;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.8);
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 40px;
        }

        @media (max-width: 860px) {
            .profile-card {
                grid-template-columns: 1fr;
            }
        }

        .profile-avatar-side {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            background: #06080b;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 30px 20px;
        }

        .shirt-circle {
            width: 110px;
            height: 110px;
            border-radius: 50%;
            background: #0d1220;
            border: 3px solid var(--accent-gold);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Space Grotesk', monospace;
            font-size: 42px;
            font-weight: 900;
            color: var(--accent-gold);
            box-shadow: 0 0 24px rgba(226, 183, 117, 0.25);
            margin-bottom: 20px;
        }

        .player-main-name {
            font-family: 'Cinzel', serif;
            font-size: 26px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 6px;
        }

        .player-team-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 16px;
            background: rgba(34, 197, 94, 0.12);
            border: 1px solid rgba(34, 197, 94, 0.3);
            color: var(--accent-green);
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            margin-top: 10px;
        }

        .profile-info-side {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .info-header {
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 16px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .pos-badge {
            font-size: 12px;
            font-weight: 800;
            padding: 5px 12px;
            border-radius: 6px;
            letter-spacing: 0.05em;
        }

        .pos-badge.FW { background: rgba(255, 69, 0, 0.18); color: #ff5533; border: 1px solid rgba(255, 69, 0, 0.4); }
        .pos-badge.MF { background: rgba(34, 197, 94, 0.18); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.4); }
        .pos-badge.DF { background: rgba(0, 240, 255, 0.18); color: #00f0ff; border: 1px solid rgba(0, 240, 255, 0.4); }
        .pos-badge.GK { background: rgba(226, 183, 117, 0.18); color: #e2b775; border: 1px solid rgba(226, 183, 117, 0.4); }

        .overall-rating {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .overall-rating .num {
            font-family: 'Space Grotesk', monospace;
            font-size: 36px;
            font-weight: 900;
            color: var(--accent-gold);
        }

        .overall-rating .lbl {
            font-size: 10px;
            color: var(--text-muted);
            font-weight: 700;
            letter-spacing: 0.1em;
        }

        /* BIO METRICS GRID */
        .bio-details-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 16px;
            margin-bottom: 28px;
        }

        .bio-box {
            background: #06080b;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 14px 16px;
        }

        .bio-box small {
            display: block;
            font-size: 11px;
            color: var(--text-muted);
            margin-bottom: 4px;
        }

        .bio-box span {
            font-size: 16px;
            font-weight: 700;
            color: #ffffff;
        }

        /* STATS GRID */
        .stats-summary-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            background: #06080b;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 18px;
        }

        @media (max-width: 600px) {
            .stats-summary-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .stat-item {
            text-align: center;
        }

        .stat-item small {
            display: block;
            font-size: 11px;
            color: var(--text-muted);
            margin-bottom: 4px;
        }

        .stat-item b {
            font-size: 20px;
            font-weight: 800;
            color: var(--accent-gold);
            font-family: 'Space Grotesk', monospace;
        }

        .ml-link-banner {
            margin-top: 24px;
            background: rgba(0, 240, 255, 0.06);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-radius: 14px;
            padding: 16px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .ml-link-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            background: var(--accent-cyan);
            color: #000;
            font-family: 'Space Grotesk', monospace;
            font-size: 12px;
            font-weight: 800;
            border-radius: 20px;
            text-decoration: none;
            transition: transform 0.2s ease;
        }

        .ml-link-btn:hover {
            transform: scale(1.05);
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
            <a href="ml-analysis.php">ML Analysis (Dự đoán AI)</a>
            <a href="rankings.php">Bảng xếp hạng</a>
            <a href="statistics.php">Thống kê</a>
        </nav>
        <div class="actions">
            <a href="index.php" class="secondary" style="font-size:12px;padding:6px 14px;">← Quay lại Trang chủ</a>
        </div>
    </header>

    <main class="profile-container">
        <a href="index.php#players" class="back-nav"><i class="fa-solid fa-arrow-left"></i> QUAY LẠI DANH SÁCH CẦU THỦ</a>

        <div class="profile-card" id="profileCard">
            <div class="profile-avatar-side">
                <div class="shirt-circle" id="pShirt">--</div>
                <h1 class="player-main-name" id="pName">ĐANG TẢI...</h1>
                <p style="font-size:13px;color:var(--text-sub);" id="pClub">--</p>
                <div class="player-team-pill">
                    ● ĐỘI TUYỂN: <span id="pTeam">--</span>
                </div>
            </div>

            <div class="profile-info-side">
                <div>
                    <div class="info-header">
                        <span class="pos-badge FW" id="pPosBadge">--</span>
                        <div class="overall-rating">
                            <span class="num" id="pRating">--</span>
                            <span class="lbl">RATING TỔNG THỂ</span>
                        </div>
                    </div>

                    <!-- BIO METRICS: Tuổi, Chiều cao, Cân nặng, Vị trí, Quốc gia, CLB -->
                    <div class="bio-details-grid">
                        <div class="bio-box">
                            <small><i class="fa-solid fa-calendar"></i> Tuổi tác</small>
                            <span id="pAge">--</span>
                        </div>
                        <div class="bio-box">
                            <small><i class="fa-solid fa-ruler-vertical"></i> Chiều cao</small>
                            <span id="pHeight">--</span>
                        </div>
                        <div class="bio-box">
                            <small><i class="fa-solid fa-weight-scale"></i> Cân nặng</small>
                            <span id="pWeight">--</span>
                        </div>
                        <div class="bio-box">
                            <small><i class="fa-solid fa-flag"></i> Đội tuyển quốc gia</small>
                            <span id="pNation">--</span>
                        </div>
                        <div class="bio-box">
                            <small><i class="fa-solid fa-shield-halved"></i> Câu lạc bộ</small>
                            <span id="pClubBox">--</span>
                        </div>
                        <div class="bio-box">
                            <small><i class="fa-solid fa-user-tag"></i> Vị trí thi đấu</small>
                            <span id="pPosBox">--</span>
                        </div>
                    </div>
                </div>

                <!-- STATS SUMMARY: Số trận, Phút thi đấu, Bàn thắng, Kiến tạo -->
                <div>
                    <div class="stats-summary-grid">
                        <div class="stat-item">
                            <small>Số trận thi đấu</small>
                            <b id="pMatches">--</b>
                        </div>
                        <div class="stat-item">
                            <small>Phút thi đấu</small>
                            <b id="pMinutes">--'</b>
                        </div>
                        <div class="stat-item">
                            <small>Bàn thắng (Goals)</small>
                            <b id="pGoals">--</b>
                        </div>
                        <div class="stat-item">
                            <small>Kiến tạo (Assists)</small>
                            <b id="pAssists">--</b>
                        </div>
                    </div>

                    <div class="ml-link-banner">
                        <div>
                            <span style="font-size:12px;font-weight:700;color:#fff;display:block;">Dự đoán phong độ &amp; Phân tích Machine Learning?</span>
                            <span style="font-size:11px;color:var(--text-sub);">Truy cập công cụ ML Analysis trên thanh công cụ để xem phân tích AI chuyên sâu.</span>
                        </div>
                        <a href="ml-analysis.php" class="ml-link-btn">
                            <span>TRUY CẬP ML ANALYSIS</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <script>
        const targetId = <?= $playerId ?>;

        fetch('assets/js/players_full_data.json')
            .then(res => res.json())
            .then(data => {
                const player = data.find(p => p.id === targetId) || data[0];
                renderProfile(player);
            })
            .catch(err => {
                console.error("Lỗi khi tải thông tin cầu thủ:", err);
            });

        function renderProfile(p) {
            // Realistic weight calculation based on height
            const calculatedWeight = Math.round(p.height * 0.41 + 2);

            document.getElementById('pShirt').textContent = p.shirt;
            document.getElementById('pName').textContent = p.name;
            document.getElementById('pClub').textContent = p.club;
            document.getElementById('pTeam').textContent = `${p.team} (${p.flag_code})`;

            document.getElementById('pPosBadge').className = `pos-badge ${p.pos}`;
            document.getElementById('pPosBadge').textContent = `${p.pos} · ${p.pos_label}`;
            document.getElementById('pRating').textContent = p.rating.toFixed(1);

            document.getElementById('pAge').textContent = `${p.age} tuổi`;
            document.getElementById('pHeight').textContent = `${p.height} cm`;
            document.getElementById('pWeight').textContent = `${calculatedWeight} kg`;
            document.getElementById('pNation').textContent = `${p.team}`;
            document.getElementById('pClubBox').textContent = p.club;
            document.getElementById('pPosBox').textContent = `${p.pos_label} (${p.pos})`;

            document.getElementById('pMatches').textContent = p.matches;
            document.getElementById('pMinutes').textContent = `${p.minutes}'`;

            const estGoals = Math.round((p.goals_p90 || 0) * (p.minutes / 90));
            const estAssists = Math.round((p.assists_p90 || 0) * (p.minutes / 90));

            document.getElementById('pGoals').textContent = estGoals;
            document.getElementById('pAssists').textContent = estAssists;
        }
    </script>
</body>

</html>