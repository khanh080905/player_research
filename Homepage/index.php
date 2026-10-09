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
                        <span class="location-tag" id="hero-tag">JAPAN / NHẬT BẢN • Samurai Blue</span>
                    </div>
                    <h1 class="main-title" id="hero-title">JAPAN</h1>
                    <p class="description" id="hero-desc">
                        Đội tuyển Nhật Bản - Samurai Blue dẫn đầu vòng loại Châu Á với lối chơi kiểm soát bóng đẳng cấp và bản lĩnh thi đấu tại VCK World Cup.
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

        <section class="section" id="players">
            <div class="heading">
                <div><small>02 / SCOUT</small>
                    <h2>FIND YOUR <em>PLAYER</em></h2>
                </div><a href="players.php">Advanced search ↗</a>
            </div>
            <div class="searchbox">
                <div>⌕ <input id="playerSearch" placeholder="Search player, club or country..."></div><select id="position">
                    <option value="">All positions</option>
                    <option>Forward</option>
                    <option>Midfielder</option>
                    <option>Defender</option>
                    <option>Goalkeeper</option>
                </select><button onclick="findPlayer()">SEARCH PLAYER</button>
            </div>
            <div class="featured">
                <div class="avatar">JB<small>FEATURED</small></div>
                <div class="playertext"><small>PLAYER OF THE WEEK</small>
                    <h3>Jude Bellingham</h3>
                    <p>Midfielder · England</p>
                    <div class="mini"><span><b>8</b> Goals</span><span><b>6</b> Assists</span><span><b>91.4</b> ML Rating</span></div><a class="light" href="player.php?id=1">View profile ↗</a>
                </div>
                <div class="rating"><b>91.4</b><small>ML RATING</small></div>
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

        <section class="ml">
            <div><small>05 / INTELLIGENCE</small>
                <h2>FOOTBALL<br><em>MEETS ML.</em></h2>
                <p>Turn raw football statistics into interpretable player ratings. Compare performance, discover patterns and build data-driven scouting insights.</p><a class="primary" href="ml-analysis.php">Explore ML analysis ↗</a>
            </div>
            <div class="network"><b>ML</b><i>PACE</i><i>GOALS</i><i>PASS</i><i>DEF</i></div>
        </section>

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