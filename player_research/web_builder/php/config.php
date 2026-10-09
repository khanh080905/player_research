<?php
declare(strict_types=1);

$root = dirname(__DIR__, 2);
define(
    'PLAYERS_CSV',
    $root . DIRECTORY_SEPARATOR . 'player_research_1' . DIRECTORY_SEPARATOR
    . 'football_ml' . DIRECTORY_SEPARATOR . 'data' . DIRECTORY_SEPARATOR
    . 'players_master_dataset.csv'
);

define('SEARCH_LIMIT', 40);
define('SUGGEST_LIMIT', 8);
define('SEARCH_MIN_CHARS', 3);
