# -*- coding: utf-8 -*-
"""Build ranking-data.js from vinh master CSV + data.js (one-shot generator)."""
import csv
import json
import collections
from pathlib import Path

root = Path(r"D:\xampp\htdocs\player_research")
csv_path = root / r"vinh\player_research_1\football_ml\data\players_master_dataset.csv"
data_js = (root / r"vinh\player_research_1\data.js").read_text(encoding="utf-8")
assert data_js.startswith("const DB=")
players_src = json.loads(data_js[len("const DB=") :].rstrip().rstrip(";"))

with csv_path.open(encoding="utf-8-sig") as f:
    master = list(csv.DictReader(f))
master_by_id = {int(r["player_id"]): r for r in master}

CONF = {
    "ALG": "CAF", "ARG": "CONMEBOL", "AUS": "AFC", "AUT": "UEFA", "BEL": "UEFA",
    "BIH": "UEFA", "BRA": "CONMEBOL", "CAN": "CONCACAF", "CIV": "CAF", "COD": "CAF",
    "COL": "CONMEBOL", "CPV": "CAF", "CRO": "UEFA", "CUW": "CONCACAF", "CZE": "UEFA",
    "ECU": "CONMEBOL", "EGY": "CAF", "ENG": "UEFA", "ESP": "UEFA", "FRA": "UEFA",
    "GER": "UEFA", "GHA": "CAF", "HAI": "CONCACAF", "IRN": "AFC", "IRQ": "AFC",
    "JOR": "AFC", "JPN": "AFC", "KOR": "AFC", "KSA": "AFC", "MAR": "CAF",
    "MEX": "CONCACAF", "NED": "UEFA", "NOR": "UEFA", "NZL": "OFC", "PAN": "CONCACAF",
    "PAR": "CONMEBOL", "POR": "UEFA", "QAT": "AFC", "RSA": "CAF", "SCO": "UEFA",
    "SEN": "CAF", "SUI": "UEFA", "SWE": "UEFA", "TUN": "CAF", "TUR": "UEFA",
    "URU": "CONMEBOL", "USA": "CONCACAF", "UZB": "AFC",
}
VN = {
    "ALG": "Algeria", "ARG": "Argentina", "AUS": "Úc", "AUT": "Áo", "BEL": "Bỉ",
    "BIH": "Bosnia & Herzegovina", "BRA": "Brazil", "CAN": "Canada",
    "CIV": "Bờ Biển Ngà", "COD": "CHDC Congo", "COL": "Colombia",
    "CPV": "Cape Verde", "CRO": "Croatia", "CUW": "Curaçao", "CZE": "Séc",
    "ECU": "Ecuador", "EGY": "Ai Cập", "ENG": "Anh", "ESP": "Tây Ban Nha",
    "FRA": "Pháp", "GER": "Đức", "GHA": "Ghana", "HAI": "Haiti", "IRN": "Iran",
    "IRQ": "Iraq", "JOR": "Jordan", "JPN": "Nhật Bản", "KOR": "Hàn Quốc",
    "KSA": "Ả Rập Xê Út", "MAR": "Maroc", "MEX": "Mexico", "NED": "Hà Lan",
    "NOR": "Na Uy", "NZL": "New Zealand", "PAN": "Panama", "PAR": "Paraguay",
    "POR": "Bồ Đào Nha", "QAT": "Qatar", "RSA": "Nam Phi", "SCO": "Scotland",
    "SEN": "Senegal", "SUI": "Thụy Sĩ", "SWE": "Thụy Điển", "TUN": "Tunisia",
    "TUR": "Thổ Nhĩ Kỳ", "URU": "Uruguay", "USA": "Hoa Kỳ", "UZB": "Uzbekistan",
}

by_team = collections.defaultdict(list)
for r in master:
    by_team[r["national_team"]].append(r)

team_rows = []
for code, plist in by_team.items():
    playing = [p for p in plist if float(p["minutes"]) > 0]
    src = playing or plist
    rating = round(sum(float(p["overall_rating"]) for p in src) / len(src), 1)
    squad_rating = round(sum(float(p["overall_rating"]) for p in plist) / len(plist), 1)
    gf = int(sum(float(p["goals"]) for p in plist))
    gks = [p for p in plist if p["position_group"] == "GK" and float(p["minutes"]) > 0]
    if not gks:
        gks = [p for p in plist if p["position_group"] == "GK"]
    ga = int(round(max((float(p["goals_against"]) for p in gks), default=0)))
    assists = int(sum(float(p["assists"]) for p in plist))
    team_rows.append({
        "code": code,
        "name": VN[code],
        "conf": CONF[code],
        "rating": rating,
        "squad_rating": squad_rating,
        "gf": gf,
        "ga": ga,
        "assists": assists,
    })

for i, t in enumerate(sorted(team_rows, key=lambda x: (-x["squad_rating"], -x["rating"], x["code"])), 1):
    t["fifa"] = i
for i, t in enumerate(sorted(team_rows, key=lambda x: (-x["rating"], -x["gf"], x["code"])), 1):
    t["wc"] = i

for t in team_rows:
    t["stage"] = t["conf"]
    t["group"] = t["conf"]
    t["pts"] = t["gf"] + t["assists"]

teams_out = sorted(team_rows, key=lambda t: t["wc"])

players = []
for p in players_src:
    m = master_by_id.get(p["id"])
    goals = int(float(m["goals"])) if m else int(round(p["goals_p90"] * p["minutes"] / 90.0))
    assists = int(float(m["assists"])) if m else int(round(p["assists_p90"] * p["minutes"] / 90.0))
    rec = {
        "id": p["id"],
        "name": p["name"],
        "team": p["team"],
        "club": p["club"],
        "pos": p["pos"],
        "rating": p["rating"],
        "predicted": p["predicted_rating"],
        "goals": goals,
        "assists": assists,
        "minutes": int(p["minutes"]),
        "matches": int(p["matches"]),
        "age": int(p["age"]),
    }
    if p["pos"] == "GK":
        rec["savePct"] = p["save_pct"]
    players.append(rec)
players.sort(key=lambda x: (-x["rating"], -x["predicted"], x["name"]))

print("TEAMS", len(teams_out), "PLAYERS", len(players))
print("top teams:")
for t in teams_out[:12]:
    print(" ", t["wc"], t["code"], t["rating"], t["squad_rating"], "fifa", t["fifa"], "gf", t["gf"])
print("players:")
for p in players:
    print(" ", p["id"], p["name"], p["team"], p["rating"], "G", p["goals"], "A", p["assists"])

def fmt_team(t):
    return (
        f'    {{ code:"{t["code"]}", name:"{t["name"]}", conf:"{t["conf"]}", '
        f'fifa:{t["fifa"]}, wc:{t["wc"]}, stage:"{t["stage"]}", group:"{t["group"]}", '
        f'pts:{t["pts"]}, gf:{t["gf"]}, ga:{t["ga"]}, rating:{t["rating"]} }}'
    )

def fmt_player(p):
    extra = f', savePct:{p["savePct"]}' if "savePct" in p else ""
    return (
        f'    {{ id:{p["id"]}, name:"{p["name"]}", team:"{p["team"]}", club:"{p["club"]}", '
        f'pos:"{p["pos"]}", rating:{p["rating"]}, predicted:{p["predicted"]}, '
        f'goals:{p["goals"]}, assists:{p["assists"]}, minutes:{p["minutes"]}, '
        f'matches:{p["matches"]}, age:{p["age"]}{extra} }}'
    )

header = '''/**
 * Bảng xếp hạng đội & cầu thủ — đồng bộ với data.js + players_master_dataset.csv (folder vinh)
 * Đội: 48 đội WC 2026 trong master dataset
 *   - rating: trung bình overall_rating các cầu thủ có phút thi đấu (>0)
 *   - wc: thứ tự theo rating đó (1 = cao nhất)
 *   - fifa: thứ tự theo rating trung bình cả đội 26 người
 *   - pts / gf: tổng (bàn + kiến tạo) / tổng bàn của squad trong dataset
 *   - ga: bàn thua của thủ môn chính (nhiều phút nhất)
 *   - stage/group: liên đoàn (không dùng kết quả VCK giả lập)
 * Cầu thủ: đúng id/rating/phút/tuổi/CLB từ data.js; bàn & kiến tạo lấy từ master
 */
window.RANKING_DATA = {
  fifaUpdated: "Theo overall_rating squad (master dataset)",
  wcNote: "48 đội WC 2026 — xếp theo rating cầu thủ trong bộ dữ liệu nghiên cứu",

  teams: [
'''

body_teams = ",\n".join(fmt_team(t) for t in teams_out)
body_players = ",\n".join(fmt_player(p) for p in players)
js = header + body_teams + "\n  ],\n\n  players: [\n" + body_players + "\n  ]\n};\n"

out_paths = [
    root / r"vinh\player_research_1\ranking-data.js",
    root / r"vinh\web_builder\js\ranking-data.js",
    root / r"khanh\ranking-data.js",
]
for out in out_paths:
    out.write_text(js, encoding="utf-8")
    print("wrote", out)
