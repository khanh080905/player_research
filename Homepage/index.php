<?php
$continents = [
    ["Europe", "🌍", 55],
    ["Asia", "🌏", 47],
    ["Africa", "🌍", 54],
    ["South America", "🌎", 12],
    ["North America", "🌎", 41],
    ["Oceania", "🌊", 14]
];
$ranking = [
    ["Argentina", "🇦🇷", 92.4],
    ["France", "🇫🇷", 91.8],
    ["Spain", "🇪🇸", 90.7],
    ["Brazil", "🇧🇷", 89.9],
    ["England", "🏴", 89.5]
];
$scorers = [
    ["Erling Haaland", "Manchester City", 24],
    ["Kylian Mbappé", "Real Madrid", 21],
    ["Mohamed Salah", "Liverpool", 19]
];
?>
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="description" content="Football ML analytics homepage">
    <title>Football ML — Football Analytics</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&family=Cinzel:wght@500;700;900&family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/Flip.min.js"></script>
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/voyage-style.css">
</head>

<body>
    <header class="header">
        <a class="brand" href="index.php"><b>FM</b><span>FOOTBALL<small>ML ANALYTICS</small></span></a>
        <nav id="nav"><a class="active" href="#home">Home</a><a href="#continents">Continents</a><a href="players.php">Players</a><a href="ml-analysis.php" style="color:#00f0ff;font-weight:700;">ML Analysis ⚡</a><a href="#rankings">Rankings</a><a href="#statistics">Statistics</a></nav>
        <div class="actions"><button id="searchBtn">⌕</button><a href="login.php">Sign in</a><button id="menuBtn">☰</button></div>
    </header>

    <main>
        <section class="hero" id="home">
            <div>
                <div class="eyebrow">● FOOTBALL × DATA × MACHINE LEARNING</div>
                <h1>THE GAME<br><em>BEYOND</em><br>THE NUMBERS.</h1>
                <p>Explore players, countries and football performance through data-driven analysis and machine learning.</p>
                <div class="buttons"><a class="primary" href="#players">Explore players ↗</a><a class="secondary" href="#continents">Explore countries</a></div>
                <div class="metrics">
                    <div><b>190+</b><span>Countries</span></div>
                    <div><b>10K+</b><span>Players</span></div>
                    <div><b>50+</b><span>Metrics</span></div>
                </div>
            </div>
            <div class="hero-art">
                <div class="pitch"><i>91</i><i>87</i><i>84</i><strong>PLAYER<br><em>INTELLIGENCE</em></strong></div>
                <div class="float f1">PLAYER RATING<strong>91.4</strong><em>+3.2%</em></div>
                <div class="float f2">ML CONFIDENCE<strong>94%</strong><em>HIGH</em></div>
            </div>
        </section>

        <div class="ticker">
            <div>PLAYER SCOUTING　✦　NATIONAL RANKINGS　✦　PERFORMANCE DATA　✦　PLAYER SCOUTING　✦</div>
        </div>

        <section class="section" id="continents">
            <div class="heading">
                <div><small>01 / DISCOVER</small>
                    <h2>EXPLORE THE <em>WORLD (VOYAGE INTERACTIVE)</em></h2>
                </div><a href="countries.php">View all countries ↗</a>
            </div>

            <!-- VOYAGE 5 EXPANDING NAV PANELS -->
            <div class="expanding-nav-panels-section">
                <div class="flex-panels-container">
                    
                    <!-- Panel 1: HOME -->
                    <div class="flex-panel" id="panel-home">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">HOME</h3>
                        <div class="panel-content">
                            <span class="panel-num">01</span>
                            <h4 class="panel-heading">WELCOME TO VOYAGE</h4>
                            <p class="panel-desc">Step into a sanctuary of curated journeys, remote wilderness, and architectural marvels across the globe.</p>
                            <button class="panel-action-btn" data-target="home-modal">
                                <span>Explore sanctuary</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Panel 2: DESTINATIONS -->
                    <div class="flex-panel" id="panel-destinations">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">DESTINATIONS</h3>
                        <div class="panel-content">
                            <span class="panel-num">02</span>
                            <h4 class="panel-heading">TIMED DESTINATION CARDS</h4>
                            <p class="panel-desc">Experience Kyoto, Marrakech, Lofoten, and Cappadocia through interactive timed cards with GSAP FLIP physics.</p>
                            <button class="panel-action-btn primary" id="open-world-map-btn">
                                <span>Open Destination Slider</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Panel 3: ABOUT (ACTIVE BY DEFAULT) -->
                    <div class="flex-panel active" id="panel-about">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">ABOUT</h3>
                        <div class="panel-content">
                            <span class="panel-num">03</span>
                            <h4 class="panel-heading">OUR PHILOSOPHY</h4>
                            <p class="panel-desc">Learn a little more about the process, design engineering, and thinking behind quiet expedition craft.</p>
                            <button class="panel-action-btn" data-target="about-modal">
                                <span>Discover story</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Panel 4: WORK -->
                    <div class="flex-panel" id="panel-work">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">WORK</h3>
                        <div class="panel-content">
                            <span class="panel-num">04</span>
                            <h4 class="panel-heading">SELECTED JOURNEYS</h4>
                            <p class="panel-desc">Explore interactive experiments, photography collections, and recent creative work across four continents.</p>
                            <button class="panel-action-btn" data-target="work-modal">
                                <span>View portfolio</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Panel 5: SERVICES -->
                    <div class="flex-panel" id="panel-services">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">SERVICES</h3>
                        <div class="panel-content">
                            <span class="panel-num">05</span>
                            <h4 class="panel-heading">GET IN TOUCH</h4>
                            <p class="panel-desc">Have a destination in mind? Contact our concierge team to start planning your next journey.</p>
                            <button class="panel-action-btn" data-target="services-modal">
                                <span>Start a project</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- INTERACTIVE WORLD MAP WITH 5 CONTINENTS -->
        <div class="feature-modal world-map-modal" id="world-map-modal">
            <div class="map-top-bar">
                <button class="close-modal-btn" id="close-map-btn">
                    <i class="fa-solid fa-arrow-left"></i>
                    <span>BACK TO PANELS</span>
                </button>

                <div class="map-nav-pills">
                    <button class="map-pill active">EXPLORE CONTINENTS</button>
                    <button class="map-pill">LIVE SCORES</button>
                    <button class="map-pill">GLOBAL NEWS</button>
                    <button class="map-pill">SCHEDULES</button>
                </div>
            </div>

            <div class="world-map-wrapper">
                <div class="map-canvas-container">
                    <div class="svg-map-stage" id="map-stage">
                        <div class="map-zoom-wrapper" id="map-zoom-wrapper">
                            <img src="images/transparent_neon_map.png" alt="FIFA World Cup 2026 Interactive World Map" class="world-map-bg-img">
                            
                            <svg class="world-svg-overlay" viewBox="0 0 1024 655" xmlns="http://www.w3.org/2000/svg">
                                <g class="svg-continent continent-americas" data-continent="americas">
                                    <path d="M 30 180 L 360 120 L 450 140 L 390 230 L 390 340 L 400 420 L 380 510 L 320 640 L 260 640 L 230 520 L 230 430 L 210 340 L 160 260 L 80 250 L 30 180 Z" fill="transparent" />
                                </g>

                                <g class="svg-continent continent-europe" data-continent="europe">
                                    <path d="M 440 220 L 515 140 L 590 150 L 610 220 L 600 290 L 565 330 L 510 330 L 450 300 Z" fill="transparent" />
                                </g>

                                <g class="svg-continent continent-asia" data-continent="asia">
                                    <path d="M 610 140 L 960 120 L 975 210 L 910 340 L 850 430 L 760 450 L 670 410 L 570 370 L 580 280 L 610 210 Z" fill="transparent" />
                                </g>

                                <g class="svg-continent continent-africa" data-continent="africa">
                                    <path d="M 430 320 L 610 320 L 630 390 L 610 470 L 560 520 L 540 570 L 480 570 L 440 460 L 410 390 Z" fill="transparent" />
                                </g>

                                <g class="svg-continent continent-oceania" data-continent="oceania">
                                    <path d="M 765 450 L 945 450 L 960 530 L 920 610 L 820 600 Z" fill="transparent" />
                                </g>
                            </svg>
                        </div>
                    </div>
                </div>

                <div class="map-side-panel">
                    <div class="side-panel-header">
                        <span>HIGHLIGHTED CONTINENTS</span>
                    </div>
                    
                    <div class="continent-list">
                        <div class="continent-card-item" data-continent="americas">
                            <div class="item-head">
                                <span class="num">1.</span>
                                <span class="name">AMERICAS</span>
                                <span class="flags">🇺🇸 🇲🇽 🇨🇦</span>
                            </div>
                            <p class="item-sub">USA, Mexico, Canada hosting details</p>
                            <div class="item-meta">
                                <span><i class="fa-solid fa-flag"></i> 16 Host Cities</span>
                                <span class="badge-tag badge-americas">CONCACAF &amp; CONMEBOL</span>
                            </div>
                        </div>

                        <div class="continent-card-item" data-continent="europe">
                            <div class="item-head">
                                <span class="num">2.</span>
                                <span class="name">EUROPE</span>
                                <span class="icon-pin"><i class="fa-solid fa-location-dot"></i></span>
                            </div>
                            <p class="item-sub">Qualified Teams • Matches • Key Cities</p>
                            <div class="item-meta">
                                <span><i class="fa-solid fa-trophy"></i> 16 Slots</span>
                                <span class="badge-tag badge-europe">UEFA</span>
                            </div>
                        </div>

                        <div class="continent-card-item" data-continent="asia">
                            <div class="item-head">
                                <span class="num">3.</span>
                                <span class="name">ASIA</span>
                                <span class="icon-flag"><i class="fa-solid fa-flag"></i></span>
                            </div>
                            <p class="item-sub">Teams • Events • Data</p>
                            <div class="item-meta">
                                <span><i class="fa-solid fa-users"></i> 8.5 Slots</span>
                                <span class="badge-tag badge-asia">AFC</span>
                            </div>
                        </div>

                        <div class="continent-card-item" data-continent="africa">
                            <div class="item-head">
                                <span class="num">4.</span>
                                <span class="name">AFRICA</span>
                                <span class="icon-flag"><i class="fa-solid fa-flag"></i></span>
                            </div>
                            <p class="item-sub">Teams • Details • Stats</p>
                            <div class="item-meta">
                                <span><i class="fa-solid fa-bolt"></i> 9.5 Slots</span>
                                <span class="badge-tag badge-africa">CAF</span>
                            </div>
                        </div>

                        <div class="continent-card-item" data-continent="oceania">
                            <div class="item-head">
                                <span class="num">5.</span>
                                <span class="name">OCEANIA</span>
                                <span class="icon-flag"><i class="fa-solid fa-flag"></i></span>
                            </div>
                            <p class="item-sub">Teams • Events</p>
                            <div class="item-meta">
                                <span><i class="fa-solid fa-trophy"></i> 1.5 Slots</span>
                                <span class="badge-tag badge-oceania">OFC</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- NATIONAL TEAMS SLIDER WITH HORIZONTAL SCROLLBAR -->
        <div class="feature-modal country-slider-modal" id="country-slider-modal">
            <button class="close-modal-btn" id="back-to-map-btn">
                <i class="fa-solid fa-arrow-left"></i>
                <span>BACK TO WORLD MAP</span>
            </button>

            <div class="modal-continent-header" id="modal-continent-title">
                ASIA • AFC — WORLD CUP 2026
            </div>

            <div class="bg-stage">
                <div class="bg-layer active" id="bg-active"></div>
                <div class="bg-overlay"></div>
            </div>

            <div class="modal-hero-content">
                <div class="info-box">
                    <div class="subtitle-wrap">
                        <span class="location-tag" id="hero-tag">JAPAN • Samurai Blue</span>
                    </div>
                    <h1 class="main-title" id="hero-title">JAPAN</h1>
                    <p class="description" id="hero-desc">
                        Japan - Samurai Blue leads the Asian FIFA rankings with mesmerizing possession control and relentless press.
                    </p>
                    <div class="cta-wrap">
                        <button class="btn-explore" id="hero-cta">
                            <span>EXPLORE TEAM</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>

                <div class="scrollable-cards-wrap">
                    <div class="scrollable-cards-track" id="scrollable-cards-track">
                    </div>
                    
                    <div class="scroll-controls-bar">
                        <button class="nav-arrow prev-btn" id="scroll-prev-btn" aria-label="Scroll Left">
                            <i class="fa-solid fa-chevron-left"></i>
                        </button>
                        
                        <div class="custom-scrollbar-track" id="scrollbar-track">
                            <div class="custom-scrollbar-thumb" id="scrollbar-thumb"></div>
                        </div>

                        <button class="nav-arrow next-btn" id="scroll-next-btn" aria-label="Scroll Right">
                            <i class="fa-solid fa-chevron-right"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- STYLES FOR REDESIGNED SECTION 02 & SECTION 05 -->
        <style>
            .search-toolbar-index {
                padding: 16px 20px;
                background: rgba(13, 18, 32, 0.85);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                display: flex;
                flex-wrap: wrap;
                align-items: center;
                justify-content: space-between;
                gap: 14px;
                margin-bottom: 24px;
            }
            .search-input-wrap-index {
                flex: 1;
                min-width: 260px;
                position: relative;
            }
            .search-input-wrap-index i {
                position: absolute;
                left: 16px;
                top: 50%;
                transform: translateY(-50%);
                color: #64748b;
            }
            .search-input-index {
                width: 100%;
                background: #06080b;
                border: 1px solid rgba(255, 255, 255, 0.15);
                color: #fff;
                padding: 11px 16px 11px 44px;
                border-radius: 10px;
                font-family: inherit;
                font-size: 13px;
                outline: none;
                transition: all 0.3s ease;
            }
            .search-input-index:focus {
                border-color: var(--accent-gold, #e2b775);
                box-shadow: 0 0 16px rgba(226, 183, 117, 0.25);
            }
            .pos-pills-index {
                display: flex;
                gap: 8px;
                flex-wrap: wrap;
            }
            .pos-pill-index {
                background: #06080b;
                border: 1px solid rgba(255, 255, 255, 0.1);
                color: #94a3b8;
                padding: 8px 14px;
                border-radius: 8px;
                font-size: 11px;
                font-weight: 700;
                cursor: pointer;
                transition: all 0.25s ease;
            }
            .pos-pill-index:hover {
                color: #fff;
                border-color: rgba(255, 255, 255, 0.25);
            }
            .pos-pill-index.active {
                background: var(--accent-gold, #e2b775);
                color: #000;
                border-color: var(--accent-gold, #e2b775);
                box-shadow: 0 0 14px rgba(226, 183, 117, 0.35);
            }

            .players-grid-index {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
                gap: 20px;
            }
            .player-card-index {
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
                display: flex;
                flex-direction: column;
            }
            .player-card-index:hover {
                transform: translateY(-6px);
                border-color: rgba(226, 183, 117, 0.45);
                box-shadow: 0 16px 36px rgba(0, 0, 0, 0.7), 0 0 20px rgba(226, 183, 117, 0.15);
            }
            .card-top-index {
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-bottom: 12px;
            }
            .flag-tag-index {
                font-family: 'Space Grotesk', monospace;
                font-size: 11px;
                font-weight: 700;
                background: #06080b;
                color: #94a3b8;
                padding: 3px 8px;
                border-radius: 4px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
            .badge-pos-index {
                font-size: 10px;
                font-weight: 800;
                padding: 3px 8px;
                border-radius: 4px;
                letter-spacing: 0.05em;
            }
            .badge-pos-index.FW { background: rgba(255, 69, 0, 0.15); color: #ff5533; border: 1px solid rgba(255, 69, 0, 0.35); }
            .badge-pos-index.MF { background: rgba(34, 197, 94, 0.15); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.35); }
            .badge-pos-index.DF { background: rgba(0, 240, 255, 0.15); color: #00f0ff; border: 1px solid rgba(0, 240, 255, 0.35); }
            .badge-pos-index.GK { background: rgba(226, 183, 117, 0.15); color: #e2b775; border: 1px solid rgba(226, 183, 117, 0.35); }

            .card-rating-index {
                text-align: right;
            }
            .card-rating-index .num {
                font-family: 'Space Grotesk', monospace;
                font-size: 22px;
                font-weight: 900;
                color: var(--accent-gold, #e2b775);
                display: block;
                line-height: 1;
            }
            .card-rating-index .lbl {
                font-size: 8px;
                color: #64748b;
                font-weight: 700;
                letter-spacing: 0.1em;
            }

            .shirt-avatar-index {
                width: 52px;
                height: 52px;
                border-radius: 50%;
                background: #06080b;
                border: 2px solid var(--accent-gold, #e2b775);
                margin: 6px auto 10px auto;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Space Grotesk', monospace;
                font-size: 20px;
                font-weight: 900;
                color: var(--accent-gold, #e2b775);
                box-shadow: 0 0 16px rgba(226, 183, 117, 0.25);
            }
            .player-name-index {
                font-family: 'Cinzel', serif;
                font-size: 16px;
                font-weight: 800;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                margin-bottom: 4px;
                text-align: center;
                color: #fff;
            }
            .player-sub-index {
                font-size: 11px;
                color: #94a3b8;
                text-align: center;
                margin-bottom: 12px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }
            .card-stats-index {
                display: grid;
                grid-template-columns: 1fr 1fr 1fr;
                gap: 4px;
                background: #06080b;
                padding: 8px;
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.06);
                font-size: 11px;
                margin-bottom: 14px;
                text-align: center;
            }
            .card-stats-index small {
                display: block;
                color: #64748b;
                font-size: 9px;
                margin-bottom: 2px;
            }
            .card-stats-index b {
                color: #fff;
                font-family: 'Space Grotesk', monospace;
            }
            .btn-profile-index {
                width: 100%;
                padding: 9px;
                background: rgba(226, 183, 117, 0.08);
                border: 1px solid rgba(226, 183, 117, 0.3);
                color: var(--accent-gold, #e2b775);
                border-radius: 8px;
                font-family: 'Space Grotesk', monospace;
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 0.08em;
                cursor: pointer;
                transition: all 0.3s ease;
                text-align: center;
                margin-top: auto;
            }
            .player-card-index:hover .btn-profile-index {
                background: var(--accent-gold, #e2b775);
                color: #000;
                border-color: var(--accent-gold, #e2b775);
            }

            /* SECTION 05: INTELLIGENCE STYLES */
            .ml-widget-container {
                background: linear-gradient(135deg, rgba(6,8,11,0.95) 0%, rgba(13,18,32,0.98) 100%);
                border: 1px solid rgba(0, 240, 255, 0.25);
                border-radius: 24px;
                padding: 50px 30px;
                max-width: var(--max);
                margin: 40px auto;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 40px;
                align-items: center;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0, 240, 255, 0.1);
            }
            @media (max-width: 960px) {
                .ml-widget-container {
                    grid-template-columns: 1fr;
                    padding: 30px 20px;
                }
            }
            .v-bar-item {
                margin-bottom: 10px;
            }
            .v-bar-header {
                display: flex;
                justify-content: space-between;
                font-size: 11px;
                font-weight: 700;
                margin-bottom: 4px;
                color: #94a3b8;
                font-family: 'Space Grotesk', monospace;
            }
            .v-bar-track {
                height: 8px;
                background: #06080b;
                border-radius: 4px;
                overflow: hidden;
                border: 1px solid rgba(255,255,255,0.08);
            }
            .v-bar-fill {
                height: 100%;
                background: linear-gradient(90deg, #00f0ff, #22c55e);
                border-radius: 4px;
                box-shadow: 0 0 10px rgba(0, 240, 255, 0.4);
                transition: width 0.5s ease;
            }
            .sim-chip {
                background: #06080b;
                border: 1px solid rgba(255, 255, 255, 0.1);
                color: #94a3b8;
                padding: 6px 12px;
                border-radius: 6px;
                font-size: 11px;
                font-family: 'Space Grotesk', monospace;
                font-weight: 700;
                cursor: pointer;
                transition: all 0.2s ease;
            }
            .sim-chip:hover, .sim-chip.active {
                background: rgba(0, 240, 255, 0.15);
                color: var(--accent-cyan, #00f0ff);
                border-color: rgba(0, 240, 255, 0.4);
            }
        </style>

        <!-- SECTION 02 / SCOUT (REDESIGNED TO MATCH PLAYERS.PHP) -->
        <section class="section" id="players">
            <div class="heading">
                <div>
                    <small style="color:var(--accent-gold, #e2b775);font-family:'Space Grotesk',monospace;font-weight:800;letter-spacing:1px;">02 / SCOUT</small>
                    <h2 style="font-family:'Cinzel',serif;">FIND YOUR <em>PLAYER (888 MATCHED PLAYERS)</em></h2>
                </div>
                <a href="players.php" style="color:var(--accent-gold, #e2b775);font-family:'Space Grotesk',monospace;font-weight:700;font-size:13px;">Browse all 888 players ↗</a>
            </div>

            <!-- SEARCH TOOLBAR PREVIEW MATCHING PLAYERS.PHP -->
            <div class="search-toolbar-index">
                <div class="search-input-wrap-index">
                    <i class="fa-solid fa-magnifying-glass"></i>
                    <input type="text" id="indexSearchInput" class="search-input-index" placeholder="Search player name, country, club... (e.g. Vinicius, Mbappé, Bellingham...)" onkeyup="filterIndexCards()">
                </div>
                <div class="pos-pills-index">
                    <button class="pos-pill-index active" data-pos="" onclick="selectIndexPos(this)">ALL (888)</button>
                    <button class="pos-pill-index" data-pos="FW" onclick="selectIndexPos(this)">⚽ FORWARD (FW)</button>
                    <button class="pos-pill-index" data-pos="MF" onclick="selectIndexPos(this)">🔄 MIDFIELDER (MF)</button>
                    <button class="pos-pill-index" data-pos="DF" onclick="selectIndexPos(this)">🛡 DEFENDER (DF)</button>
                    <button class="pos-pill-index" data-pos="GK" onclick="selectIndexPos(this)">🧤 GOALKEEPER (GK)</button>
                </div>
            </div>

            <!-- 4 FEATURED PLAYER CARDS MATCHING PLAYERS.PHP GRID -->
            <div class="players-grid-index" id="indexPlayersGrid">
                <!-- CARD 1: Bellingham -->
                <a class="player-card-index" href="player.php?id=30" data-name="Jude Bellingham" data-pos="MF" data-country="ENG" data-club="Real Madrid C. F.">
                    <div class="card-top-index">
                        <span class="flag-tag-index">ENG 🏴󠁧󠁢󠁥󠁮󠁧󠁿</span>
                        <span class="badge-pos-index MF">MF · MIDFIELDER</span>
                        <div class="card-rating-index">
                            <span class="num">91.4</span>
                            <span class="lbl">OVERALL</span>
                        </div>
                    </div>
                    <div class="shirt-avatar-index">7</div>
                    <div class="player-name-index">Jude Bellingham</div>
                    <div class="player-sub-index">England · Real Madrid C. F. · 22 yrs · 186 cm</div>
                    <div class="card-stats-index">
                        <div><small>GOALS</small><b>8</b></div>
                        <div><small>ASSISTS</small><b>6</b></div>
                        <div><small>MATCHES</small><b>5</b></div>
                    </div>
                    <div class="btn-profile-index">VIEW PLAYER PROFILE ↗</div>
                </a>

                <!-- CARD 2: Mbappé -->
                <a class="player-card-index" href="player.php?id=3" data-name="Kylian Mbappé" data-pos="FW" data-country="FRA" data-club="Real Madrid C. F.">
                    <div class="card-top-index">
                        <span class="flag-tag-index">FRA 🇫🇷</span>
                        <span class="badge-pos-index FW">FW · FORWARD</span>
                        <div class="card-rating-index">
                            <span class="num">91.8</span>
                            <span class="lbl">OVERALL</span>
                        </div>
                    </div>
                    <div class="shirt-avatar-index">10</div>
                    <div class="player-name-index">Kylian Mbappé</div>
                    <div class="player-sub-index">France · Real Madrid C. F. · 27 yrs · 178 cm</div>
                    <div class="card-stats-index">
                        <div><small>GOALS</small><b>12</b></div>
                        <div><small>ASSISTS</small><b>5</b></div>
                        <div><small>MATCHES</small><b>6</b></div>
                    </div>
                    <div class="btn-profile-index">VIEW PLAYER PROFILE ↗</div>
                </a>

                <!-- CARD 3: Messi -->
                <a class="player-card-index" href="player.php?id=1" data-name="Lionel Messi" data-pos="FW" data-country="ARG" data-club="Inter Miami CF">
                    <div class="card-top-index">
                        <span class="flag-tag-index">ARG 🇦🇷</span>
                        <span class="badge-pos-index FW">FW · FORWARD</span>
                        <div class="card-rating-index">
                            <span class="num">90.5</span>
                            <span class="lbl">OVERALL</span>
                        </div>
                    </div>
                    <div class="shirt-avatar-index">10</div>
                    <div class="player-name-index">Lionel Messi</div>
                    <div class="player-sub-index">Argentina · Inter Miami CF · 38 yrs · 170 cm</div>
                    <div class="card-stats-index">
                        <div><small>GOALS</small><b>10</b></div>
                        <div><small>ASSISTS</small><b>8</b></div>
                        <div><small>MATCHES</small><b>7</b></div>
                    </div>
                    <div class="btn-profile-index">VIEW PLAYER PROFILE ↗</div>
                </a>

                <!-- CARD 4: Haaland -->
                <a class="player-card-index" href="player.php?id=2" data-name="Erling Haaland" data-pos="FW" data-country="NOR" data-club="Manchester City">
                    <div class="card-top-index">
                        <span class="flag-tag-index">NOR 🇳🇴</span>
                        <span class="badge-pos-index FW">FW · FORWARD</span>
                        <div class="card-rating-index">
                            <span class="num">92.1</span>
                            <span class="lbl">OVERALL</span>
                        </div>
                    </div>
                    <div class="shirt-avatar-index">9</div>
                    <div class="player-name-index">Erling Haaland</div>
                    <div class="player-sub-index">Norway · Manchester City · 25 yrs · 195 cm</div>
                    <div class="card-stats-index">
                        <div><small>GOALS</small><b>15</b></div>
                        <div><small>ASSISTS</small><b>3</b></div>
                        <div><small>MATCHES</small><b>6</b></div>
                    </div>
                    <div class="btn-profile-index">VIEW PLAYER PROFILE ↗</div>
                </a>
            </div>
        </section>

        <section class="section split" id="rankings">
            <div class="panel">
                <div class="panelhead">
                    <div><small>03 / RANK</small>
                        <h2>NATIONAL <em>POWER</em></h2>
                    </div><em>UPDATED</em>
                </div>
                <?php foreach ($ranking as $i => $r): ?><div class="row"><span><?= ($i + 1) ?></span><b><?= $r[1] ?> <?= htmlspecialchars($r[0]) ?></b><strong><?= $r[2] ?></strong><em>↗</em></div><?php endforeach; ?>
                <a class="panelLink" href="rankings.php">Full national ranking ↗</a>
            </div>
            <div class="panel" id="statistics">
                <div class="panelhead">
                    <div><small>04 / STATS</small>
                        <h2>TOP <em>SCORERS</em></h2>
                    </div>
                </div>
                <?php foreach ($scorers as $i => $s): ?><div class="scorer"><span>0<?= ($i + 1) ?></span>
                        <div><b><?= htmlspecialchars($s[0]) ?></b><small><?= htmlspecialchars($s[1]) ?></small></div><strong><?= $s[2] ?><small>GOALS</small></strong>
                    </div><?php endforeach; ?>
                <a class="panelLink" href="statistics.php">All player statistics ↗</a>
            </div>
        </section>

        <!-- SECTION 05 / INTELLIGENCE (REDESIGNED TO MATCH ML-ANALYSIS.PHP) -->
        <section class="ml-widget-container" id="ml-intelligence">
            <div style="padding-right:20px;">
                <small style="color:var(--accent-cyan, #00f0ff);font-family:'Space Grotesk',monospace;font-weight:800;letter-spacing:2px;display:block;margin-bottom:8px;">05 / INTELLIGENCE — MACHINE LEARNING ENGINE</small>
                <h2 style="font-family:'Cinzel', serif;font-size:clamp(34px, 4vw, 50px);line-height:1.1;color:#fff;margin:10px 0 16px 0;">FOOTBALL<br><em style="color:var(--accent-cyan, #00f0ff);font-style:normal;">MEETS AI ML.</em></h2>
                <p style="color:#94a3b8;font-size:14px;line-height:1.7;margin-bottom:24px;">
                    Machine Learning model <strong>XGBoost (R² = 90.26%)</strong> analyzing <strong>888 FIFA World Cup 2026 matched players</strong>. Features 5 position-based LED VU-Meters and real-time What-If scenario simulation.
                </p>
                <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:28px;">
                    <span style="font-family:'Space Grotesk',monospace;font-size:11px;font-weight:700;padding:5px 12px;background:rgba(34,197,94,0.12);border:1px solid rgba(34,197,94,0.3);color:#22c55e;border-radius:20px;">● MODEL: XGBoost</span>
                    <span style="font-family:'Space Grotesk',monospace;font-size:11px;font-weight:700;padding:5px 12px;background:rgba(0,240,255,0.12);border:1px solid rgba(0,240,255,0.3);color:#00f0ff;border-radius:20px;">● ACCURACY: R² 90.26%</span>
                    <span style="font-family:'Space Grotesk',monospace;font-size:11px;font-weight:700;padding:5px 12px;background:rgba(226,183,117,0.12);border:1px solid rgba(226,183,117,0.3);color:#e2b775;border-radius:20px;">● MATCHED: 888 PLAYERS</span>
                </div>
                <a class="primary" href="ml-analysis.php" style="background:var(--accent-cyan, #00f0ff);color:#000;font-family:'Space Grotesk',monospace;font-weight:800;padding:14px 28px;border-radius:30px;text-decoration:none;display:inline-block;box-shadow:0 0 24px rgba(0,240,255,0.35);transition:all 0.3s ease;">LAUNCH ML ANALYSIS DASHBOARD ⚡</a>
            </div>

            <!-- INTERACTIVE ML PREVIEW WIDGET -->
            <div style="background:rgba(6,8,11,0.9);border:1px solid rgba(0,240,255,0.25);border-radius:20px;padding:24px;box-shadow:0 20px 50px rgba(0,0,0,0.8);">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,0.08);">
                    <div style="font-family:'Space Grotesk',monospace;font-size:12px;font-weight:800;color:#fff;">🤖 AI MODEL INFERENCE &amp; VU-METER</div>
                    <span style="background:rgba(34,197,94,0.15);color:#22c55e;padding:3px 8px;border-radius:4px;font-size:10px;font-weight:700;font-family:'Space Grotesk',monospace;">LIVE PREVIEW</span>
                </div>

                <!-- PLAYER TOGGLE TAB -->
                <div style="display:flex;gap:6px;margin-bottom:16px;" id="indexMlPlayerTabs">
                    <button class="sim-chip active" onclick="switchIndexMlPlayer('bellingham', this)">BELLINGHAM</button>
                    <button class="sim-chip" onclick="switchIndexMlPlayer('mbappe', this)">MBAPPÉ</button>
                    <button class="sim-chip" onclick="switchIndexMlPlayer('messi', this)">MESSI</button>
                    <button class="sim-chip" onclick="switchIndexMlPlayer('haaland', this)">HAALAND</button>
                </div>

                <!-- 5 LED VU METERS -->
                <div id="indexVuContainer">
                    <div class="v-bar-item">
                        <div class="v-bar-header"><span>PACE ⚡</span><span id="vPaceVal">94.2</span></div>
                        <div class="v-bar-track"><div class="v-bar-fill" id="vPaceBar" style="width:94.2%"></div></div>
                    </div>
                    <div class="v-bar-item">
                        <div class="v-bar-header"><span>SHOOTING ⚽</span><span id="vShootVal">91.5</span></div>
                        <div class="v-bar-track"><div class="v-bar-fill" id="vShootBar" style="width:91.5%"></div></div>
                    </div>
                    <div class="v-bar-item">
                        <div class="v-bar-header"><span>PASSING 🎯</span><span id="vPassVal">89.8</span></div>
                        <div class="v-bar-track"><div class="v-bar-fill" id="vPassBar" style="width:89.8%"></div></div>
                    </div>
                    <div class="v-bar-item">
                        <div class="v-bar-header"><span>DRIBBLING 💫</span><span id="vDribVal">93.1</span></div>
                        <div class="v-bar-track"><div class="v-bar-fill" id="vDribBar" style="width:93.1%"></div></div>
                    </div>
                    <div class="v-bar-item">
                        <div class="v-bar-header"><span>DEFENDING 🛡</span><span id="vDefVal">68.4</span></div>
                        <div class="v-bar-track"><div class="v-bar-fill" id="vDefBar" style="width:68.4%"></div></div>
                    </div>
                </div>

                <!-- SIMULATOR CONTROLS -->
                <div style="background:#06080b;border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:12px;margin-top:16px;">
                    <div style="font-size:11px;color:#94a3b8;font-family:'Space Grotesk',monospace;margin-bottom:8px;display:flex;justify-content:space-between;">
                        <span>WHAT-IF SCENARIO SIMULATION:</span>
                        <b style="color:var(--accent-cyan,#00f0ff);" id="indexSimResult">Rating: 91.4 ➔ 91.8</b>
                    </div>
                    <div style="display:flex;gap:6px;">
                        <button class="sim-chip" onclick="applyIndexSim(30, 0, 0, this)">+30' Mins</button>
                        <button class="sim-chip" onclick="applyIndexSim(0, 1, 0, this)">+1 Goal</button>
                        <button class="sim-chip" onclick="applyIndexSim(0, 0, 1, this)">+1 Assist</button>
                        <button class="sim-chip" onclick="resetIndexSim(this)">Reset</button>
                    </div>
                </div>
            </div>
        </section>

        <script>
            // Section 02 Search & Filter Logic
            let currentSelectedPos = '';
            function selectIndexPos(btn) {
                document.querySelectorAll('.pos-pill-index').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentSelectedPos = btn.getAttribute('data-pos') || '';
                filterIndexCards();
            }

            function filterIndexCards() {
                const query = (document.getElementById('indexSearchInput').value || '').toLowerCase().trim();
                const cards = document.querySelectorAll('#indexPlayersGrid .player-card-index');
                cards.forEach(card => {
                    const name = (card.getAttribute('data-name') || '').toLowerCase();
                    const pos = card.getAttribute('data-pos') || '';
                    const country = (card.getAttribute('data-country') || '').toLowerCase();
                    const club = (card.getAttribute('data-club') || '').toLowerCase();

                    const matchesPos = !currentSelectedPos || pos === currentSelectedPos;
                    const matchesQuery = !query || name.includes(query) || country.includes(query) || club.includes(query);

                    if (matchesPos && matchesQuery) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }

            // Section 05 ML Preview Data & Logic
            const mlPlayerData = {
                bellingham: { pace: 88.5, shoot: 86.4, pass: 91.2, drib: 92.5, def: 78.4, base: 91.4, ai: 91.8 },
                mbappe: { pace: 97.4, shoot: 94.2, pass: 82.5, drib: 93.8, def: 42.1, base: 91.8, ai: 92.3 },
                messi: { pace: 80.2, shoot: 92.8, pass: 96.5, drib: 95.1, def: 38.6, base: 90.5, ai: 91.1 },
                haaland: { pace: 89.6, shoot: 96.1, pass: 72.4, drib: 80.2, def: 45.0, base: 92.1, ai: 92.7 }
            };

            let currentMlPlayerKey = 'bellingham';
            let extraMins = 0;
            let extraGoals = 0;
            let extraAssists = 0;

            function switchIndexMlPlayer(key, btn) {
                document.querySelectorAll('#indexMlPlayerTabs .sim-chip').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentMlPlayerKey = key;
                extraMins = 0;
                extraGoals = 0;
                extraAssists = 0;
                updateIndexMlView();
            }

            function applyIndexSim(mins, goals, assists, btn) {
                extraMins += mins;
                extraGoals += goals;
                extraAssists += assists;
                updateIndexMlView();
            }

            function resetIndexSim(btn) {
                extraMins = 0;
                extraGoals = 0;
                extraAssists = 0;
                updateIndexMlView();
            }

            function updateIndexMlView() {
                const data = mlPlayerData[currentMlPlayerKey] || mlPlayerData.bellingham;
                document.getElementById('vPaceVal').innerText = data.pace.toFixed(1);
                document.getElementById('vPaceBar').style.width = data.pace + '%';

                document.getElementById('vShootVal').innerText = data.shoot.toFixed(1);
                document.getElementById('vShootBar').style.width = data.shoot + '%';

                document.getElementById('vPassVal').innerText = data.pass.toFixed(1);
                document.getElementById('vPassBar').style.width = data.pass + '%';

                document.getElementById('vDribVal').innerText = data.drib.toFixed(1);
                document.getElementById('vDribBar').style.width = data.drib + '%';

                document.getElementById('vDefVal').innerText = data.def.toFixed(1);
                document.getElementById('vDefBar').style.width = data.def + '%';

                const simBoost = (extraMins * 0.015) + (extraGoals * 0.4) + (extraAssists * 0.25);
                const simRating = (data.ai + simBoost).toFixed(1);

                document.getElementById('indexSimResult').innerHTML = `Actual: ${data.base} ➔ AI: ${data.ai} ${simBoost > 0 ? `<span style="color:var(--accent-gold,#e2b775)">(Simulated: ${simRating} ⚡)</span>` : ''}`;
            }
        </script>

        <section class="section">
            <div class="heading">
                <div><small>06 / INSIGHTS</small>
                    <h2>LATEST <em>INSIGHTS</em></h2>
                </div>
            </div>
            <div class="news">
                <?php foreach ([["ML ANALYSIS", "How machine learning can evaluate player performance"], ["SCOUTING", "The next generation of midfielders to watch"], ["DATA", "What goals and assists don't tell you about a player"]] as $n): ?>
                    <article>
                        <div class="newsimg"><?= $n[0] ?></div><small>Today</small>
                        <h3><?= $n[1] ?></h3><a href="#">Read article ↗</a>
                    </article>
                <?php endforeach; ?>
            </div>
        </section>
    </main>

    <footer>
        <div class="footerbrand"><b>FM</b><span>FOOTBALL<small>ML ANALYTICS</small></span></div>
        <p>Football intelligence for the data-driven generation.</p><a href="#home">↑ Back to top</a>
        <hr><small>© <?= date("Y") ?> Football ML</small>
    </footer>
    <div class="overlay" id="overlay"><button id="close">×</button>
        <div><small>GLOBAL SEARCH</small>
            <h2>SEARCH <em>FOOTBALL</em></h2><input placeholder="Player, country, club...">
        </div>
    </div>
    <script src="assets/js/timed-cards.js"></script>
    <script src="assets/js/expanding-panels.js"></script>
    <script src="assets/js/app.js"></script>
</body>

</html>