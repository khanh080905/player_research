# -*- coding: utf-8 -*-
html_content = '''<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="description" content="FIFA World Cup 2026 — Football Analytics & Machine Learning Portal">
    <title>FIFA World Cup 2026 — Football Analytics &amp; Machine Learning Portal</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&family=Cinzel:wght@500;700;900&family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- GSAP for World Map & Timed Cards Animation -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/Flip.min.js"></script>
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="assets/css/style.css?v=20261014_2">
    <link rel="stylesheet" href="assets/css/voyage-style.css?v=20261014_wc">

    <style>
        :root {
            --accent-gold: #e2b775;
            --accent-cyan: #38bdf8;
            --accent-green: #22c55e;
            --accent-red: #f87171;
            --bg-card: #0d1220;
            --border-glow: rgba(226, 183, 117, 0.25);
        }

        html { scroll-behavior: smooth; }

        /* Section Headings 01 -> 05 in Cinzel serif font */
        .heading h2,
        .ml h2 {
            font-family: 'Cinzel', serif !important;
            font-size: clamp(32px, 4.2vw, 56px) !important;
            font-weight: 700 !important;
            line-height: 1.15 !important;
            letter-spacing: 1.5px !important;
            color: #fff !important;
            margin: 10px 0 !important;
        }

        /* ══════════════ NEWS SECTION: ROW-BASED EDITORIAL LAYOUT ══════════════ */
        .news-list-container {
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin-top: 14px;
        }

        .news-row-card {
            display: flex;
            align-items: center;
            background: rgba(13, 18, 32, 0.72);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 18px 22px;
            gap: 26px;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            backdrop-filter: blur(12px);
        }

        .news-row-card:hover {
            background: rgba(18, 26, 46, 0.92);
            border-color: rgba(226, 183, 117, 0.35);
            transform: translateY(-2px);
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5), 0 0 24px rgba(226, 183, 117, 0.08);
        }

        .news-thumb-wrap {
            flex-shrink: 0;
            width: 250px;
            height: 160px;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
            background: #080d1a;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }

        .news-thumb-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            transition: transform 0.5s ease;
        }

        .news-row-card:hover .news-thumb-img {
            transform: scale(1.05);
        }

        .news-content-wrap {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-width: 0;
        }

        .news-tag {
            font-size: 13px;
            font-weight: 600;
            color: #94a3b8;
            margin-bottom: 6px;
            letter-spacing: 0.3px;
        }

        .news-headline {
            font-size: clamp(18px, 1.9vw, 24px);
            font-weight: 700;
            color: #ffffff;
            line-height: 1.35;
            margin: 0 0 8px 0;
            letter-spacing: -0.2px;
            font-family: 'Inter', -apple-system, sans-serif;
            transition: color 0.25s ease;
        }

        .news-row-card:hover .news-headline {
            color: var(--accent-gold, #e2b775);
        }

        .news-summary {
            font-size: 14px;
            color: #94a3b8;
            line-height: 1.55;
            margin: 0 0 12px 0;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .news-link-row {
            margin-top: 4px;
        }

        .news-direct-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 20px;
            background: rgba(226, 183, 117, 0.12);
            border: 1px solid rgba(226, 183, 117, 0.35);
            color: var(--accent-gold, #e2b775);
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.25s ease;
            letter-spacing: 0.4px;
        }

        .news-direct-link:hover {
            background: var(--accent-gold, #e2b775);
            color: #070b14;
            box-shadow: 0 0 16px rgba(226, 183, 117, 0.4);
            transform: translateX(3px);
        }

        .news-direct-link i {
            font-size: 11px;
            transition: transform 0.25s ease;
        }

        .news-direct-link:hover i {
            transform: translate(2px, -2px);
        }

        @media (max-width: 768px) {
            .news-row-card {
                flex-direction: column;
                align-items: stretch;
                padding: 16px;
                gap: 16px;
            }
            .news-thumb-wrap {
                width: 100%;
                height: 190px;
            }
        }

        /* Header link styling */
        .header {
            position: sticky;
            top: 0;
            background: rgba(6, 10, 16, 0.94);
            backdrop-filter: blur(14px);
            z-index: 1000;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            transition: opacity 0.3s ease, transform 0.3s ease, visibility 0.3s;
        }
        body.modal-open .header,
        body:has(.feature-modal.active) .header,
        body:has(.wc-history-modal.is-open) .header {
            opacity: 0 !important;
            visibility: hidden !important;
            pointer-events: none !important;
            transform: translateY(-100%) !important;
        }

        /* Ensure country-slider-modal is immediately visible on top of world-map-modal */
        .country-slider-modal {
            z-index: 13000 !important;
        }
        .country-slider-modal.active {
            opacity: 1 !important;
            visibility: visible !important;
            transform: scale(1) !important;
            pointer-events: auto !important;
        }
        .country-slider-modal .close-modal-btn {
            z-index: 13100 !important;
        }
        .svg-continent {
            cursor: pointer !important;
            pointer-events: auto !important;
        }
        .svg-continent path {
            pointer-events: all !important;
            cursor: pointer !important;
        }
        .header nav a {
            font-size: 13px;
            font-weight: 700;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            transition: all 0.25s ease;
            cursor: pointer;
            padding: 8px 12px;
            border-radius: 6px;
            text-decoration: none;
        }
        /* ═════════ 6-COLOR NEON NAV ITEMS ═════════ */
        /* 1. Xanh lá (Green) - Home */
        .header nav a.nav-home {
            color: #4ade80;
            border: 1px solid rgba(34, 197, 94, 0.55);
            background: rgba(34, 197, 94, 0.08);
        }
        .header nav a.nav-home:hover, .header nav a.nav-home.active {
            color: #fff;
            background: rgba(34, 197, 94, 0.22);
            border-color: rgba(34, 197, 94, 0.95);
            box-shadow: 0 0 14px rgba(34, 197, 94, 0.4);
        }

        /* 2. Đỏ (Red) - Nations & Map */
        .header nav a.nav-map {
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.55);
            background: rgba(239, 68, 68, 0.08);
        }
        .header nav a.nav-map:hover, .header nav a.nav-map.active {
            color: #fff;
            background: rgba(239, 68, 68, 0.22);
            border-color: rgba(239, 68, 68, 0.95);
            box-shadow: 0 0 14px rgba(239, 68, 68, 0.4);
        }

        /* 3. Tím (Purple) - Player Profiles */
        .header nav a.nav-players {
            color: #c084fc;
            border: 1px solid rgba(168, 85, 247, 0.55);
            background: rgba(168, 85, 247, 0.08);
        }
        .header nav a.nav-players:hover, .header nav a.nav-players.active {
            color: #fff;
            background: rgba(168, 85, 247, 0.22);
            border-color: rgba(168, 85, 247, 0.95);
            box-shadow: 0 0 14px rgba(168, 85, 247, 0.4);
        }

        /* 4. Vàng sáng (Bright Yellow) - Rankings */
        .header nav a.nav-rankings {
            color: #facc15;
            border: 1px solid rgba(250, 204, 21, 0.6);
            background: rgba(250, 204, 21, 0.08);
        }
        .header nav a.nav-rankings:hover, .header nav a.nav-rankings.active {
            color: #fff;
            background: rgba(250, 204, 21, 0.24);
            border-color: rgba(250, 204, 21, 1);
            box-shadow: 0 0 16px rgba(250, 204, 21, 0.45);
        }

        /* 5. Xanh dương (Cyan) - ML Intelligence */
        .header nav a.ml-link, .header nav a.nav-ml {
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.45);
            background: rgba(56, 189, 248, 0.08);
        }
        .header nav a.ml-link:hover, .header nav a.nav-ml:hover, .header nav a.ml-link.active, .header nav a.nav-ml.active {
            color: #fff;
            background: rgba(56, 189, 248, 0.22);
            border-color: rgba(56, 189, 248, 0.95);
            box-shadow: 0 0 14px rgba(56, 189, 248, 0.4);
        }

        /* 6. Vàng champagne (Champagne Gold) - News */
        .header nav a.news-link, .header nav a.nav-news {
            color: #e2b775;
            border: 1px solid rgba(226, 183, 117, 0.45);
            background: rgba(226, 183, 117, 0.08);
            display: inline-flex;
            align-items: center;
            gap: 7px;
        }
        .header nav a.news-link:hover, .header nav a.nav-news:hover, .header nav a.news-link.active, .header nav a.nav-news.active {
            color: #fff;
            background: rgba(226, 183, 117, 0.22);
            border-color: rgba(226, 183, 117, 0.95);
            box-shadow: 0 0 14px rgba(226, 183, 117, 0.4);
        }
        .header nav a.news-link i, .header nav a.nav-news i {
            font-size: 13px;
            color: inherit;
            transition: transform 0.25s ease;
        }
        .header nav a.news-link:hover i, .header nav a.nav-news:hover i {
            transform: scale(1.15);
        }

        #news, .section[id] {
            scroll-margin-top: 80px;
        }

        /* Quick Stat Pill in Hero */
        .hero-metric-box {
            background: rgba(13, 18, 32, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 12px 18px;
            min-width: 130px;
        }
        .hero-metric-box b {
            font-family: 'Space Grotesk', monospace;
            font-size: 24px;
            color: var(--accent-gold);
            display: block;
        }
        .hero-metric-box span {
            font-size: 11px;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* SECTION CTA BUTTONS LINKING TO DEDICATED PAGES */
        .section-cta-wrap {
            text-align: center;
            margin-top: 36px;
            padding-top: 24px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }
        .btn-section-cta {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            padding: 15px 34px;
            background: linear-gradient(135deg, rgba(226, 183, 117, 0.16) 0%, rgba(226, 183, 117, 0.06) 100%);
            border: 1.5px solid var(--accent-gold);
            color: var(--accent-gold);
            border-radius: 30px;
            font-family: 'Space Grotesk', monospace;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            text-decoration: none;
            transition: all 0.3s cubic-bezier(0.22, 1, 0.36, 1);
            box-shadow: 0 10px 28px rgba(0, 0, 0, 0.6);
        }
        .btn-section-cta:hover {
            background: var(--accent-gold);
            color: #000;
            transform: translateY(-3px);
            box-shadow: 0 14px 34px rgba(226, 183, 117, 0.4);
        }
        .btn-section-cta.ml-cta {
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.16) 0%, rgba(56, 189, 248, 0.06) 100%);
            border-color: var(--accent-cyan);
            color: var(--accent-cyan);
        }
        .btn-section-cta.ml-cta:hover {
            background: var(--accent-cyan);
            color: #000;
            box-shadow: 0 14px 34px rgba(56, 189, 248, 0.4);
        }

        /* ── SECTION 02: SPOTLIGHT PLAYERS GRID ── */
        .players-grid-index {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 18px;
        }
        @media (min-width: 1280px) {
            .players-grid-index {
                grid-template-columns: repeat(5, 1fr);
            }
        }
        .player-card-index {
            background: linear-gradient(160deg, #131c2e 0%, #0d1320 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 20px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.22, 1, 0.36, 1);
            position: relative;
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
        }
        .player-card-index:hover {
            transform: translateY(-6px);
            border-color: rgba(226, 183, 117, 0.5);
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
            padding: 4px 10px;
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .badge-pos-index {
            font-size: 11px;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 6px;
            letter-spacing: 0.05em;
        }
        .badge-pos-index.FW { background: rgba(248, 113, 113, 0.18); color: #f87171; border: 1px solid rgba(248, 113, 113, 0.4); }
        .badge-pos-index.MF { background: rgba(74, 222, 128, 0.18); color: #4ade80; border: 1px solid rgba(74, 222, 128, 0.4); }
        .badge-pos-index.DF { background: rgba(56, 189, 248, 0.18); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
        .badge-pos-index.GK { background: rgba(226, 183, 117, 0.18); color: #e2b775; border: 1px solid rgba(226, 183, 117, 0.4); }

        .shirt-avatar-index {
            width: 58px;
            height: 58px;
            border-radius: 50%;
            background: #06080b;
            border: 2px solid var(--accent-gold);
            margin: 6px auto 12px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Space Grotesk', monospace;
            font-size: 22px;
            font-weight: 900;
            color: var(--accent-gold);
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
            margin-bottom: 14px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* 4 BASIC CORE METRICS */
        .card-basic-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            background: #06080b;
            padding: 10px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            margin-bottom: 14px;
        }
        .basic-spec-item {
            display: flex;
            flex-direction: column;
            gap: 2px;
            padding: 6px 8px;
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
        }
        .basic-spec-item .lbl {
            font-size: 9px;
            font-weight: 700;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .basic-spec-item .val {
            font-family: 'Space Grotesk', monospace;
            font-size: 13px;
            font-weight: 800;
            color: #fff;
        }
        .basic-spec-item .val.pos-val { color: var(--accent-gold); }
        .basic-spec-item .val.team-val { color: var(--accent-cyan); }

        .btn-profile-index {
            width: 100%;
            padding: 10px;
            background: rgba(226, 183, 117, 0.08);
            border: 1px solid rgba(226, 183, 117, 0.3);
            color: var(--accent-gold);
            border-radius: 8px;
            font-family: 'Space Grotesk', monospace;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 0.08em;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            margin-top: auto;
        }
        .player-card-index:hover .btn-profile-index {
            background: var(--accent-gold);
            color: #000;
            border-color: var(--accent-gold);
        }

        /* ── SECTION 03 & 04: STANDINGS PREVIEW PODIUM ── */
        .podium {
            display: grid;
            grid-template-columns: 1fr 1.15fr 1fr;
            gap: 14px;
            align-items: end;
            margin-bottom: 24px;
        }
        .podium-card {
            background: linear-gradient(160deg, #131c2e 0%, #0d1320 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 18px;
            text-align: center;
        }
        .podium-card.p1 {
            padding: 26px 18px;
            border-color: rgba(226, 183, 117, 0.55);
            box-shadow: 0 10px 28px rgba(226, 183, 117, 0.15);
        }
        .podium-rank {
            display: inline-flex;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            align-items: center;
            justify-content: center;
            font-family: 'Space Mono', monospace;
            font-weight: 800;
            margin-bottom: 8px;
        }
        .rank-gold .podium-rank { background: var(--accent-gold); color: #000; }
        .rank-silver .podium-rank { background: #94a3b8; color: #000; }
        .rank-bronze .podium-rank { background: #b45309; color: #fff; }
        .podium-card strong { font-family: 'Cinzel', serif; font-weight: 800; display: block; font-size: 16px; margin-bottom: 4px; color: #fff; }
        .podium-card small { font-family: 'Space Grotesk', sans-serif; color: #94a3b8; font-size: 11px; }
        .podium-card b { display: block; margin-top: 8px; color: var(--accent-gold); font-family: 'Space Mono', monospace; font-size: 18px; }

        /* ── SECTION 03: LEADERBOARD PANELS (BEST PLAYERS & GOLDEN BOOT) ── */
        .split {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
            margin-bottom: 24px;
        }
        @media (max-width: 900px) {
            .split { grid-template-columns: 1fr; }
        }
        .panel {
            background: linear-gradient(160deg, #101a2d 0%, #090e18 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 26px 28px;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
        }
        .panelhead {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 18px;
            padding-bottom: 14px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        .panelhead small {
            font-family: 'Space Grotesk', monospace, sans-serif;
            font-size: 11px;
            font-weight: 800;
            color: var(--accent-gold);
            letter-spacing: 1.5px;
            text-transform: uppercase;
            display: block;
            margin-bottom: 4px;
        }
        .panelhead h3 {
            font-family: 'Cinzel', serif;
            font-size: 22px;
            font-weight: 800;
            color: #fff;
            letter-spacing: 0.8px;
            margin: 0;
            line-height: 1.2;
        }
        .panelhead h3 em {
            font-style: normal;
            color: var(--accent-gold);
        }
        .panelhead > em {
            font-family: 'Space Grotesk', monospace, sans-serif;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1px;
            padding: 4px 12px;
            border-radius: 20px;
            background: rgba(226, 183, 117, 0.12);
            color: var(--accent-gold);
            border: 1px solid rgba(226, 183, 117, 0.3);
            font-style: normal;
        }
        .row {
            display: grid;
            grid-template-columns: 36px 1fr auto 24px;
            gap: 12px;
            align-items: center;
            padding: 12px 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            transition: all 0.2s ease;
        }
        .row:hover, .scorer:hover {
            background: rgba(255, 255, 255, 0.03);
        }
        .row:first-of-type, .scorer:first-of-type {
            border-top: none;
        }
        .row > span, .scorer > span {
            font-family: 'Space Mono', monospace;
            font-size: 13px;
            font-weight: 700;
            color: #64748b;
        }
        .row:nth-child(2) > span, .scorer:nth-child(2) > span {
            color: var(--accent-gold);
            font-weight: 800;
        }
        .row:nth-child(3) > span, .scorer:nth-child(3) > span {
            color: #cbd5e1;
            font-weight: 800;
        }
        .row:nth-child(4) > span, .scorer:nth-child(4) > span {
            color: #d97706;
            font-weight: 800;
        }
        .row b, .scorer b {
            font-family: 'Cinzel', serif;
            font-size: 15px;
            font-weight: 800;
            color: #fff;
            letter-spacing: 0.5px;
            display: block;
        }
        .row small, .scorer small {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 11px;
            color: #94a3b8;
            display: block;
            margin-top: 2px;
        }
        .row strong {
            font-family: 'Space Mono', monospace;
            font-size: 18px;
            font-weight: 800;
            color: var(--accent-gold);
            text-align: right;
        }
        .row em {
            font-family: 'Space Mono', monospace;
            font-size: 14px;
            color: var(--accent-green);
            font-style: normal;
            text-align: right;
        }
        .scorer {
            display: grid;
            grid-template-columns: 36px 1fr auto;
            gap: 12px;
            align-items: center;
            padding: 12px 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            transition: all 0.2s ease;
        }
        .scorer > strong {
            font-family: 'Space Mono', monospace;
            font-size: 20px;
            font-weight: 800;
            color: var(--accent-gold);
            text-align: right;
            line-height: 1.1;
        }
        .scorer > strong small {
            display: block;
            font-family: 'Space Grotesk', monospace, sans-serif;
            font-size: 9px;
            font-weight: 800;
            color: #64748b;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            margin-top: 3px;
        }

        /* ── SECTION 05: ML SPOTLIGHT PREVIEW ── */
        .ml-dedicated-section {
            padding: 60px 0;
            border-top: 1px solid rgba(56, 189, 248, 0.2);
            border-bottom: 1px solid rgba(56, 189, 248, 0.2);
            background: radial-gradient(circle at 50% 20%, rgba(14, 28, 48, 0.45) 0%, rgba(6, 10, 16, 0.95) 75%);
        }
        .ml-cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .ml-player-card {
            background: linear-gradient(160deg, #101a2d 0%, #090e18 100%);
            border: 1px solid rgba(56, 189, 248, 0.22);
            border-radius: 16px;
            padding: 20px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.22, 1, 0.36, 1);
            position: relative;
            display: flex;
            flex-direction: column;
        }
        .ml-player-card:hover {
            transform: translateY(-6px);
            border-color: var(--accent-cyan);
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.8), 0 0 22px rgba(56, 189, 248, 0.22);
        }
        .ml-scores-row {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 6px;
            background: #06080b;
            padding: 10px 8px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            margin: 12px 0 14px 0;
            text-align: center;
        }
        .ml-score-col small {
            font-size: 8px;
            color: #64748b;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            display: block;
            margin-bottom: 2px;
        }
        .ml-score-col b {
            font-family: 'Space Mono', monospace;
            font-size: 15px;
            font-weight: 800;
        }
        .ml-score-col.actual b { color: var(--accent-gold); }
        .ml-score-col.pred b { color: var(--accent-cyan); }
        .ml-score-col.delta b { color: var(--accent-green); }

        .btn-ml-inspect {
            width: 100%;
            padding: 9px;
            background: rgba(56, 189, 248, 0.1);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: var(--accent-cyan);
            border-radius: 8px;
            font-family: 'Space Grotesk', monospace;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 0.06em;
            cursor: pointer;
            transition: all 0.25s ease;
            text-align: center;
            margin-top: auto;
        }
        .ml-player-card:hover .btn-ml-inspect {
            background: var(--accent-cyan);
            color: #000;
            border-color: var(--accent-cyan);
        }

        /* ML WORKBENCH PREVIEW */
        .ml-workbench-box {
            background: linear-gradient(135deg, rgba(6, 8, 11, 0.98) 0%, rgba(13, 18, 32, 0.98) 100%);
            border: 1px solid rgba(56, 189, 248, 0.35);
            border-radius: 24px;
            padding: 36px 30px;
            display: grid;
            grid-template-columns: 1fr 1.15fr;
            gap: 36px;
            align-items: center;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 0 35px rgba(56, 189, 248, 0.15);
        }
        @media (max-width: 960px) {
            .ml-workbench-box { grid-template-columns: 1fr; padding: 24px 18px; }
            .podium { grid-template-columns: 1fr; }
        }
        .v-bar-item { margin-bottom: 12px; }
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
            height: 9px;
            background: #06080b;
            border-radius: 5px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.08);
        }
        .v-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #38bdf8, #22c55e);
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
            transition: width 0.5s ease;
        }
        .sim-chip {
            background: #06080b;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #94a3b8;
            padding: 7px 14px;
            border-radius: 6px;
            font-size: 11px;
            font-family: 'Space Grotesk', monospace;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .sim-chip:hover, .sim-chip.active {
            background: rgba(56, 189, 248, 0.15);
            color: var(--accent-cyan);
            border-color: rgba(56, 189, 248, 0.4);
        }

        /* Modal Basic Profile */
        .player-modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.88);
            backdrop-filter: blur(14px);
            z-index: 9999;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .player-modal-overlay.show { display: flex; }
        .pm-box {
            width: 100%;
            max-width: 820px;
            max-height: 90vh;
            overflow-y: auto;
            background: #0d1117;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 18px;
            box-shadow: 0 30px 70px rgba(0, 0, 0, 0.95);
        }
        .pm-hdr {
            padding: 18px 24px;
            background: #090e18;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .pm-close-btn {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #fff;
            width: 34px;
            height: 34px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .pm-body {
            display: grid;
            grid-template-columns: 1fr 1.35fr;
            gap: 24px;
            padding: 28px;
        }
        @media (max-width: 720px) { .pm-body { grid-template-columns: 1fr; padding: 20px; } }
        .pm-card {
            background: #0f1829;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 20px;
        }

        /* ══════════════ STICKY SKYSCRAPER SIDE BANNERS (2X SIZE) ══════════════ */
        .skyscraper-banner {
            position: fixed;
            top: 50%;
            transform: translateY(-50%);
            z-index: 150;
            width: 300px;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            animation: fadeInSkyscraper 0.8s ease-out;
        }

        @keyframes fadeInSkyscraper {
            from {
                opacity: 0;
                transform: translateY(-42%) scale(0.92);
            }
            to {
                opacity: 1;
                transform: translateY(-50%) scale(1);
            }
        }

        .skyscraper-left {
            left: 24px;
        }

        .skyscraper-right {
            right: 24px;
        }

        .skyscraper-card {
            display: flex;
            flex-direction: column;
            text-decoration: none;
            background: rgba(8, 12, 20, 0.94);
            backdrop-filter: blur(14px);
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.14);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
            transition: all 0.3s ease;
        }

        .skyscraper-left .skyscraper-card {
            border-color: rgba(239, 68, 68, 0.45);
            box-shadow: 0 16px 45px rgba(220, 38, 38, 0.28);
        }
        .skyscraper-left:hover .skyscraper-card {
            border-color: rgba(239, 68, 68, 0.95);
            box-shadow: 0 24px 60px rgba(220, 38, 38, 0.55);
            transform: scale(1.03) translateX(6px);
        }

        .skyscraper-right .skyscraper-card {
            border-color: rgba(56, 189, 248, 0.45);
            box-shadow: 0 16px 45px rgba(56, 189, 248, 0.28);
        }
        .skyscraper-right:hover .skyscraper-card {
            border-color: rgba(56, 189, 248, 0.95);
            box-shadow: 0 24px 60px rgba(56, 189, 248, 0.55);
            transform: scale(1.03) translateX(-6px);
        }

        .skyscraper-tag {
            font-family: 'Space Grotesk', monospace;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 2px;
            padding: 10px 14px;
            text-align: center;
            text-transform: uppercase;
        }
        .tag-portugal {
            background: linear-gradient(90deg, rgba(220, 38, 38, 0.4), rgba(16, 185, 129, 0.28));
            color: #fca5a5;
            border-bottom: 1px solid rgba(220, 38, 38, 0.4);
        }
        .tag-argentina {
            background: linear-gradient(90deg, rgba(56, 189, 248, 0.4), rgba(226, 183, 117, 0.28));
            color: #bae6fd;
            border-bottom: 1px solid rgba(56, 189, 248, 0.4);
        }

        .skyscraper-img-wrap {
            width: 100%;
            line-height: 0;
            overflow: hidden;
            background: #000;
        }

        .skyscraper-img {
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
            transition: transform 0.4s ease;
        }
        .skyscraper-banner:hover .skyscraper-img {
            transform: scale(1.03);
        }

        .skyscraper-footer {
            padding: 12px 16px 16px;
            display: flex;
            flex-direction: column;
            gap: 4px;
            text-align: center;
        }
        .footer-portugal {
            background: rgba(18, 6, 8, 0.96);
        }
        .footer-argentina {
            background: rgba(6, 14, 24, 0.96);
        }

        .skyscraper-title {
            font-family: 'Cinzel', serif;
            font-weight: 800;
            font-size: 15px;
            letter-spacing: 1.5px;
            color: #fff;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .skyscraper-sub {
            font-family: 'Space Grotesk', monospace;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.8px;
        }
        .footer-portugal .skyscraper-sub { color: #f87171; }
        .footer-argentina .skyscraper-sub { color: #38bdf8; }

        .skyscraper-close-btn {
            position: absolute;
            top: -12px;
            right: -12px;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #94a3b8;
            font-size: 17px;
            font-weight: 700;
            line-height: 1;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 160;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
        }
        .skyscraper-close-btn:hover {
            background: #ef4444;
            color: #fff;
            border-color: #ef4444;
            transform: scale(1.15);
        }

        @media (max-width: 1750px) {
            .skyscraper-banner {
                width: clamp(220px, 15vw, 270px);
            }
            .skyscraper-left { left: 12px; }
            .skyscraper-right { right: 12px; }
        }
        @media (max-width: 1380px) {
            .skyscraper-banner {
                display: none !important;
            }
        }
    </style>
</head>

<body>
    <!-- ══════════════ HEADER NAVIGATION ══════════════ -->
    <header class="header">
        <a class="brand" href="index.html">
            <b>FM</b><span>FOOTBALL<small>ANALYTICS</small></span>
        </a>
        <nav id="nav">
            <a class="nav-home active" href="#home">Home</a>
            <a class="nav-map" href="#continents" onclick="openWorldMap();return false;">Nations &amp; Map 🌍</a>
            <a class="nav-players" href="players.html">Player Profiles 👤</a>
            <a class="nav-rankings" href="ranking.html">Rankings 🏆</a>
            <a class="nav-ml ml-link" href="ml-intelligence.html">ML Intelligence ⚡</a>
            <a class="nav-news news-link" href="#news"><i class="fa-solid fa-newspaper"></i> News</a>
        </nav>
        <div class="actions">
            <button id="menuBtn">☰</button>
        </div>
    </header>

    <!-- ══════════════ STICKY SKYSCRAPER SIDE BANNERS ══════════════ -->
    <div class="skyscraper-banner skyscraper-left" id="bannerPortugal">
        <button class="skyscraper-close-btn" onclick="document.getElementById('bannerPortugal').style.display='none'" title="Close banner">×</button>
        <a href="players.html?q=Ronaldo" class="skyscraper-card" title="Cristiano Ronaldo — Portugal World Cup 2026">
            <div class="skyscraper-tag tag-portugal">🇵🇹 PORTUGAL</div>
            <div class="skyscraper-img-wrap">
                <img src="assets/images/banner_portugal.png" alt="Cristiano Ronaldo - Portugal World Cup 2026" class="skyscraper-img">
            </div>
            <div class="skyscraper-footer footer-portugal">
                <span class="skyscraper-title">CRISTIANO RONALDO</span>
                <span class="skyscraper-sub">WC 2026 · FINAL DANCE ⚡</span>
            </div>
        </a>
    </div>

    <div class="skyscraper-banner skyscraper-right" id="bannerArgentina">
        <button class="skyscraper-close-btn" onclick="document.getElementById('bannerArgentina').style.display='none'" title="Close banner">×</button>
        <a href="players.html?q=Messi" class="skyscraper-card" title="Lionel Messi — Argentina World Cup 2026">
            <div class="skyscraper-tag tag-argentina">🇦🇷 ARGENTINA</div>
            <div class="skyscraper-img-wrap">
                <img src="assets/images/banner_argentina.png" alt="Lionel Messi - Argentina World Cup 2026" class="skyscraper-img">
            </div>
            <div class="skyscraper-footer footer-argentina">
                <span class="skyscraper-title">LIONEL MESSI</span>
                <span class="skyscraper-sub">WC 2026 · DEFENDING CHAMPION ★</span>
            </div>
        </a>
    </div>

    <main>
        <!-- ══════════════ HERO SECTION ══════════════ -->
        <section class="hero" id="home">
            <div>
                <div class="eyebrow">● FOOTBALL × DATA × MACHINE LEARNING</div>
                <h1>THE GAME<br><em>BEYOND</em><br>THE NUMBERS.</h1>
                <p>Welcome to the FIFA World Cup 2026 Analytics Hub. Explore interactive world maps, sample player biometrics, tournament standings, and machine learning performance predictions.</p>
                
                <div class="metrics" style="margin-top:36px;display:flex;gap:14px;flex-wrap:wrap">
                    <div class="hero-metric-box">
                        <b>48</b>
                        <span>Nations at WC 2026</span>
                    </div>
                    <div class="hero-metric-box">
                        <b style="color:var(--accent-cyan)">888+</b>
                        <span>Master Player Profiles</span>
                    </div>
                    <div class="hero-metric-box">
                        <b style="color:var(--accent-green)">90.26%</b>
                        <span>AI Accuracy (R²)</span>
                    </div>
                    <div class="hero-metric-box">
                        <b style="color:#fff">50+</b>
                        <span>Advanced Metrics</span>
                    </div>
                </div>
            </div>

            <div class="hero-art">
                <div class="pitch"><i>91</i><i>87</i><i>84</i><strong>PLAYER<br><em>INTELLIGENCE</em></strong></div>
                <div class="float f1">PLAYER RATING<strong>91.4</strong><em>+3.2%</em></div>
                <div class="float f2">ML CONFIDENCE<strong>94%</strong><em>HIGH</em></div>
            </div>
        </section>

        <!-- ══════════════ TICKER ══════════════ -->
        <div class="ticker">
            <div>✦ WORLD NATIONS ✦ INTERACTIVE MAP ✦ BASIC PLAYER PROFILES ✦ FEATURED PLAYERS RANKINGS ✦ MACHINE LEARNING INTELLIGENCE ✦ VU-METER WHAT-IF SIMULATOR ✦</div>
        </div>

        <!-- ══════════════ SECTION 01: EXPLORE THE WORLD ══════════════ -->
        <section class="section" id="continents">
            <div class="heading">
                <div>
                    <h2>01 / EXPLORE THE WORLD</h2>
                </div>
            </div>

            <!-- VOYAGE 5 EXPANDING NAV PANELS -->
            <div class="expanding-nav-panels-section">
                <div class="flex-panels-container">
                    
                    <!-- Panel 1: HOME -->
                    <div class="flex-panel" id="panel-home">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">WC 2026</h3>
                        <div class="panel-content">
                            <span class="panel-num">01</span>
                            <h4 class="panel-heading">FIFA WORLD CUP 2026</h4>
                            <p class="panel-desc">The largest World Cup in football history featuring 48 national teams hosted across USA, Mexico, and Canada.</p>
                            <button class="panel-action-btn" onclick="openWorldMap()">
                                <span>Explore Nations</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Panel 2: DESTINATIONS / MAP -->
                    <div class="flex-panel" id="panel-destinations">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">MAP</h3>
                        <div class="panel-content">
                            <span class="panel-num">02</span>
                            <h4 class="panel-heading">INTERACTIVE WORLD MAP</h4>
                            <p class="panel-desc">Visualize 5 participating continents via glowing neon vector map, national rosters, and host cities.</p>
                            <button class="panel-action-btn primary" id="open-world-map-btn">
                                <span>Open World Map</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Panel 3: ABOUT / ML -->
                    <div class="flex-panel active" id="panel-about">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">AI ML</h3>
                        <div class="panel-content">
                            <span class="panel-num">03</span>
                            <h4 class="panel-heading">MACHINE LEARNING INTELLIGENCE</h4>
                            <p class="panel-desc">XGBoost &amp; Random Forest models achieving R²=90.26% accuracy to predict player performance &amp; What-If scenarios.</p>
                            <a class="panel-action-btn" href="ml-intelligence.html" style="text-decoration:none;">
                                <span>Explore ML Portal</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>

                    <!-- Panel 4: PLAYERS -->
                    <div class="flex-panel" id="panel-work">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">PLAYERS</h3>
                        <div class="panel-content">
                            <span class="panel-num">04</span>
                            <h4 class="panel-heading">PLAYER PROFILES</h4>
                            <p class="panel-desc">Search player profiles: Playing Position, National Team, Height, Weight, Age, and Club affiliation.</p>
                            <a class="panel-action-btn" href="players.html" style="text-decoration:none;">
                                <span>Search All 888+</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>

                    <!-- Panel 5: RANKINGS -->
                    <div class="flex-panel" id="panel-services">
                        <div class="panel-bg" style="background-image: url('https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1200&q=80');"></div>
                        <div class="panel-overlay"></div>
                        <h3 class="flex-title">RANKINGS</h3>
                        <div class="panel-content">
                            <span class="panel-num">05</span>
                            <h4 class="panel-heading">FEATURED PLAYERS</h4>
                            <p class="panel-desc">Tournament standings, goals, assists and performance ratings of premier star players from the master dataset.</p>
                            <a class="panel-action-btn" href="ranking.html" style="text-decoration:none;">
                                <span>View Player Rankings</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- ══════════════ MODAL: INTERACTIVE WORLD MAP WITH 5 CONTINENTS ══════════════ -->
        <div class="feature-modal world-map-modal" id="world-map-modal">
            <div class="map-top-bar">
                <button class="close-modal-btn" id="close-map-btn">
                    <i class="fa-solid fa-arrow-left"></i>
                    <span>BACK TO HOME</span>
                </button>

            </div>

            <div class="world-map-wrapper">
                <div class="map-canvas-container">
                    <div class="svg-map-stage" id="map-stage">
                        <div class="map-zoom-wrapper" id="map-zoom-wrapper">
                            <img src="assets/images/transparent_neon_map.png" alt="FIFA World Cup 2026 Interactive World Map" class="world-map-bg-img">
                            
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
                        <span>🌍 5 CONTINENTS &amp; QUALIFICATION SLOTS</span>
                    </div>
                    
                    <div class="continent-list">
                        <div class="continent-card-item" data-continent="americas">
                            <div class="item-head">
                                <span class="num">1.</span>
                                <span class="name">AMERICAS</span>
                                <span class="flags">🇺🇸 🇲🇽 🇨🇦</span>
                            </div>
                            <p class="item-sub">Co-hosts &amp; CONMEBOL qualification</p>
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
                                <span><i class="fa-solid fa-trophy"></i> 16 Finals Slots</span>
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
                                <span><i class="fa-solid fa-users"></i> 8.5 Finals Slots</span>
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
                                <span><i class="fa-solid fa-bolt"></i> 9.5 Finals Slots</span>
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
                                <span><i class="fa-solid fa-trophy"></i> 1.5 Finals Slots</span>
                                <span class="badge-tag badge-oceania">OFC</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ══════════════ MODAL: NATIONAL TEAMS SLIDER ══════════════ -->
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
                            <span>VIEW PLAYER ROSTER</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>

                <div class="scrollable-cards-wrap">
                    <div class="scrollable-cards-track" id="scrollable-cards-track"></div>
                    
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

        <!-- ══════════════ SECTION 02: BASIC PROFILE SPOTLIGHT ══════════════ -->
        <section class="section" id="players">
            <div class="heading">
                <div>
                    <h2>02 / BASIC PROFILE SPOTLIGHT</h2>
                </div>
            </div>

            <!-- SPOTLIGHT SAMPLE PLAYERS GRID (5 PLAYERS) -->
            <div class="players-grid-index" id="indexPlayersGrid"></div>

            <!-- PROMINENT BUTTON LINKING TO DEDICATED PLAYERS.HTML PAGE -->
            <div class="section-cta-wrap">
                <a href="players.html" class="btn-section-cta">
                    <span>EXPLORE ALL 888+ PLAYERS &amp; FULL DATABASE</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </a>
            </div>
        </section>

        <!-- ══════════════ SECTION 03: RANKINGS ══════════════ -->
        <section class="section" id="rankings">
            <div class="heading">
                <div>
                    <h2>03 / RANKINGS</h2>
                </div>
                <span class="live-pill" style="font-size:11px;font-weight:700;padding:5px 12px;border-radius:20px;background:rgba(34,197,94,.15);border:1px solid rgba(34,197,94,.3);color:#22c55e;">
                    ● LIVE STANDINGS PREVIEW
                </span>
            </div>

            <!-- TOP 3 PODIUM PREVIEW (PLAYERS) -->
            <div class="podium">
                <div class="podium-card rank-silver">
                    <span class="podium-rank">2</span>
                    <strong>Erling Haaland</strong>
                    <small>Forward · Norway (Man City)</small>
                    <b>91.8</b>
                </div>
                <div class="podium-card p1 rank-gold">
                    <span class="podium-rank">1</span>
                    <strong style="font-size:18px;">🏆 Kylian Mbappé</strong>
                    <small>Forward · France (Real Madrid)</small>
                    <b style="font-size:22px;">92.4</b>
                </div>
                <div class="podium-card rank-bronze">
                    <span class="podium-rank">3</span>
                    <strong>Vinicius Junior</strong>
                    <small>Forward · Brazil (Real Madrid)</small>
                    <b>90.7</b>
                </div>
            </div>

            <!-- QUICK SUMMARY SPLIT (SAMPLE 5 PLAYERS & 5 SCORERS) -->
            <div class="split">
                <div class="panel">
                    <div class="panelhead">
                        <div>
                            <small>BEST PLAYERS</small>
                            <h3>OVERALL <em>RATING</em></h3>
                        </div>
                        <em>TOP 5</em>
                    </div>
                    <div class="row"><span>01</span><div><b>🇫🇷 Kylian Mbappé</b><small>Real Madrid · France</small></div><strong>92.4</strong><em>↗</em></div>
                    <div class="row"><span>02</span><div><b>🇳🇴 Erling Haaland</b><small>Manchester City · Norway</small></div><strong>91.8</strong><em>↗</em></div>
                    <div class="row"><span>03</span><div><b>🇧🇷 Vinicius Junior</b><small>Real Madrid · Brazil</small></div><strong>90.7</strong><em>↗</em></div>
                    <div class="row"><span>04</span><div><b>🏴󠁧󠁢󠁥󠁮󠁧󠁿 Jude Bellingham</b><small>Real Madrid · England</small></div><strong>89.9</strong><em>↗</em></div>
                    <div class="row"><span>05</span><div><b>🇧🇪 Kevin De Bruyne</b><small>Manchester City · Belgium</small></div><strong>89.5</strong><em>↗</em></div>
                </div>

                <div class="panel">
                    <div class="panelhead">
                        <div>
                            <small>GOLDEN BOOT</small>
                            <h3>TOP <em>SCORERS</em></h3>
                        </div>
                        <em>TOP 5</em>
                    </div>
                    <div class="scorer"><span>01</span><div><b>🇳🇴 Erling Haaland</b><small>Manchester City · Norway</small></div><strong>24<small>GOALS</small></strong></div>
                    <div class="scorer"><span>02</span><div><b>🇫🇷 Kylian Mbappé</b><small>Real Madrid · France</small></div><strong>21<small>GOALS</small></strong></div>
                    <div class="scorer"><span>03</span><div><b>🇪🇬 Mohamed Salah</b><small>Liverpool · Egypt</small></div><strong>19<small>GOALS</small></strong></div>
                    <div class="scorer"><span>04</span><div><b>🏴󠁧󠁢󠁥󠁮󠁧󠁿 Harry Kane</b><small>Bayern München · England</small></div><strong>18<small>GOALS</small></strong></div>
                    <div class="scorer"><span>05</span><div><b>🇧🇷 Vinicius Junior</b><small>Real Madrid · Brazil</small></div><strong>16<small>GOALS</small></strong></div>
                </div>
            </div>

            <!-- PROMINENT BUTTON LINKING TO DEDICATED RANKING.HTML PAGE -->
            <div class="section-cta-wrap">
                <a href="ranking.html" class="btn-section-cta">
                    <span>VIEW ALL PLAYER RANKINGS &amp; LEADERBOARDS</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </a>
            </div>
        </section>

        <!-- ══════════════ SECTION 04: AI PREDICTION ══════════════ -->
        <section class="ml-dedicated-section" id="ml-intelligence">
            <div style="max-width: var(--max); margin: 0 auto; padding: 0 20px;">
                <div class="heading">
                    <div>
                        <h2>04 / AI PREDICTION</h2>
                    </div>
                </div>

                <div class="ml-cards-grid" id="indexMlSampleGrid"></div>

                <!-- WORKBENCH PREVIEW -->
                <div class="ml-workbench-box" id="mlWorkbench">
                    <!-- Left: Evaluation Summary -->
                    <div>
                        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
                            <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--accent-cyan);box-shadow:0 0 10px var(--accent-cyan)"></span>
                            <small style="color:var(--accent-cyan);font-family:'Space Grotesk',monospace;font-weight:800;letter-spacing:1.5px;">PLAYER UNDER AI EVALUATION</small>
                        </div>

                        <div style="display:flex;align-items:center;gap:14px;margin-bottom:16px;">
                            <div class="shirt-avatar-index" id="wbShirt" style="width:54px;height:54px;font-size:22px;margin:0;border-color:var(--accent-cyan);color:var(--accent-cyan);">7</div>
                            <div>
                                <h3 id="wbName" style="font-family:'Cinzel',serif;font-size:22px;color:#fff;margin:0 0 4px 0;">VINICIUS JUNIOR</h3>
                                <div style="font-size:12px;color:#94a3b8;" id="wbSub">Real Madrid C. F. · BRA · Forward</div>
                            </div>
                        </div>

                        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;background:#06080b;padding:14px;border-radius:14px;border:1px solid rgba(56,189,248,0.25);margin-bottom:0;">
                            <div style="text-align:center;">
                                <small style="font-size:9px;color:#64748b;display:block;font-weight:700;">ACTUAL RATING</small>
                                <b style="font-size:22px;color:var(--accent-gold);font-family:'Space Mono',monospace;" id="wbActual">79.1</b>
                                <span style="font-size:9px;color:#64748b;display:block;">Actual Match Score</span>
                            </div>
                            <div style="text-align:center;border-left:1px solid rgba(255,255,255,0.08);border-right:1px solid rgba(255,255,255,0.08);">
                                <small style="font-size:9px;color:var(--accent-cyan);display:block;font-weight:700;">AI PREDICTED</small>
                                <b style="font-size:22px;color:var(--accent-cyan);font-family:'Space Mono',monospace;" id="wbPred">78.8</b>
                                <span style="font-size:9px;color:var(--accent-cyan);display:block;">XGBoost / RF</span>
                            </div>
                            <div style="text-align:center;">
                                <small style="font-size:9px;color:#22c55e;display:block;font-weight:700;">DELTA Δ</small>
                                <b style="font-size:22px;color:#22c55e;font-family:'Space Mono',monospace;" id="wbDelta">+0.3</b>
                                <span style="font-size:9px;color:#22c55e;display:block;">Model Error Margin</span>
                            </div>
                        </div>
                    </div>

                    <!-- Right: VU-Meter & What-If -->
                    <div style="background:rgba(6,8,11,0.95);border:1px solid rgba(56,189,248,0.25);border-radius:18px;padding:22px;box-shadow:0 14px 36px rgba(0,0,0,0.8);">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,0.08);">
                            <div id="wbGaugesTitle" style="font-family:'Space Grotesk',monospace;font-size:12px;font-weight:800;color:#fff;">🤖 5 POSITION METRICS TELEMETRY</div>
                            <span style="background:rgba(34,197,94,0.15);color:#22c55e;padding:3px 8px;border-radius:4px;font-size:10px;font-weight:700;font-family:'Space Grotesk',monospace;">LIVE PREVIEW</span>
                        </div>

                        <!-- 5 LED VU METERS -->
                        <div id="indexVuContainer"></div>

                        <!-- WHAT-IF SIMULATOR -->
                        <div style="background:#090e18;border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:16px;margin-top:16px;">
                            <div style="font-size:11px;color:#94a3b8;font-family:'Space Grotesk',monospace;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center;">
                                <span>SAMPLE WHAT-IF SIMULATOR:</span>
                                <b style="color:var(--accent-cyan);" id="indexSimResult">Base AI: 78.8</b>
                            </div>
                            <div id="simChipsContainer" style="display:flex;gap:8px;flex-wrap:wrap;"></div>
                        </div>
                    </div>
                </div>

                <!-- PROMINENT BUTTON LINKING TO DEDICATED ML-INTELLIGENCE.HTML PAGE -->
                <div class="section-cta-wrap">
                    <a href="ml-intelligence.html" class="btn-section-cta ml-cta">
                        <span>LAUNCH FULL ML INTELLIGENCE &amp; SIMULATOR PORTAL</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>
        </section>

        <!-- ══════════════ SECTION 05: NEWS ══════════════ -->
        <section class="section" id="news">
            <div class="heading">
                <div>
                    <h2>05 / NEWS</h2>
                </div>
            </div>
            <div class="news-list-container">
                <!-- Article 1: Nico Williams -->
                <article class="news-row-card">
                    <div class="news-thumb-wrap">
                        <img src="assets/images/news_williams.jpg" alt="Williams' winding road to world glory" class="news-thumb-img">
                    </div>
                    <div class="news-content-wrap">
                        <span class="news-tag">Spain</span>
                        <h3 class="news-headline">Williams' winding road to world glory</h3>
                        <p class="news-summary">From local grassroots beginnings to football immortality on the global stage, Nico Williams' electric speed, technical flair, and pivotal goals powered Spain through a historic championship run.</p>
                        <div class="news-link-row">
                            <a href="https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/nico-williams-spain-road-to-glory" target="_blank" rel="noopener noreferrer" class="news-direct-link">
                                <span>Xem bài báo gốc trên FIFA.com</span>
                                <i class="fa-solid fa-arrow-up-right-from-square"></i>
                            </a>
                        </div>
                    </div>
                </article>

                <!-- Article 2: Unai Simon -->
                <article class="news-row-card">
                    <div class="news-thumb-wrap">
                        <img src="assets/images/news_simon.jpg" alt="Tears turn to cheers for world champion Simon" class="news-thumb-img">
                    </div>
                    <div class="news-content-wrap">
                        <span class="news-tag">Spain</span>
                        <h3 class="news-headline">Tears turn to cheers for world champion Simon</h3>
                        <p class="news-summary">Spain goalkeeper Unai Simón claimed the adidas Golden Glove after recording seven clean sheets and conceding just one goal in an impassioned masterclass between the posts across North America.</p>
                        <div class="news-link-row">
                            <a href="https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/unai-simon-spain-world-cup-glory" target="_blank" rel="noopener noreferrer" class="news-direct-link">
                                <span>Xem bài báo gốc trên FIFA.com</span>
                                <i class="fa-solid fa-arrow-up-right-from-square"></i>
                            </a>
                        </div>
                    </div>
                </article>

                <!-- Article 3: World Cup Awards -->
                <article class="news-row-card">
                    <div class="news-thumb-wrap">
                        <img src="assets/images/news_awards.jpg" alt="FIFA World Cup awards: Rodri, Cubarsi, Simon and Mbappe honoured" class="news-thumb-img">
                    </div>
                    <div class="news-content-wrap">
                        <span class="news-tag">Featured</span>
                        <h3 class="news-headline">FIFA World Cup awards: Rodri, Cubarsi, Simon and Mbappe honoured</h3>
                        <p class="news-summary">Tournament individual honours officially awarded: Rodri collects the adidas Golden Ball, Kylian Mbappé secures Golden Boot, Unai Simón wins Golden Glove, and Pau Cubarsí earns Best Young Player.</p>
                        <div class="news-link-row">
                            <a href="https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/award-winners" target="_blank" rel="noopener noreferrer" class="news-direct-link">
                                <span>Xem bài báo gốc trên FIFA.com</span>
                                <i class="fa-solid fa-arrow-up-right-from-square"></i>
                            </a>
                        </div>
                    </div>
                </article>

                <!-- Article 4: Spain 2030 -->
                <article class="news-row-card">
                    <div class="news-thumb-wrap">
                        <img src="assets/images/news_yamal.jpg" alt="Spain have ingredients for more history in 2030" class="news-thumb-img">
                    </div>
                    <div class="news-content-wrap">
                        <span class="news-tag">Spain</span>
                        <h3 class="news-headline">Spain have ingredients for more history in 2030</h3>
                        <p class="news-summary">Spearheaded by Lamine Yamal and a dazzling young generation, reigning champions Spain already set their sights on a historic title defense on home soil at FIFA World Cup 2030.</p>
                        <div class="news-link-row">
                            <a href="https://www.fifa.com/en/tournaments/mens/worldcup/2030/articles/spain-have-ingredients-for-more-history-in-2030" target="_blank" rel="noopener noreferrer" class="news-direct-link">
                                <span>Xem bài báo gốc trên FIFA.com</span>
                                <i class="fa-solid fa-arrow-up-right-from-square"></i>
                            </a>
                        </div>
                    </div>
                </article>
            </div>
        </section>
    </main>

    <!-- ══════════════ FOOTER ══════════════ -->
    <footer>
        <div class="footerbrand"><b>FM</b><span>FOOTBALL<small>ANALYTICS</small></span></div>
        <p>FIFA World Cup 2026 — Football Data Analytics &amp; Machine Learning Portal.</p>
        <a href="#home">↑ Back to Top</a>
        <hr><small>© 2026 Football Analytics · Multi-Page Tournament Intelligence Portal</small>
    </footer>

    <!-- ══════════════ GLOBAL SEARCH OVERLAY ══════════════ -->
    <div class="overlay" id="overlay">
        <button id="close">×</button>
        <div>
            <small>GLOBAL SEARCH</small>
            <h2>SEARCH <em>PLAYERS &amp; TEAMS</em></h2>
            <input placeholder="Enter player name, national team, club..." onkeyup="if(event.key==='Enter'){window.location.href='players.html';}">
        </div>
    </div>

    <!-- ══════════════ MODAL: BASIC PLAYER PROFILE ══════════════ -->
    <div class="player-modal-overlay" id="playerModal" onclick="if(event.target===this)closePlayerModal()">
        <div class="pm-box">
            <div class="pm-hdr">
                <div style="display:flex;align-items:center;gap:10px;">
                    <span style="width:10px;height:10px;border-radius:50%;background:var(--accent-gold);box-shadow:0 0 10px var(--accent-gold)"></span>
                    <span style="font-size:12px;font-weight:800;letter-spacing:1.5px;color:#fff;">PLAYER BASIC PROFILE</span>
                </div>
                <button class="pm-close-btn" onclick="closePlayerModal()">×</button>
            </div>

            <div class="pm-body">
                <!-- COL 1 -->
                <div style="display:flex;flex-direction:column;gap:14px;">
                    <div class="pm-card" style="text-align:center;">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                            <span class="flag-tag-index" id="pmFlag">BRA</span>
                            <span class="badge-pos-index FW" id="pmPosBadge">FW</span>
                        </div>
                        <div class="shirt-avatar-index" id="pmShirt" style="width:68px;height:68px;font-size:26px;margin:12px auto;">7</div>
                        <div style="font-size:18px;font-weight:800;color:#fff;margin-bottom:4px;" id="pmName">VINICIUS JUNIOR</div>
                        <div style="font-size:12px;color:#94a3b8;margin-bottom:12px;" id="pmClub">Real Madrid C. F.</div>
                        <span style="display:inline-block;padding:5px 14px;background:rgba(34,197,94,.12);border:1px solid rgba(34,197,94,.25);color:#22c55e;border-radius:20px;font-size:11px;font-weight:700;" id="pmTeam">● NATIONAL TEAM: BRA</span>
                    </div>

                    <div class="pm-card" style="font-size:12px;color:#94a3b8;line-height:1.6;">
                        <b style="color:#fff;display:block;margin-bottom:4px;">FIFA World Cup 2026 Verified Roster</b>
                        Official biometric &amp; tournament participation records from the master tournament roster.
                    </div>
                </div>

                <!-- COL 2 -->
                <div style="display:flex;flex-direction:column;gap:14px;">
                    <div class="pm-card">
                        <div style="font-size:11px;font-weight:800;color:var(--accent-gold);margin-bottom:14px;letter-spacing:1px;text-transform:uppercase;">
                            📋 4 CORE BASIC METRICS
                        </div>
                        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
                            <div style="background:#06080b;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,.08);">
                                <small style="color:#64748b;display:block;font-size:10px;font-weight:700;margin-bottom:4px;">⚽ PLAYING POSITION</small>
                                <b id="pmPosDetail" style="color:var(--accent-gold);font-family:'Space Grotesk',monospace;font-size:15px;">Forward (FW)</b>
                            </div>
                            <div style="background:#06080b;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,.08);">
                                <small style="color:#64748b;display:block;font-size:10px;font-weight:700;margin-bottom:4px;">🌐 NATIONAL TEAM</small>
                                <b id="pmNationalTeam" style="color:var(--accent-cyan);font-family:'Space Grotesk',monospace;font-size:15px;">Brazil (BRA)</b>
                            </div>
                            <div style="background:#06080b;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,.08);">
                                <small style="color:#64748b;display:block;font-size:10px;font-weight:700;margin-bottom:4px;">📏 HEIGHT</small>
                                <b id="pmHeight" style="color:#fff;font-family:'Space Grotesk',monospace;font-size:15px;">176 cm</b>
                            </div>
                            <div style="background:#06080b;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,.08);">
                                <small style="color:#64748b;display:block;font-size:10px;font-weight:700;margin-bottom:4px;">⚖️ WEIGHT</small>
                                <b id="pmWeight" style="color:#fff;font-family:'Space Grotesk',monospace;font-size:15px;">71 kg</b>
                            </div>
                        </div>
                    </div>

                    <div class="pm-card">
                        <div style="font-size:11px;font-weight:800;color:#94a3b8;margin-bottom:12px;letter-spacing:1px;text-transform:uppercase;">
                            📊 ADDITIONAL BIOMETRIC &amp; MATCH RECORDS
                        </div>
                        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
                            <div style="background:#06080b;padding:10px 12px;border-radius:8px;border:1px solid rgba(255,255,255,.06);font-size:12px;">
                                <small style="color:#64748b;display:block;margin-bottom:2px;">Age</small>
                                <b id="pmAge" style="color:#fff;font-family:'Space Grotesk',monospace;">25 yrs</b>
                            </div>
                            <div style="background:#06080b;padding:10px 12px;border-radius:8px;border:1px solid rgba(255,255,255,.06);font-size:12px;">
                                <small style="color:#64748b;display:block;margin-bottom:2px;">Shirt Number</small>
                                <b id="pmShirtNum" style="color:#fff;font-family:'Space Grotesk',monospace;">#7</b>
                            </div>
                            <div style="background:#06080b;padding:10px 12px;border-radius:8px;border:1px solid rgba(255,255,255,.06);font-size:12px;">
                                <small style="color:#64748b;display:block;margin-bottom:2px;">Matches Played</small>
                                <b id="pmMatches" style="color:#fff;font-family:'Space Grotesk',monospace;">5 matches</b>
                            </div>
                            <div style="background:#06080b;padding:10px 12px;border-radius:8px;border:1px solid rgba(255,255,255,.06);font-size:12px;">
                                <small style="color:#64748b;display:block;margin-bottom:2px;">Minutes Played</small>
                                <b id="pmMinutes" style="color:#fff;font-family:'Space Grotesk',monospace;">440 mins</b>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ══════════════ SCRIPTS ══════════════ -->
    <script src="assets/js/timed-cards.js?v=20261014_wchistory2"></script>
    <script src="assets/js/expanding-panels.js?v=20261014_v2"></script>
    <script src="assets/js/app.js"></script>

    <script>
    let samplePlayers = [];
    let activePlayer = null;
    let activeMlPlayer = null;
    let simMins = 0, simGoals = 0, simAssists = 0;

    function computePlayerWeight(p) {
        if (p.weight) return p.weight;
        const h = p.height || 180;
        return Math.round(((h / 100) ** 2) * 22.8);
    }

    function getPosDetailLabel(pos) {
        const map = {
            'FW': 'Forward (FW)',
            'MF': 'Midfielder (MF)',
            'DF': 'Defender (DF)',
            'GK': 'Goalkeeper (GK)'
        };
        return map[pos] || pos || 'Player';
    }

    fetch('assets/js/players_full_data.json?v=20261014')
        .then(res => res.json())
        .then(data => {
            // Pick 5 prominent sample star players for Section 02
            const starNames = ['Vinicius', 'Bellingham', 'Mbapp', 'Messi', 'Haaland'];
            samplePlayers = starNames.map(n => data.find(p => p.name.toLowerCase().includes(n.toLowerCase()))).filter(Boolean);
            if (samplePlayers.length < 5) {
                samplePlayers = data.slice(0, 5);
            }
            renderSamplePlayerCards(samplePlayers);

            // Pick 4 sample players for Section 04 ML preview
            const mlSamples = samplePlayers.slice(0, 4);
            renderSampleMlCards(mlSamples);
            selectPlayerForMlWorkbench(samplePlayers[0]);
        })
        .catch(() => {
            // Fallback sample players (Highlight 5 players with authentic shirt numbers)
            samplePlayers = [
                { id: 137, name: "VINICIUS JUNIOR", team: "BRA", club: "Real Madrid C. F.", pos: "FW", pos_detail: "FW", age: 25, height: 176, minutes: 440, matches: 5, rating: 79.1, predicted_rating: 78.8, delta: 0.3, goals_p90: 0.82, assists_p90: 0.2, shots_p90: 3.47, shirt: 7, flag_code: "BR" },
                { id: 354, name: "Jude Bellingham", team: "ENG", club: "Real Madrid C. F.", pos: "MF", pos_detail: "MF", age: 22, height: 186, minutes: 450, matches: 5, rating: 79.5, predicted_rating: 79.8, delta: 0.3, goals_p90: 0.4, assists_p90: 0.2, shots_p90: 2.0, shirt: 10, flag_code: "ENG" },
                { id: 376, name: "Kylian Mbappé", team: "FRA", club: "Real Madrid C. F.", pos: "FW", pos_detail: "FW", age: 26, height: 178, minutes: 450, matches: 5, rating: 82.2, predicted_rating: 82.0, delta: 0.2, goals_p90: 1.0, assists_p90: 0.2, shots_p90: 4.0, shirt: 10, flag_code: "FR" },
                { id: 30, name: "Lionel Messi", team: "ARG", club: "Inter Miami CF", pos: "FW", pos_detail: "FW", age: 38, height: 170, minutes: 180, matches: 2, rating: 73.5, predicted_rating: 73.3, delta: 0.2, goals_p90: 0.0, assists_p90: 0.0, shots_p90: 1.5, shirt: 10, flag_code: "AR" },
                { id: 590, name: "Erling Haaland", team: "NOR", club: "Manchester City", pos: "FW", pos_detail: "FW", age: 25, height: 194, minutes: 360, matches: 4, rating: 80.5, predicted_rating: 80.8, delta: 0.3, goals_p90: 1.25, assists_p90: 0.0, shots_p90: 3.75, shirt: 9, flag_code: "NO" }
            ];
            renderSamplePlayerCards(samplePlayers);
            renderSampleMlCards(samplePlayers.slice(0, 4));
            selectPlayerForMlWorkbench(samplePlayers[0]);
        });

    function renderSamplePlayerCards(list) {
        const grid = document.getElementById('indexPlayersGrid');
        grid.innerHTML = list.map(p => {
            const weight = computePlayerWeight(p);
            return `
            <div class="player-card-index" onclick="openPlayerModal(${p.id})">
                <div class="card-top-index">
                    <span class="flag-tag-index">🌐 ${p.team || p.flag_code || 'WC'}</span>
                    <span class="badge-pos-index ${p.pos}">${p.pos}</span>
                </div>
                <div class="shirt-avatar-index">${p.shirt || ''}</div>
                <div class="player-name-index">${p.name}</div>
                <div class="player-sub-index">${p.club || 'National Team'} · ${p.age || 25} yrs</div>
                
                <div class="card-basic-grid">
                    <div class="basic-spec-item">
                        <span class="lbl"><i class="fa-solid fa-futbol"></i> POSITION</span>
                        <b class="val pos-val">${p.pos_detail || p.pos}</b>
                    </div>
                    <div class="basic-spec-item">
                        <span class="lbl"><i class="fa-solid fa-flag"></i> TEAM</span>
                        <b class="val team-val">${p.team || 'N/A'}</b>
                    </div>
                    <div class="basic-spec-item">
                        <span class="lbl"><i class="fa-solid fa-ruler-vertical"></i> HEIGHT</span>
                        <b class="val">${p.height || 180} cm</b>
                    </div>
                    <div class="basic-spec-item">
                        <span class="lbl"><i class="fa-solid fa-weight-scale"></i> WEIGHT</span>
                        <b class="val">${weight} kg</b>
                    </div>
                </div>

                <div class="btn-profile-index">INSPECT PROFILE ↗</div>
            </div>`;
        }).join('');
    }

    function renderSampleMlCards(list) {
        const grid = document.getElementById('indexMlSampleGrid');
        grid.innerHTML = list.map(p => {
            const actual = (p.rating || 75).toFixed(1);
            const pred = (p.predicted_rating || p.rating || 75).toFixed(1);
            const diff = ((p.predicted_rating || p.rating) - p.rating);
            const deltaStr = (diff >= 0 ? '+' : '') + diff.toFixed(1);

            return `
            <div class="ml-player-card" onclick="selectPlayerForMlWorkbenchById(${p.id})">
                <div class="card-top-index">
                    <span class="flag-tag-index">🌐 ${p.team || p.flag_code || 'WC'}</span>
                    <span class="badge-pos-index ${p.pos}">${p.pos}</span>
                </div>
                <div class="player-name-index" style="text-align:left;font-size:15px;margin-bottom:2px;">${p.name}</div>
                <div class="player-sub-index" style="text-align:left;margin-bottom:6px;">${p.club || 'National Team'}</div>

                <div class="ml-scores-row">
                    <div class="ml-score-col actual">
                        <small>ACTUAL</small>
                        <b>${actual}</b>
                    </div>
                    <div class="ml-score-col pred">
                        <small>AI PREDICTED</small>
                        <b>${pred}</b>
                    </div>
                    <div class="ml-score-col delta">
                        <small>DELTA Δ</small>
                        <b>${deltaStr}</b>
                    </div>
                </div>

                <div class="btn-ml-inspect">⚡ TEST IN WORKBENCH</div>
            </div>`;
        }).join('');
    }

    function selectPlayerForMlWorkbenchById(id) {
        const p = samplePlayers.find(item => item.id === id);
        if (p) selectPlayerForMlWorkbench(p);
    }

    function renderSimChips(pos) {
        const container = document.getElementById('simChipsContainer');
        if (!container) return;
        if (pos === 'FW') {
            container.innerHTML = `
                <button class="sim-chip" onclick="applyIndexSim(30, 0, 0, this, 0)">+30 Mins</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 1, 0, this, 0)">+1 Goal</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 1, this, 0)">+1 Assist</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 0, this, 2)">+2 Pressing</button>
                <button class="sim-chip" onclick="resetIndexSim(this)" style="background:rgba(248,113,113,0.15);color:#f87171;border-color:rgba(248,113,113,0.3)">Reset</button>
            `;
        } else if (pos === 'MF') {
            container.innerHTML = `
                <button class="sim-chip" onclick="applyIndexSim(30, 0, 0, this, 0)">+30 Mins</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 1, this, 0)">+1 Key Assist</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 1, 0, this, 0)">+1 Goal</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 0, this, 2)">+2 Recoveries</button>
                <button class="sim-chip" onclick="resetIndexSim(this)" style="background:rgba(248,113,113,0.15);color:#f87171;border-color:rgba(248,113,113,0.3)">Reset</button>
            `;
        } else if (pos === 'DF') {
            container.innerHTML = `
                <button class="sim-chip" onclick="applyIndexSim(30, 0, 0, this, 0)">+30 Mins</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 0, this, 2)">+2 Tackles Won</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 0, this, 3)">+3 Interceptions</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 1, this, 0)">+1 Long Pass</button>
                <button class="sim-chip" onclick="resetIndexSim(this)" style="background:rgba(248,113,113,0.15);color:#f87171;border-color:rgba(248,113,113,0.3)">Reset</button>
            `;
        } else { // GK
            container.innerHTML = `
                <button class="sim-chip" onclick="applyIndexSim(30, 0, 0, this, 0)">+30 Mins</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 0, this, 3)">+3 Crucial Saves</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 0, this, 2)">+2 High Claims</button>
                <button class="sim-chip" onclick="applyIndexSim(0, 0, 1, this, 0)">+1 Clean Catch</button>
                <button class="sim-chip" onclick="resetIndexSim(this)" style="background:rgba(248,113,113,0.15);color:#f87171;border-color:rgba(248,113,113,0.3)">Reset</button>
            `;
        }
    }

    function selectPlayerForMlWorkbench(p) {
        if (!p) return;
        activeMlPlayer = p;
        simMins = 0; simGoals = 0; simAssists = 0; simTackles = 0;

        document.getElementById('wbShirt').textContent = p.shirt || (p.pos === 'GK' ? '1' : (p.pos === 'DF' ? '4' : '10'));
        document.getElementById('wbName').textContent = p.name;
        document.getElementById('wbSub').textContent = `${p.club || 'National Team'} · ${p.team} · ${getPosDetailLabel(p.pos)}`;

        const actual = (p.rating || 75).toFixed(1);
        const pred = (p.predicted_rating || p.rating || 75).toFixed(1);
        const diff = ((p.predicted_rating || p.rating) - p.rating);
        const deltaStr = (diff >= 0 ? '+' : '') + diff.toFixed(1);

        document.getElementById('wbActual').textContent = actual;
        document.getElementById('wbPred').textContent = pred;
        document.getElementById('wbDelta').textContent = deltaStr;

        renderSimChips(p.pos);
        updateMlWorkbenchTelemetry();
    }

    function getPosition5Metrics(p, sim) {
        const r = p.rating || 75;
        const pos = p.pos || 'FW';

        if (pos === 'FW') {
            const finishing = Math.min(99, Math.max(65, Math.round(62 + (p.goals_p90 || 0.3) * 24 + (p.shot_acc || 45) * 0.2)));
            const pace = Math.min(99, Math.max(70, Math.round(76 + (p.shots_p90 || 1.5) * 3.8 + (r - 70) * 0.7)));
            const dribbling = Math.min(99, Math.max(68, Math.round(72 + (r - 70) * 1.3)));
            const linkup = Math.min(99, Math.max(60, Math.round(66 + (p.assists_p90 || 0.1) * 32 + (r - 70) * 0.7)));
            const pressing = Math.min(95, Math.max(45, Math.round(50 + (p.tackles_p90 || 0.3) * 25 + (r - 70) * 0.5)));

            return [
                { label: 'FINISHING & CONVERSION', icon: '⚽', val: finishing, boost: (sim.goals || 0) * 4.0 },
                { label: 'ATTACKING PACE & SPRINT', icon: '⚡', val: pace, boost: (sim.mins || 0) * 0.02 },
                { label: 'DRIBBLING & 1v1 TAKE-ONS', icon: '💫', val: dribbling, boost: (sim.goals || 0) * 1.5 + (sim.assists || 0) * 1.5 },
                { label: 'KEY PASSES & LINK-UP', icon: '🎯', val: linkup, boost: (sim.assists || 0) * 3.5 },
                { label: 'PRESSING & WORK RATE', icon: '⚔', val: pressing, boost: (sim.tackles || 0) * 3.0 }
            ];
        } else if (pos === 'MF') {
            const vision = Math.min(99, Math.max(72, Math.round(76 + (p.assists_p90 || 0.25) * 30 + (r - 70) * 0.9)));
            const control = Math.min(99, Math.max(68, Math.round(74 + (r - 70) * 1.2)));
            const creation = Math.min(99, Math.max(65, Math.round(70 + (p.assists_p90 || 0.2) * 28 + (p.shots_p90 || 1.0) * 3)));
            const recovery = Math.min(99, Math.max(60, Math.round(65 + (p.interceptions_p90 || 0.8) * 14 + (p.tackles_p90 || 0.8) * 12)));
            const stamina = Math.min(99, Math.max(70, Math.round(75 + (r - 70) * 0.8 + Math.min(10, (p.minutes || 300) / 90 * 1.5))));

            return [
                { label: 'VISION & PASS ACCURACY', icon: '🎯', val: vision, boost: (sim.assists || 0) * 3.5 },
                { label: 'BALL CONTROL & RETENTION', icon: '💫', val: control, boost: (sim.assists || 0) * 1.5 + (sim.goals || 0) * 1.5 },
                { label: 'CHANCE CREATION & PASSES', icon: '⚡', val: creation, boost: (sim.assists || 0) * 3.0 + (sim.goals || 0) * 1.5 },
                { label: 'RECOVERIES & INTERCEPTIONS', icon: '🛡', val: recovery, boost: (sim.tackles || 0) * 3.0 },
                { label: 'STAMINA & TRANSITIONS', icon: '🏃', val: stamina, boost: (sim.mins || 0) * 0.03 }
            ];
        } else if (pos === 'DF') {
            const tackling = Math.min(99, Math.max(72, Math.round(74 + (p.tackles_p90 || 1.2) * 14 + (r - 70) * 0.7)));
            const intercep = Math.min(99, Math.max(70, Math.round(73 + (p.interceptions_p90 || 1.2) * 14 + (r - 70) * 0.7)));
            const aerial = Math.min(99, Math.max(65, Math.round(68 + Math.max(0, (p.height || 180) - 175) * 1.2 + (r - 70) * 0.6)));
            const clearances = Math.min(99, Math.max(70, Math.round(75 + (p.tackles_p90 || 1.0) * 8 + (r - 70) * 0.8)));
            const buildUp = Math.min(95, Math.max(55, Math.round(64 + (p.assists_p90 || 0) * 35 + (r - 70) * 0.8)));

            return [
                { label: 'TACKLING & GROUND 1v1', icon: '🛡', val: tackling, boost: (sim.tackles || 0) * 3.5 },
                { label: 'INTERCEPTIONS & READING', icon: '🧠', val: intercep, boost: (sim.tackles || 0) * 2.5 },
                { label: 'AERIAL DUELS & PHYSICALITY', icon: '🦘', val: aerial, boost: (sim.tackles || 0) * 2.0 },
                { label: 'CLEARANCES & SHOT BLOCKS', icon: '🧱', val: clearances, boost: (sim.tackles || 0) * 3.0 },
                { label: 'BALL PROGRESSION & PASS', icon: '🎯', val: buildUp, boost: (sim.mins || 0) * 0.02 + (sim.assists || 0) * 3.0 }
            ];
        } else { // GK
            const reflexes = Math.min(99, Math.max(70, Math.round(68 + (p.save_pct || 70) * 0.28 + (r - 70) * 0.6)));
            const diving = Math.min(99, Math.max(70, Math.round(70 + Math.max(0, (p.height || 188) - 180) * 1.3 + (r - 70) * 0.6)));
            const positioning = Math.min(99, Math.max(70, Math.round(72 + (p.clean_sheets || 0) * 4 + (r - 70) * 0.8)));
            const handling = Math.min(99, Math.max(68, Math.round(70 + (p.save_pct || 70) * 0.22 + Math.max(0, 3 - (p.ga90 || 1.0)) * 4)));
            const distribution = Math.min(96, Math.max(60, Math.round(65 + (r - 70) * 0.9)));

            return [
                { label: 'REFLEXES & SHOT STOPPING', icon: '🧤', val: reflexes, boost: (sim.tackles || 0) * 3.0 },
                { label: 'DIVING & AERIAL REACH', icon: '🦅', val: diving, boost: (sim.mins || 0) * 0.02 },
                { label: 'POSITIONING & BOX COMMAND', icon: '🎯', val: positioning, boost: (sim.mins || 0) * 0.025 },
                { label: 'HANDLING & CLEAN CATCHES', icon: '🤲', val: handling, boost: (sim.tackles || 0) * 2.0 },
                { label: 'DISTRIBUTION & LONG BALL', icon: '🚀', val: distribution, boost: (sim.assists || 0) * 3.0 + (sim.mins || 0) * 0.02 }
            ];
        }
    }

    function applyIndexSim(m, g, a, btn, t = 0) {
        simMins += m;
        simGoals += g;
        simAssists += a;
        simTackles += t;
        updateMlWorkbenchTelemetry();
    }

    function resetIndexSim(btn) {
        simMins = 0;
        simGoals = 0;
        simAssists = 0;
        simTackles = 0;
        updateMlWorkbenchTelemetry();
    }

    function updateMlWorkbenchTelemetry() {
        if (!activeMlPlayer) return;
        const p = activeMlPlayer;
        const sim = { mins: simMins, goals: simGoals, assists: simAssists, tackles: simTackles };
        const metrics = getPosition5Metrics(p, sim);

        const titleElem = document.getElementById('wbGaugesTitle');
        if (titleElem) {
            titleElem.textContent = `🤖 5 POSITION METRICS: ${getPosDetailLabel(p.pos).toUpperCase()}`;
        }

        const vuHtml = metrics.map(m => {
            const finalVal = Math.min(99.0, Math.max(30.0, m.val + (m.boost || 0))).toFixed(1);
            return `
            <div class="v-bar-item">
                <div class="v-bar-header"><span>${m.label} ${m.icon}</span><span>${finalVal}</span></div>
                <div class="v-bar-track"><div class="v-bar-fill" style="width:${finalVal}%"></div></div>
            </div>`;
        }).join('');
        document.getElementById('indexVuContainer').innerHTML = vuHtml;

        const basePred = activeMlPlayer.predicted_rating || activeMlPlayer.rating || 75;
        let boost = 0;
        if (p.pos === 'FW') {
            boost = (simMins * 0.015) + (simGoals * 0.5) + (simAssists * 0.3) + (simTackles * 0.15);
        } else if (p.pos === 'MF') {
            boost = (simMins * 0.015) + (simAssists * 0.45) + (simGoals * 0.35) + (simTackles * 0.25);
        } else if (p.pos === 'DF') {
            boost = (simMins * 0.015) + (simTackles * 0.4) + (simAssists * 0.25) + (simGoals * 0.2);
        } else { // GK
            boost = (simMins * 0.015) + (simTackles * 0.45) + (simAssists * 0.2);
        }
        const simTotal = Math.min(99.0, basePred + boost).toFixed(1);

        if (boost > 0) {
            document.getElementById('indexSimResult').innerHTML = `Base AI: ${basePred.toFixed(1)} ➔ <span style="color:var(--accent-gold);margin-left:4px;">Simulated: ${simTotal} ⚡ (+${boost.toFixed(1)})</span>`;
        } else {
            document.getElementById('indexSimResult').innerHTML = `Base AI: ${basePred.toFixed(1)}`;
        }
    }

    function openPlayerModal(id) {
        const p = samplePlayers.find(item => item.id === id);
        if (!p) return;
        const weight = computePlayerWeight(p);

        document.getElementById('pmFlag').textContent = p.team || p.flag_code || 'WC';
        document.getElementById('pmPosBadge').textContent = p.pos;
        document.getElementById('pmPosBadge').className = 'badge-pos-index ' + p.pos;
        document.getElementById('pmShirt').textContent = p.shirt || '';
        document.getElementById('pmName').textContent = p.name;
        document.getElementById('pmClub').textContent = p.club || 'National Team';
        document.getElementById('pmTeam').textContent = '● NATIONAL TEAM: ' + (p.team || 'WC 2026');
        
        document.getElementById('pmPosDetail').textContent = getPosDetailLabel(p.pos_detail || p.pos);
        document.getElementById('pmNationalTeam').textContent = `${p.team || 'N/A'} (FIFA: ${p.flag_code || p.team || 'WC'})`;
        document.getElementById('pmHeight').textContent = (p.height || 180) + ' cm';
        document.getElementById('pmWeight').textContent = weight + ' kg';

        document.getElementById('pmAge').textContent = (p.age || 25) + ' yrs';
        document.getElementById('pmShirtNum').textContent = p.shirt ? '#' + p.shirt : 'N/A';
        document.getElementById('pmMatches').textContent = (p.matches || 4) + ' matches';
        document.getElementById('pmMinutes').textContent = (p.minutes || 360) + ' mins';

        document.getElementById('playerModal').classList.add('show');
        document.body.style.overflow = 'hidden';
    }

    function closePlayerModal() {
        document.getElementById('playerModal').classList.remove('show');
        document.body.style.overflow = '';
    }
    </script>
</body>
</html>
'''
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
