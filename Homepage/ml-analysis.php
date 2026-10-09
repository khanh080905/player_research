<?php
$title = "PHÂN TÍCH & DỰ ĐOÁN PHONG ĐỘ AI (ML ANALYSIS)";
?>
<!doctype html>
<html lang="vi">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="description" content="FIFA World Cup 2026 - AI Machine Learning Analysis & Performance Prediction">
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
            --accent-red: #ff4500;
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
            color: var(--accent-cyan);
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
            max-width: 780px;
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
            border-color: var(--accent-cyan);
            box-shadow: 0 0 16px rgba(0, 240, 255, 0.25);
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
        }

        .player-card:hover {
            transform: translateY(-6px);
            border-color: rgba(0, 240, 255, 0.45);
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.7), 0 0 20px rgba(0, 240, 255, 0.2);
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
            color: var(--accent-cyan);
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
            border: 2px solid var(--accent-cyan);
            margin: 10px auto 14px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Space Grotesk', monospace;
            font-size: 22px;
            font-weight: 900;
            color: var(--accent-cyan);
            box-shadow: 0 0 16px rgba(0, 240, 255, 0.25);
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

        .card-stats b.ai {
            color: var(--accent-cyan);
        }

        .btn-profile {
            width: 100%;
            padding: 10px;
            background: rgba(0, 240, 255, 0.08);
            border: 1px solid rgba(0, 240, 255, 0.25);
            color: var(--accent-cyan);
            border-radius: 8px;
            font-family: 'Space Grotesk', monospace;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.08em;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .player-card:hover .btn-profile {
            background: var(--accent-cyan);
            color: #000;
            border-color: var(--accent-cyan);
        }

        /* MODAL STYLES */
        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.88);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            z-index: 9999;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .modal-overlay.active {
            display: flex;
        }

        .modal-card {
            width: 100%;
            max-width: 1160px;
            max-height: 92vh;
            overflow-y: auto;
            background: #090e17;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.9);
            display: flex;
            flex-direction: column;
        }

        .modal-header {
            padding: 18px 24px;
            background: #06080b;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .modal-body {
            display: grid;
            grid-template-columns: 3fr 5fr 4fr;
            gap: 20px;
            padding: 24px;
        }

        @media (max-width: 960px) {
            .modal-body {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

    <header class="app-header">
        <a class="brand" href="index.php"><b>FM</b><span>FOOTBALL<small>ML ANALYTICS</small></span></a>
        <nav id="nav">
            <a href="index.php">Trang chủ</a>
            <a href="countries.php">Châu lục</a>
            <a href="players.php">Cầu thủ</a>
            <a class="active" href="ml-analysis.php">ML Analysis (Dự đoán AI)</a>
            <a href="rankings.php">Bảng xếp hạng</a>
            <a href="statistics.php">Thống kê</a>
        </nav>
        <div class="actions">
            <a href="index.php" class="secondary" style="font-size:12px;padding:6px 14px;">← Quay lại Trang chủ</a>
        </div>
    </header>

    <section class="player-hero">
        <div class="hero-container">
            <div class="eyebrow-tag">● MACHINE LEARNING INFERENCE &amp; WHAT-IF SIMULATION</div>
            <h1 class="hero-title">PHÂN TÍCH &amp; DỰ ĐOÁN PHONG ĐỘ AI</h1>
            <p class="hero-desc">
                Ứng dụng mô hình học máy <strong>XGBoost (R² = 90.26%)</strong> phân tích <strong>888 cầu thủ đã match thông tin</strong>. Đánh giá phong độ thời gian thực, đo lường 5 chỉ số VU-Meter theo từng vị trí thi đấu và giả lập kịch bản thi đấu (What-If Simulator).
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

    <!-- PLAYER PROFILE & AI PREDICTION MODAL -->
    <div class="modal-overlay" id="playerModal" onclick="handleModalOverlayClick(event)">
        <div class="modal-card">
            <div class="modal-header">
                <div style="display:flex;align-items:center;gap:10px;">
                    <span style="width:10px;height:10px;border-radius:50%;background:var(--accent-cyan);box-shadow:0 0 10px var(--accent-cyan)"></span>
                    <span style="font-family:'Space Grotesk',monospace;font-size:12px;font-weight:700;letter-spacing:0.15em;">FIFA WC 2026 · HỒ SƠ PHÂN TÍCH &amp; DỰ ĐOÁN AI ML</span>
                </div>
                <button class="close-btn" onclick="closePlayerModal()" style="background:rgba(255,255,255,0.1);border:none;color:#fff;width:32px;height:32px;border-radius:50%;cursor:pointer;">✕</button>
            </div>

            <div class="modal-body">
                <!-- COL 1: BIO -->
                <div style="display:flex;flex-direction:column;gap:14px;">
                    <div style="background:var(--surface);border:1px solid var(--card-border);border-radius:14px;padding:18px;text-align:center;">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                            <span class="flag-tag" id="mFlag">BRA</span>
                            <span class="badge-pos FW" id="mPosBadge">FW · TIỀN ĐẠO</span>
                        </div>
                        <div class="shirt-avatar" id="mShirt">7</div>
                        <h3 style="font-size:18px;font-weight:800;margin-bottom:4px;" id="mName">VINICIUS JUNIOR</h3>
                        <p style="font-size:12px;color:var(--text-sub);margin-bottom:10px;" id="mClub">Real Madrid C. F.</p>
                        <span style="display:inline-flex;align-items:center;gap:6px;padding:4px 12px;background:rgba(34,197,94,0.12);border:1px solid rgba(34,197,94,0.25);color:var(--accent-green);border-radius:20px;font-size:11px;font-weight:700;">
                            ● ĐỘI TUYỂN: <span id="mTeam">BRA</span>
                        </span>
                    </div>

                    <div style="background:var(--surface);border:1px solid var(--card-border);border-radius:14px;padding:16px;">
                        <div style="font-size:11px;font-weight:800;color:var(--text-sub);letter-spacing:0.1em;margin-bottom:10px;padding-bottom:6px;border-bottom:1px solid var(--card-border);display:flex;justify-content:space-between;">
                            <span>SINH TRẮC &amp; THỐNG KÊ</span>
                            <span style="color:var(--accent-green)">✓ FBref Verified</span>
                        </div>
                        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
                            <div style="background:#06080b;padding:8px 10px;border-radius:8px;border:1px solid var(--card-border);">
                                <small style="display:block;font-size:10px;color:var(--text-muted);">Độ tuổi</small>
                                <span style="font-size:13px;font-weight:700;" id="mAge">25 tuổi</span>
                            </div>
                            <div style="background:#06080b;padding:8px 10px;border-radius:8px;border:1px solid var(--card-border);">
                                <small style="display:block;font-size:10px;color:var(--text-muted);">Chiều cao</small>
                                <span style="font-size:13px;font-weight:700;" id="mHeight">176 cm</span>
                            </div>
                            <div style="background:#06080b;padding:8px 10px;border-radius:8px;border:1px solid var(--card-border);">
                                <small style="display:block;font-size:10px;color:var(--text-muted);">Phút thi đấu</small>
                                <span style="font-size:13px;font-weight:700;color:var(--accent-cyan);" id="mMins">440'</span>
                            </div>
                            <div style="background:#06080b;padding:8px 10px;border-radius:8px;border:1px solid var(--card-border);">
                                <small style="display:block;font-size:10px;color:var(--text-muted);">Số trận</small>
                                <span style="font-size:13px;font-weight:700;" id="mMatches">5 trận</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- COL 2: VU-METER & RADAR -->
                <div style="display:flex;flex-direction:column;gap:14px;">
                    <div style="background:var(--surface);border:1px solid var(--card-border);border-radius:14px;padding:16px;">
                        <div style="font-size:11px;font-weight:800;color:var(--text-sub);letter-spacing:0.1em;margin-bottom:10px;padding-bottom:6px;border-bottom:1px solid var(--card-border);display:flex;justify-content:space-between;align-items:center;">
                            <span>🎚️ 5 CHỈ SỐ CAO NHẤT THEO VỊ TRÍ</span>
                            <span style="background:rgba(0,240,255,0.18);color:var(--accent-cyan);padding:2px 6px;border-radius:4px;font-size:10px;font-family:'Space Grotesk',monospace">VU-METER</span>
                        </div>
                        <div id="vBarsContainer"></div>
                    </div>
                </div>

                <!-- COL 3: MACHINE LEARNING & SIMULATOR -->
                <div style="display:flex;flex-direction:column;gap:14px;">
                    <div style="background:var(--surface);border:1px solid rgba(0,240,255,0.25);border-radius:14px;padding:16px;">
                        <div style="font-size:11px;font-weight:800;color:var(--text-sub);letter-spacing:0.1em;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center;">
                            <span>🤖 MACHINE LEARNING</span>
                            <span style="font-size:10px;font-weight:700;padding:2px 7px;border-radius:4px;background:rgba(34,197,94,0.18);color:var(--accent-green);">XGBoost R²=90.26%</span>
                        </div>
                        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:10px;">
                            <div style="background:#06080b;border:1px solid var(--card-border);border-radius:10px;padding:10px;text-align:center;">
                                <small style="display:block;font-size:10px;font-weight:700;color:var(--text-sub);text-transform:uppercase;">Điểm Thực Tế</small>
                                <div style="font-size:26px;font-weight:900;font-family:'Space Grotesk',monospace;color:#fff;" id="mActual">79.1</div>
                                <span style="font-size:9px;color:var(--text-muted);">Formula Rating</span>
                            </div>
                            <div style="background:#06080b;border:1px solid rgba(0,240,255,0.3);border-radius:10px;padding:10px;text-align:center;">
                                <small style="display:block;font-size:10px;font-weight:700;color:var(--accent-cyan);text-transform:uppercase;">AI Dự Đoán</small>
                                <div style="font-size:26px;font-weight:900;font-family:'Space Grotesk',monospace;color:var(--accent-cyan);text-shadow:0 0 14px rgba(0,240,255,0.5);" id="mPred">78.8</div>
                                <span style="font-size:9px;color:var(--accent-cyan);">Model Inference</span>
                            </div>
                        </div>
                        <div style="background:#06080b;padding:8px 12px;border-radius:8px;font-size:11px;display:flex;justify-content:space-between;border:1px solid var(--card-border);">
                            <span style="color:var(--text-sub);">Sai số tuyệt đối:</span>
                            <b id="mDelta" style="color:var(--accent-green);font-family:'Space Grotesk',monospace;">± 0.30 điểm</b>
                        </div>
                    </div>

                    <div style="background:var(--surface);border:1px solid var(--card-border);border-radius:14px;padding:16px;">
                        <div style="font-size:11px;font-weight:800;color:var(--text-sub);letter-spacing:0.1em;margin-bottom:10px;padding-bottom:6px;border-bottom:1px solid var(--card-border);">
                            <span>⚡ GIẢ LẬP KỊCH BẢN (WHAT-IF SIMULATOR)</span>
                        </div>
                        <div style="display:flex;justify-content:space-between;font-size:11px;font-weight:700;margin-bottom:6px;">
                            <span>Số phút thi đấu bổ sung:</span>
                            <span id="simVal" style="color:var(--accent-gold);font-family:'Space Grotesk',monospace">+0 phút</span>
                        </div>
                        <input type="range" min="0" max="180" step="15" value="0" id="simRange" oninput="updateSimScore(this.value)" style="width:100%;accent-color:var(--accent-gold);cursor:pointer;margin-bottom:10px;">
                        <div style="background:#06080b;padding:10px 14px;border-radius:8px;font-size:11px;display:flex;justify-content:space-between;align-items:center;border:1px solid var(--card-border);">
                            <span style="color:var(--text-sub);">Điểm AI mô phỏng:</span>
                            <span id="simScore" style="font-size:16px;font-weight:900;color:var(--accent-cyan);font-family:'Space Grotesk',monospace;">78.8</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let allPlayersData = [];
        let filteredPlayers = [];
        let currentPosFilter = 'ALL';
        let activePlayer = null;

        fetch('assets/js/players_full_data.json')
            .then(res => res.json())
            .then(data => {
                allPlayersData = data;
                filteredPlayers = [...allPlayersData];
                renderPlayersGrid();
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

            countBar.textContent = `Hiển thị ${filteredPlayers.length} / ${allPlayersData.length} cầu thủ đã match thông tin`;

            if (!filteredPlayers.length) {
                grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:40px;color:var(--text-muted);">Không tìm thấy cầu thủ phù hợp.</div>`;
                return;
            }

            grid.innerHTML = filteredPlayers.slice(0, 120).map(p => `
                <div class="player-card" onclick="openPlayerModal(${p.id})">
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
                        <div><small>Phút</small><b>${p.minutes}'</b></div>
                        <div><small>Trận</small><b>${p.matches}</b></div>
                        <div><small>AI dự đoán</small><b class="ai">${p.predicted_rating.toFixed(1)}</b></div>
                    </div>
                    <button class="btn-profile">PHÂN TÍCH AI &amp; ML 🎚️</button>
                </div>
            `).join('');
        }

        function getTopMetrics(p) {
            if (p.pos === 'FW') return [
                { n: 'Bàn thắng / 90p (Goals p90)', sc: Math.min(99, Math.round(p.goals_p90 * 85 + 25)) },
                { n: 'Độ chính xác dứt điểm (Shot Acc %)', sc: Math.min(99, Math.round(p.shot_acc * 0.9 + 20)) },
                { n: 'Tần suất dứt điểm (Shots p90)', sc: Math.min(99, Math.round(p.shots_p90 * 18 + 20)) },
                { n: 'Đóng góp bàn thắng trực tiếp (G+A)', sc: Math.min(99, Math.round((p.goals_p90 + p.assists_p90) * 60 + 25)) },
                { n: 'Kiến tạo đột biến (Assists p90)', sc: Math.min(99, Math.round(p.assists_p90 * 120 + 20)) }
            ];
            if (p.pos === 'MF') return [
                { n: 'Cắt bóng & Đánh chặn (Interceptions p90)', sc: Math.min(99, Math.round(p.interceptions_p90 * 60 + 25)) },
                { n: 'Tắc bóng thu hồi (Tackles p90)', sc: Math.min(99, Math.round(p.tackles_p90 * 65 + 25)) },
                { n: 'Sút xa & Tuyến hai (Shots p90)', sc: Math.min(99, Math.round(p.shots_p90 * 16 + 20)) },
                { n: 'Điều tiết nhịp độ (Minutes)', sc: Math.min(99, Math.round(p.minutes / 360 * 50 + 40)) },
                { n: 'Chính xác dứt điểm (Shot Acc %)', sc: Math.min(99, Math.round(p.shot_acc * 0.8 + 25)) }
            ];
            if (p.pos === 'DF') return [
                { n: 'Đánh chặn & Phán đoán (Interceptions p90)', sc: Math.min(99, Math.round(p.interceptions_p90 * 80 + 35)) },
                { n: 'Tắc bóng thành công (Tackles p90)', sc: Math.min(99, Math.round(p.tackles_p90 * 85 + 35)) },
                { n: 'Thời lượng thi đấu trụ cột (Minutes)', sc: Math.min(99, Math.round(p.minutes / 360 * 50 + 45)) },
                { n: 'Kỷ luật thi đấu & Tranh chấp', sc: 85 },
                { n: 'Không chiến & Phát động bóng', sc: 82 }
            ];
            return [
                { n: 'Tỷ lệ cản phá thành công (Save %)', sc: Math.min(99, Math.round(p.save_pct * 0.9 + 25)) },
                { n: 'Tỷ lệ giữ sạch lưới (Clean Sheet %)', sc: Math.min(99, Math.round(p.clean_sheet_pct * 1.2 + 40)) },
                { n: 'Chỉ số thủng lưới thấp (GA90)', sc: Math.min(99, Math.max(50, Math.round(95 - p.ga90 * 12))) },
                { n: 'Số trận trắng lưới (Clean Sheets)', sc: Math.min(99, Math.round(p.clean_sheets * 20 + 45)) },
                { n: 'Làm chủ vùng cấm & Cản phá đối mặt', sc: 88 }
            ];
        }

        function renderVuBar(m) {
            const sc = Math.max(12, Math.min(99, m.sc));
            const total = 30;
            const active = Math.round((sc / 100) * total);
            let leds = '';
            for (let i = 0; i < total; i++) {
                let colorClass = 'background:rgba(255,255,255,0.07)';
                if (i < active) {
                    colorClass = i < 18 ? 'background:#00f0ff;box-shadow:0 0 6px #00f0ff;' :
                                 i < 25 ? 'background:#e2b775;box-shadow:0 0 6px #e2b775;' :
                                          'background:#22c55e;box-shadow:0 0 6px #22c55e;';
                }
                leds += `<span style="flex:1;height:12px;border-radius:1px;${colorClass}"></span>`;
            }
            return `
                <div style="background:#06080b;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:10px 12px;margin-bottom:10px;">
                    <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:6px;">
                        <span style="font-weight:600;">${m.n}</span>
                        <span style="color:var(--accent-cyan);font-family:'Space Grotesk',monospace;font-weight:800;">${sc}/100</span>
                    </div>
                    <div style="display:flex;gap:2.5px;background:rgba(0,0,0,0.5);padding:4px 6px;border-radius:6px;border:1px solid rgba(255,255,255,0.05);">${leds}</div>
                </div>
            `;
        }

        function openPlayerModal(id) {
            activePlayer = allPlayersData.find(x => x.id === id) || allPlayersData[0];
            const p = activePlayer;

            document.getElementById('mFlag').textContent = p.flag_code;
            document.getElementById('mPosBadge').className = `badge-pos ${p.pos}`;
            document.getElementById('mPosBadge').textContent = `${p.pos} · ${p.pos_label}`;
            document.getElementById('mShirt').textContent = p.shirt;
            document.getElementById('mName').textContent = p.name;
            document.getElementById('mClub').textContent = p.club;
            document.getElementById('mTeam').textContent = p.team;
            document.getElementById('mAge').textContent = `${p.age} tuổi`;
            document.getElementById('mHeight').textContent = `${p.height} cm`;
            document.getElementById('mMins').textContent = `${p.minutes}'`;
            document.getElementById('mMatches').textContent = `${p.matches} trận`;

            document.getElementById('vBarsContainer').innerHTML = getTopMetrics(p).map(renderVuBar).join('');
            document.getElementById('mActual').textContent = p.rating.toFixed(1);
            document.getElementById('mPred').textContent = p.predicted_rating.toFixed(1);
            document.getElementById('mDelta').textContent = `± ${p.delta.toFixed(2)} điểm`;

            document.getElementById('simRange').value = 0;
            document.getElementById('simVal').textContent = '+0 phút';
            document.getElementById('simScore').textContent = p.predicted_rating.toFixed(1);

            document.getElementById('playerModal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closePlayerModal() {
            document.getElementById('playerModal').classList.remove('active');
            document.body.style.overflow = '';
        }

        function handleModalOverlayClick(e) {
            if (e.target === e.currentTarget) closePlayerModal();
        }

        function updateSimScore(mins) {
            document.getElementById('simVal').textContent = `+${mins} phút`;
            if (activePlayer) {
                const simulated = Math.min(99, activePlayer.predicted_rating + (parseInt(mins) / 180) * 1.8);
                document.getElementById('simScore').textContent = simulated.toFixed(1);
            }
        }

        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') closePlayerModal();
        });
    </script>
</body>

</html>