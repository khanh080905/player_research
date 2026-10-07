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
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>

<body>
    <header class="header">
        <a class="brand" href="index.php"><b>FM</b><span>FOOTBALL<small>ML ANALYTICS</small></span></a>
        <nav id="nav"><a class="active" href="#home">Home</a><a href="#continents">Continents</a><a href="#players">Players</a><a href="#rankings">Rankings</a><a href="#statistics">Statistics</a></nav>
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
                    <h2>EXPLORE THE <em>WORLD</em></h2>
                </div><a href="countries.php">View all countries ↗</a>
            </div>
            <div class="continents">
                <?php foreach ($continents as $c): ?>
                    <a class="continent" href="countries.php?continent=<?= urlencode($c[0]) ?>"><span><?= $c[1] ?></span><b><?= htmlspecialchars($c[0]) ?></b><small><?= $c[2] ?> countries</small><i>↗</i></a>
                <?php endforeach; ?>
            </div>
        </section>

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
    <script src="assets/js/app.js"></script>
</body>

</html>