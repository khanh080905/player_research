/**
 * FIFA World Cup 2026 - Player Analytics & Machine Learning UI
 * Real Player Database & Audio Volume Level Bar Logic
 */

const PLAYERS_DATABASE = [
  {
    "id": 163,
    "name": "VINICIUS JUNIOR",
    "team": "BRA",
    "club": "Real Madrid C. F.",
    "pos": "FW",
    "pos_detail": "FW",
    "age": 25,
    "height": 176.0,
    "minutes": 440,
    "matches": 5,
    "rating": 79.1,
    "goals_p90": 0.82,
    "assists_p90": 0.2,
    "shots_p90": 3.47,
    "shot_acc": 64.7,
    "tackles_p90": 0.2,
    "interceptions_p90": 0.2,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇧🇷",
    "predicted_rating": 78.8,
    "delta": 0.3
  },
  {
    "id": 1178,
    "name": "VALVERDE Federico",
    "team": "URU",
    "club": "Real Madrid C. F.",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 27,
    "height": 182.0,
    "minutes": 236,
    "matches": 3,
    "rating": 71.8,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 3.85,
    "shot_acc": 20.0,
    "tackles_p90": 0.77,
    "interceptions_p90": 1.15,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇺🇾",
    "predicted_rating": 71.5,
    "delta": 0.3
  },
  {
    "id": 160,
    "name": "MARQUINHOS",
    "team": "BRA",
    "club": "Paris Saint-Germain",
    "pos": "DF",
    "pos_detail": "DF",
    "age": 32,
    "height": 183.0,
    "minutes": 450,
    "matches": 5,
    "rating": 73.5,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 0.4,
    "shot_acc": 0.0,
    "tackles_p90": 0.4,
    "interceptions_p90": 0.6,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇧🇷",
    "predicted_rating": 74.2,
    "delta": 0.7
  },
  {
    "id": 157,
    "name": "ALISSON",
    "team": "BRA",
    "club": "Liverpool FC",
    "pos": "GK",
    "pos_detail": "GK",
    "age": 33,
    "height": 193.0,
    "minutes": 450,
    "matches": 5,
    "rating": 82.0,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 0.0,
    "shot_acc": 0.0,
    "tackles_p90": 0.0,
    "interceptions_p90": 0.0,
    "save_pct": 77.8,
    "clean_sheet_pct": 40.0,
    "clean_sheets": 2.0,
    "ga90": 0.8,
    "flag": "🇧🇷",
    "predicted_rating": 82.0,
    "delta": 0.0
  },
  {
    "id": 36,
    "name": "MESSI Lionel",
    "team": "ARG",
    "club": "Inter Miami CF",
    "pos": "FW",
    "pos_detail": "FW",
    "age": 38,
    "height": 170.0,
    "minutes": 740,
    "matches": 8,
    "rating": 80.4,
    "goals_p90": 0.98,
    "assists_p90": 0.49,
    "shots_p90": 4.27,
    "shot_acc": 51.4,
    "tackles_p90": 1.22,
    "interceptions_p90": 0.0,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇦🇷",
    "predicted_rating": 79.9,
    "delta": 0.5
  },
  {
    "id": 478,
    "name": "MBAPPE Kylian",
    "team": "FRA",
    "club": "Real Madrid C. F.",
    "pos": "FW",
    "pos_detail": "FW",
    "age": 27,
    "height": 180.0,
    "minutes": 695,
    "matches": 8,
    "rating": 81.4,
    "goals_p90": 1.3,
    "assists_p90": 0.52,
    "shots_p90": 5.32,
    "shot_acc": 56.1,
    "tackles_p90": 0.13,
    "interceptions_p90": 0.0,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇫🇷",
    "predicted_rating": 81.2,
    "delta": 0.2
  },
  {
    "id": 452,
    "name": "BELLINGHAM Jude",
    "team": "ENG",
    "club": "Real Madrid C. F.",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 22,
    "height": 183.0,
    "minutes": 614,
    "matches": 8,
    "rating": 77.7,
    "goals_p90": 1.03,
    "assists_p90": 0.15,
    "shots_p90": 2.79,
    "shot_acc": 68.4,
    "tackles_p90": 1.47,
    "interceptions_p90": 0.44,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "predicted_rating": 78.0,
    "delta": 0.3
  },
  {
    "id": 33,
    "name": "DE PAUL Rodrigo",
    "team": "ARG",
    "club": "Inter Miami CF",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 32,
    "height": 178.0,
    "minutes": 491,
    "matches": 7,
    "rating": 73.6,
    "goals_p90": 0.0,
    "assists_p90": 0.18,
    "shots_p90": 0.36,
    "shot_acc": 50.0,
    "tackles_p90": 0.73,
    "interceptions_p90": 1.09,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇦🇷",
    "predicted_rating": 74.1,
    "delta": 0.5
  },
  {
    "id": 815,
    "name": "HAALAND Erling",
    "team": "NOR",
    "club": "Manchester City FC",
    "pos": "FW",
    "pos_detail": "FW",
    "age": 25,
    "height": 195.0,
    "minutes": 465,
    "matches": 5,
    "rating": 81.0,
    "goals_p90": 1.35,
    "assists_p90": 0.0,
    "shots_p90": 3.85,
    "shot_acc": 65.0,
    "tackles_p90": 0.0,
    "interceptions_p90": 0.19,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇳🇴",
    "predicted_rating": 81.0,
    "delta": 0.0
  },
  {
    "id": 111,
    "name": "DE BRUYNE Kevin",
    "team": "BEL",
    "club": "SSC Napoli",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 34,
    "height": 181.0,
    "minutes": 382,
    "matches": 5,
    "rating": 71.7,
    "goals_p90": 0.24,
    "assists_p90": 0.0,
    "shots_p90": 4.76,
    "shot_acc": 25.0,
    "tackles_p90": 0.48,
    "interceptions_p90": 0.0,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇧🇪",
    "predicted_rating": 72.5,
    "delta": 0.8
  },
  {
    "id": 451,
    "name": "KANE Harry",
    "team": "ENG",
    "club": "FC Bayern München",
    "pos": "FW",
    "pos_detail": "FW",
    "age": 32,
    "height": 190.0,
    "minutes": 652,
    "matches": 7,
    "rating": 78.3,
    "goals_p90": 0.83,
    "assists_p90": 0.14,
    "shots_p90": 3.19,
    "shot_acc": 52.2,
    "tackles_p90": 0.42,
    "interceptions_p90": 0.14,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "predicted_rating": 78.3,
    "delta": 0.0
  },
  {
    "id": 262,
    "name": "WAN-BISSAKA Aaron",
    "team": "COD",
    "club": "West Ham United FC",
    "pos": "DF",
    "pos_detail": "DF",
    "age": 28,
    "height": 183.0,
    "minutes": 354,
    "matches": 4,
    "rating": 78.0,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 0.0,
    "shot_acc": 0.0,
    "tackles_p90": 1.03,
    "interceptions_p90": 1.79,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🌍",
    "predicted_rating": 78.0,
    "delta": 0.0
  },
  {
    "id": 426,
    "name": "MOHAMED SALAH",
    "team": "EGY",
    "club": "Liverpool FC",
    "pos": "FW",
    "pos_detail": "FW",
    "age": 33,
    "height": 175.0,
    "minutes": 425,
    "matches": 5,
    "rating": 76.0,
    "goals_p90": 0.21,
    "assists_p90": 0.43,
    "shots_p90": 1.91,
    "shot_acc": 44.4,
    "tackles_p90": 0.0,
    "interceptions_p90": 0.43,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🌍",
    "predicted_rating": 76.8,
    "delta": 0.8
  },
  {
    "id": 166,
    "name": "NEYMAR JR",
    "team": "BRA",
    "club": "Santos FC",
    "pos": "FW",
    "pos_detail": "FW",
    "age": 34,
    "height": 175.0,
    "minutes": 39,
    "matches": 2,
    "rating": 73.0,
    "goals_p90": 2.5,
    "assists_p90": 0.0,
    "shots_p90": 7.5,
    "shot_acc": 66.7,
    "tackles_p90": 0.0,
    "interceptions_p90": 0.0,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇧🇷",
    "predicted_rating": 73.5,
    "delta": 0.5
  },
  {
    "id": 167,
    "name": "RAPHINHA",
    "team": "BRA",
    "club": "FC Barcelona",
    "pos": "FW",
    "pos_detail": "FW",
    "age": 29,
    "height": 176.0,
    "minutes": 129,
    "matches": 2,
    "rating": 70.5,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 2.14,
    "shot_acc": 66.7,
    "tackles_p90": 0.0,
    "interceptions_p90": 0.0,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇧🇷",
    "predicted_rating": 71.2,
    "delta": 0.7
  },
  {
    "id": 758,
    "name": "VAN DIJK Virgil",
    "team": "NED",
    "club": "Liverpool FC",
    "pos": "DF",
    "pos_detail": "DF",
    "age": 34,
    "height": 195.0,
    "minutes": 390,
    "matches": 4,
    "rating": 78.3,
    "goals_p90": 0.23,
    "assists_p90": 0.23,
    "shots_p90": 0.47,
    "shot_acc": 100.0,
    "tackles_p90": 0.23,
    "interceptions_p90": 0.7,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇳🇱",
    "predicted_rating": 78.0,
    "delta": 0.3
  },
  {
    "id": 887,
    "name": "RUBEN DIAS",
    "team": "POR",
    "club": "Manchester City FC",
    "pos": "DF",
    "pos_detail": "DF",
    "age": 29,
    "height": 187.0,
    "minutes": 360,
    "matches": 4,
    "rating": 75.0,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 0.0,
    "shot_acc": 0.0,
    "tackles_p90": 0.75,
    "interceptions_p90": 1.25,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇵🇹",
    "predicted_rating": 75.5,
    "delta": 0.5
  },
  {
    "id": 105,
    "name": "COURTOIS Thibaut",
    "team": "BEL",
    "club": "Real Madrid C. F.",
    "pos": "GK",
    "pos_detail": "GK",
    "age": 34,
    "height": 199.0,
    "minutes": 550,
    "matches": 6,
    "rating": 78.1,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 0.0,
    "shot_acc": 0.0,
    "tackles_p90": 0.0,
    "interceptions_p90": 0.0,
    "save_pct": 70.0,
    "clean_sheet_pct": 16.7,
    "clean_sheets": 1.0,
    "ga90": 0.98,
    "flag": "🇧🇪",
    "predicted_rating": 77.3,
    "delta": 0.8
  },
  {
    "id": 32,
    "name": "MARTINEZ Lisandro",
    "team": "ARG",
    "club": "Manchester United FC",
    "pos": "DF",
    "pos_detail": "DF",
    "age": 28,
    "height": 175.0,
    "minutes": 624,
    "matches": 7,
    "rating": 78.7,
    "goals_p90": 0.14,
    "assists_p90": 0.14,
    "shots_p90": 0.58,
    "shot_acc": 50.0,
    "tackles_p90": 1.01,
    "interceptions_p90": 0.87,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇦🇷",
    "predicted_rating": 79.0,
    "delta": 0.3
  },
  {
    "id": 730,
    "name": "HAKIMI Achraf",
    "team": "MAR",
    "club": "Paris Saint-Germain",
    "pos": "DF",
    "pos_detail": "DF",
    "age": 27,
    "height": 180.0,
    "minutes": 570,
    "matches": 6,
    "rating": 83.5,
    "goals_p90": 0.16,
    "assists_p90": 0.32,
    "shots_p90": 2.22,
    "shot_acc": 28.6,
    "tackles_p90": 1.59,
    "interceptions_p90": 0.79,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇲🇦",
    "predicted_rating": 83.2,
    "delta": 0.3
  },
  {
    "id": 227,
    "name": "DAVIES Alphonso",
    "team": "CAN",
    "club": "FC Bayern München",
    "pos": "DF",
    "pos_detail": "DF",
    "age": 25,
    "height": 183.0,
    "minutes": 16,
    "matches": 1,
    "rating": 65.3,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 0.0,
    "shot_acc": 0.0,
    "tackles_p90": 0.0,
    "interceptions_p90": 0.0,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇨🇦",
    "predicted_rating": 65.3,
    "delta": 0.0
  },
  {
    "id": 270,
    "name": "BONGONDA Theo",
    "team": "COD",
    "club": "FC Spartak Moscow",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 30,
    "height": 176.0,
    "minutes": 34,
    "matches": 2,
    "rating": 67.1,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 2.5,
    "shot_acc": 0.0,
    "tackles_p90": 0.0,
    "interceptions_p90": 2.5,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🌍",
    "predicted_rating": 67.3,
    "delta": 0.2
  },
  {
    "id": 504,
    "name": "MUSIALA Jamal",
    "team": "GER",
    "club": "FC Bayern München",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 23,
    "height": 180.0,
    "minutes": 270,
    "matches": 4,
    "rating": 72.8,
    "goals_p90": 0.33,
    "assists_p90": 0.0,
    "shots_p90": 2.0,
    "shot_acc": 16.7,
    "tackles_p90": 1.67,
    "interceptions_p90": 0.33,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇩🇪",
    "predicted_rating": 72.0,
    "delta": 0.8
  },
  {
    "id": 511,
    "name": "WIRTZ Florian",
    "team": "GER",
    "club": "Liverpool FC",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 23,
    "height": 176.0,
    "minutes": 361,
    "matches": 4,
    "rating": 77.8,
    "goals_p90": 0.0,
    "assists_p90": 0.75,
    "shots_p90": 2.5,
    "shot_acc": 10.0,
    "tackles_p90": 1.5,
    "interceptions_p90": 0.5,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇩🇪",
    "predicted_rating": 77.0,
    "delta": 0.8
  },
  {
    "id": 1060,
    "name": "PEDRI",
    "team": "ESP",
    "club": "FC Barcelona",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 23,
    "height": 174.0,
    "minutes": 499,
    "matches": 8,
    "rating": 74.9,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 0.91,
    "shot_acc": 40.0,
    "tackles_p90": 1.45,
    "interceptions_p90": 1.82,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇪🇸",
    "predicted_rating": 74.9,
    "delta": 0.0
  },
  {
    "id": 1049,
    "name": "GAVI",
    "team": "ESP",
    "club": "FC Barcelona",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 21,
    "height": 173.0,
    "minutes": 76,
    "matches": 2,
    "rating": 70.8,
    "goals_p90": 0.0,
    "assists_p90": 0.0,
    "shots_p90": 1.25,
    "shot_acc": 0.0,
    "tackles_p90": 2.5,
    "interceptions_p90": 1.25,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇪🇸",
    "predicted_rating": 71.5,
    "delta": 0.7
  },
  {
    "id": 233,
    "name": "SALIBA Nathan",
    "team": "CAN",
    "club": "RSC Anderlecht",
    "pos": "MF",
    "pos_detail": "MF",
    "age": 22,
    "height": 174.0,
    "minutes": 182,
    "matches": 3,
    "rating": 80.0,
    "goals_p90": 0.5,
    "assists_p90": 1.0,
    "shots_p90": 1.5,
    "shot_acc": 33.3,
    "tackles_p90": 2.0,
    "interceptions_p90": 2.0,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇨🇦",
    "predicted_rating": 79.8,
    "delta": 0.2
  },
  {
    "id": 159,
    "name": "GABRIEL MAGALHAES",
    "team": "BRA",
    "club": "Arsenal FC",
    "pos": "DF",
    "pos_detail": "DF",
    "age": 28,
    "height": 190.0,
    "minutes": 450,
    "matches": 5,
    "rating": 76.5,
    "goals_p90": 0.0,
    "assists_p90": 0.2,
    "shots_p90": 0.2,
    "shot_acc": 0.0,
    "tackles_p90": 0.4,
    "interceptions_p90": 0.8,
    "save_pct": 0.0,
    "clean_sheet_pct": 0.0,
    "clean_sheets": 0.0,
    "ga90": 0.0,
    "flag": "🇧🇷",
    "predicted_rating": 77.0,
    "delta": 0.5
  }
];

let currentFilteredPlayers = [...PLAYERS_DATABASE];
let activePositionFilter = 'ALL';
let activePlayer = PLAYERS_DATABASE[0];

// Compute top 5 metrics by position
function getTop5Metrics(player) {
  const pos = player.pos;
  if (pos === 'FW') {
    return [
      { name: 'Bàn thắng / 90p (Goals p90)', val: player.goals_p90, score: Math.min(99, Math.round(player.goals_p90 * 85 + 25)) },
      { name: 'Độ chính xác dứt điểm (Shot Acc %)', val: player.shot_acc + '%', score: Math.min(99, Math.round(player.shot_acc * 0.9 + 20)) },
      { name: 'Tần suất dứt điểm (Shots p90)', val: player.shots_p90, score: Math.min(99, Math.round(player.shots_p90 * 18 + 20)) },
      { name: 'Đóng góp bàn thắng trực tiếp (G+A)', val: (player.goals_p90 + player.assists_p90).toFixed(2), score: Math.min(99, Math.round((player.goals_p90 + player.assists_p90) * 60 + 25)) },
      { name: 'Kiến tạo đột biến (Assists p90)', val: player.assists_p90, score: Math.min(99, Math.round(player.assists_p90 * 120 + 20)) }
    ];
  } else if (pos === 'MF') {
    return [
      { name: 'Cắt bóng & Đánh chặn (Interceptions p90)', val: player.interceptions_p90, score: Math.min(99, Math.round(player.interceptions_p90 * 60 + 25)) },
      { name: 'Tắc bóng thu hồi (Tackles p90)', val: player.tackles_p90, score: Math.min(99, Math.round(player.tackles_p90 * 65 + 25)) },
      { name: 'Sút xa & Tuyến hai (Shots p90)', val: player.shots_p90, score: Math.min(99, Math.round(player.shots_p90 * 16 + 20)) },
      { name: 'Điều tiết nhịp độ & Phút thi đấu', val: player.minutes + "'", score: Math.min(99, Math.round(player.minutes / 360 * 50 + 40)) },
      { name: 'Chính xác dứt điểm (Shot Acc %)', val: player.shot_acc + '%', score: Math.min(99, Math.round(player.shot_acc * 0.8 + 25)) }
    ];
  } else if (pos === 'DF') {
    return [
      { name: 'Đánh chặn & Phán đoán (Interceptions p90)', val: player.interceptions_p90, score: Math.min(99, Math.round(player.interceptions_p90 * 80 + 35)) },
      { name: 'Tắc bóng thành công (Tackles p90)', val: player.tackles_p90, score: Math.min(99, Math.round(player.tackles_p90 * 85 + 35)) },
      { name: 'Thời lượng thi đấu trụ cột (Minutes)', val: player.minutes + "'", score: Math.min(99, Math.round(player.minutes / 360 * 50 + 45)) },
      { name: 'Kỷ luật thi đấu (Thẻ phạt)', val: 'Chuẩn', score: 85 },
      { name: 'Không chiến & Phát động bóng', val: 'Cao', score: 82 }
    ];
  } else {
    // GK
    return [
      { name: 'Tỷ lệ cản phá thành công (Save %)', val: player.save_pct + '%', score: Math.min(99, Math.round(player.save_pct * 0.9 + 25)) },
      { name: 'Tỷ lệ giữ sạch lưới (Clean Sheet %)', val: player.clean_sheet_pct + '%', score: Math.min(99, Math.round(player.clean_sheet_pct * 1.2 + 40)) },
      { name: 'Chỉ số thủng lưới thấp (Low GA90)', val: player.ga90, score: Math.min(99, Math.max(50, Math.round(95 - player.ga90 * 15))) },
      { name: 'Số trận trắng lưới (Clean Sheets)', val: player.clean_sheets + ' trận', score: Math.min(99, Math.round(player.clean_sheets * 20 + 45)) },
      { name: 'Làm chủ vùng cấm & Cản phá đối mặt', val: 'Xuất sắc', score: 88 }
    ];
  }
}

// Audio Volume Level Bar Renderer
function renderVolumeBar(metric) {
  const score = Math.max(10, Math.min(99, metric.score));
  
  // 1. Exact Textual ASCII format requested by user: |=========================------|
  const totalChars = 28;
  const activeChars = Math.round((score / 100) * totalChars);
  const inactiveChars = totalChars - activeChars;
  const asciiBar = "|" + "=".repeat(activeChars) + "-".repeat(inactiveChars) + "|";

  // 2. Graphic LED Segments
  const totalSegments = 30;
  const activeSegments = Math.round((score / 100) * totalSegments);
  let segmentsHtml = "";
  for (let i = 0; i < totalSegments; i++) {
    let stateClass = "led-off";
    if (i < activeSegments) {
      if (i < 18) stateClass = "led-cyan";
      else if (i < 25) stateClass = "led-gold";
      else stateClass = "led-green";
    }
    segmentsHtml += '<span class="led-segment ' + stateClass + '"></span>';
  }

  return `
    <div class="volume-bar-card">
      <div class="volume-bar-header">
        <span class="metric-name">${metric.name}</span>
        <span class="metric-score">${score}/100</span>
      </div>
      
      <!-- Graphical LED VU Meter -->
      <div class="vu-led-track">
        ${segmentsHtml}
      </div>

      <!-- Exact Textual Volume Level Format Requested by User -->
      <div class="vu-ascii-box">
        <span class="ascii-track">${asciiBar}</span>
        <span class="ascii-score">${score}/100</span>
      </div>
    </div>
  `;
}

// Render Radar Polygon SVG points based on player
function getRadarPoints(player) {
  const pos = player.pos;
  if (pos === 'FW') {
    return "100,30 165,65 155,135 100,165 45,130 38,65";
  } else if (pos === 'MF') {
    return "100,60 155,75 140,125 100,168 55,125 45,75";
  } else if (pos === 'DF') {
    return "100,80 135,85 130,120 100,165 40,135 35,80";
  } else {
    return "100,95 125,95 120,110 100,165 35,145 35,95";
  }
}

// Render Top Feature Impacts (SHAP style)
function renderFeatureImpacts(player) {
  const pos = player.pos;
  let feats = [];
  if (pos === 'FW') {
    feats = [
      { name: 'goals_p90 (' + player.goals_p90 + ')', impact: '+4.12 điểm', w: '85%', cls: 'feat-green' },
      { name: 'shot_acc (' + player.shot_acc + '%)', impact: '+2.85 điểm', w: '68%', cls: 'feat-cyan' },
      { name: 'minutes (' + player.minutes + "\')", impact: '+1.90 điểm', w: '50%', cls: 'feat-gold' }
    ];
  } else if (pos === 'MF') {
    feats = [
      { name: 'interceptions (' + player.interceptions_p90 + ')', impact: '+3.65 điểm', w: '78%', cls: 'feat-cyan' },
      { name: 'tackles (' + player.tackles_p90 + ')', impact: '+2.40 điểm', w: '60%', cls: 'feat-green' },
      { name: 'minutes (' + player.minutes + "\')", impact: '+1.85 điểm', w: '48%', cls: 'feat-gold' }
    ];
  } else if (pos === 'DF') {
    feats = [
      { name: 'interceptions (' + player.interceptions_p90 + ')', impact: '+3.10 điểm', w: '72%', cls: 'feat-cyan' },
      { name: 'clean_sheets (Defense)', impact: '+2.70 điểm', w: '64%', cls: 'feat-green' },
      { name: 'tackles (' + player.tackles_p90 + ')', impact: '+1.95 điểm', w: '52%', cls: 'feat-gold' }
    ];
  } else {
    feats = [
      { name: 'save_pct (' + player.save_pct + '%)', impact: '+5.20 điểm', w: '90%', cls: 'feat-green' },
      { name: 'clean_sheets (' + player.clean_sheets + ')', impact: '+3.80 điểm', w: '75%', cls: 'feat-cyan' },
      { name: 'ga90 (' + player.ga90 + ')', impact: '-1.10 điểm', w: '35%', cls: 'feat-gold' }
    ];
  }

  return feats.map(f => `
    <div class="feat-item">
      <div class="feat-header">
        <span class="feat-label">${f.name}</span>
        <span class="feat-value">${f.impact}</span>
      </div>
      <div class="feat-bar-bg">
        <div class="feat-bar-fill ${f.cls}" style="width: ${f.w}"></div>
      </div>
    </div>
  `).join('');
}

// Open Modal with detailed player data
function openPlayerModal(playerId) {
  const player = PLAYERS_DATABASE.find(p => p.id === playerId) || PLAYERS_DATABASE[0];
  activePlayer = player;

  // Cột 1: Thông tin
  document.getElementById('modal-name').textContent = player.name;
  document.getElementById('modal-flag').textContent = player.flag;
  document.getElementById('modal-team').textContent = player.team;
  document.getElementById('modal-club').textContent = player.club;
  document.getElementById('modal-pos-badge').textContent = player.pos + ' • ' + player.pos_detail;
  document.getElementById('modal-shirt-num').textContent = (player.id % 23) + 1;
  document.getElementById('modal-age').textContent = player.age + ' tuổi';
  document.getElementById('modal-height').textContent = player.height + ' cm';
  document.getElementById('modal-minutes').textContent = player.minutes + ' phút';
  document.getElementById('modal-matches').textContent = player.matches + ' trận';

  // Cột 2: 5 Chỉ số cao nhất dạng Thanh âm lượng + Radar
  const topMetrics = getTop5Metrics(player);
  document.getElementById('volume-bars-list').innerHTML = topMetrics.map(renderVolumeBar).join('');
  document.getElementById('radar-poly').setAttribute('points', getRadarPoints(player));

  // Cột 3: Machine Learning Prediction
  document.getElementById('modal-actual-rating').textContent = player.rating.toFixed(1);
  document.getElementById('modal-predicted-rating').textContent = player.predictedRating.toFixed(1);
  document.getElementById('modal-delta-error').textContent = '± ' + player.delta.toFixed(2) + ' điểm';
  document.getElementById('modal-shap-features').innerHTML = renderFeatureImpacts(player);
  
  // What-If reset
  document.getElementById('sim-slider').value = 0;
  document.getElementById('sim-slider-val').textContent = '+0 phút';
  document.getElementById('sim-result-score').textContent = player.predictedRating.toFixed(1);

  // Show Modal
  const modal = document.getElementById('player-detail-modal');
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closePlayerModal() {
  const modal = document.getElementById('player-detail-modal');
  modal.classList.remove('active');
  document.body.style.overflow = '';
}

// What-If Simulator
function onSimulateChange(extraMins) {
  document.getElementById('sim-slider-val').textContent = `+${extraMins} phút`;
  const base = activePlayer.predictedRating;
  const boost = (parseInt(extraMins) / 180) * 1.8;
  const newRating = Math.min(99.0, (base + boost)).toFixed(1);
  document.getElementById('sim-result-score').textContent = newRating;
}

// Render Player Card Grid
function renderPlayerCards(players) {
  const grid = document.getElementById('players-grid');
  if (!grid) return;

  if (players.length === 0) {
    grid.innerHTML = '<div class="no-results">Không tìm thấy cầu thủ phù hợp với bộ lọc.</div>';
    return;
  }

  grid.innerHTML = players.map(p => `
    <div class="player-card" onclick="openPlayerModal(${p.id})">
      <div class="card-top">
        <span class="card-flag">${p.flag}</span>
        <span class="card-pos pos-${p.pos.toLowerCase()}">${p.pos}</span>
        <div class="card-rating-badge">
          <span class="badge-val">${p.rating.toFixed(1)}</span>
          <span class="badge-lbl">RATING</span>
        </div>
      </div>

      <div class="card-avatar">
        <div class="avatar-num">${(p.id % 23) + 1}</div>
      </div>

      <div class="card-body">
        <h3 class="player-title">${p.name}</h3>
        <p class="player-team-info">${p.team} &bull; ${p.club}</p>
        <div class="card-stats-mini">
          <div><small>Phút</small><b>${p.minutes}'</b></div>
          <div><small>Trận</small><b>${p.matches}</b></div>
          <div><small>AI Dự đoán</small><b class="text-cyan">${p.predictedRating.toFixed(1)}</b></div>
        </div>
      </div>

      <div class="card-footer">
        <button class="btn-view-profile">XEM HỒ SƠ & ML 🎚️</button>
      </div>
    </div>
  `).join('');
}

// Filtering
function applyFilters() {
  const searchInput = document.getElementById('search-input');
  const query = searchInput ? searchInput.value.toLowerCase().trim() : '';

  currentFilteredPlayers = PLAYERS_DATABASE.filter(p => {
    const matchPos = activePositionFilter === 'ALL' || p.pos === activePositionFilter;
    const matchQuery = !query || 
      p.name.toLowerCase().includes(query) || 
      p.club.toLowerCase().includes(query) || 
      p.team.toLowerCase().includes(query);
    return matchPos && matchQuery;
  });

  renderPlayerCards(currentFilteredPlayers);
  
  const countEl = document.getElementById('result-count');
  if (countEl) {
    countEl.textContent = `Hiển thị ${currentFilteredPlayers.length} / ${PLAYERS_DATABASE.length} cầu thủ`;
  }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  renderPlayerCards(PLAYERS_DATABASE);

  // Search input
  const searchInput = document.getElementById('search-input');
  if (searchInput) {
    searchInput.addEventListener('input', applyFilters);
  }

  // Filter Buttons
  const filterBtns = document.querySelectorAll('.filter-pill-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activePositionFilter = btn.dataset.pos;
      applyFilters();
    });
  });

  // Close modal on escape or background
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closePlayerModal();
  });

  const modal = document.getElementById('player-detail-modal');
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closePlayerModal();
    });
  }
});
