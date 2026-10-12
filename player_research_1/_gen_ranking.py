# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

ROOT = Path(r"D:\xampp\htdocs\player_research")
MASTER = ROOT / "vinh" / "player_research_1" / "football_ml" / "data" / "players_master_dataset.csv"

# Thứ hạng chung cuộc FIFA WC 2026 (1–48): vòng đi + điểm/Hiệu số trong từng vòng.
# Khớp số trận trong master dataset (8=CK/hạng 3, 6=tứ kết, 5=V16, 4=V32, 3=bảng).
WC = [
    ("ESP", 1, "Vô địch"),
    ("ARG", 2, "Á quân"),
    ("ENG", 3, "Hạng 3"),
    ("FRA", 4, "Hạng 4"),
    ("NOR", 5, "Tứ kết"),
    ("BEL", 6, "Tứ kết"),
    ("MAR", 7, "Tứ kết"),
    ("SUI", 8, "Tứ kết"),
    ("MEX", 9, "Vòng 16"),
    ("COL", 10, "Vòng 16"),
    ("BRA", 11, "Vòng 16"),
    ("USA", 12, "Vòng 16"),
    ("POR", 13, "Vòng 16"),
    ("CAN", 14, "Vòng 16"),
    ("EGY", 15, "Vòng 16"),
    ("PAR", 16, "Vòng 16"),
    ("NED", 17, "Vòng 32"),
    ("GER", 18, "Vòng 32"),
    ("CIV", 19, "Vòng 32"),
    ("CRO", 20, "Vòng 32"),
    ("JPN", 21, "Vòng 32"),
    ("AUS", 22, "Vòng 32"),
    ("COD", 23, "Vòng 32"),
    ("GHA", 24, "Vòng 32"),
    ("ECU", 25, "Vòng 32"),
    ("RSA", 26, "Vòng 32"),
    ("SWE", 27, "Vòng 32"),
    ("AUT", 28, "Vòng 32"),
    ("BIH", 29, "Vòng 32"),
    ("ALG", 30, "Vòng 32"),
    ("SEN", 31, "Vòng 32"),
    ("CPV", 32, "Vòng 32"),
    ("IRN", 33, "Vòng bảng"),
    ("KOR", 34, "Vòng bảng"),
    ("TUR", 35, "Vòng bảng"),
    ("SCO", 36, "Vòng bảng"),
    ("URU", 37, "Vòng bảng"),
    ("KSA", 38, "Vòng bảng"),
    ("CZE", 39, "Vòng bảng"),
    ("NZL", 40, "Vòng bảng"),
    ("QAT", 41, "Vòng bảng"),
    ("CUW", 42, "Vòng bảng"),
    ("PAN", 43, "Vòng bảng"),
    ("JOR", 44, "Vòng bảng"),
    ("HAI", 45, "Vòng bảng"),
    ("UZB", 46, "Vòng bảng"),
    ("TUN", 47, "Vòng bảng"),
    ("IRQ", 48, "Vòng bảng"),
]

META = {
    "FRA": ("Pháp", "UEFA"),
    "ESP": ("Tây Ban Nha", "UEFA"),
    "ARG": ("Argentina", "CONMEBOL"),
    "MAR": ("Maroc", "CAF"),
    "GER": ("Đức", "UEFA"),
    "ENG": ("Anh", "UEFA"),
    "BEL": ("Bỉ", "UEFA"),
    "NOR": ("Na Uy", "UEFA"),
    "CAN": ("Canada", "CONCACAF"),
    "COL": ("Colombia", "CONMEBOL"),
    "BRA": ("Brazil", "CONMEBOL"),
    "CPV": ("Cape Verde", "CAF"),
    "USA": ("Hoa Kỳ", "CONCACAF"),
    "CRO": ("Croatia", "UEFA"),
    "NED": ("Hà Lan", "UEFA"),
    "EGY": ("Ai Cập", "CAF"),
    "CIV": ("Bờ Biển Ngà", "CAF"),
    "MEX": ("Mexico", "CONCACAF"),
    "SUI": ("Thụy Sĩ", "UEFA"),
    "SEN": ("Senegal", "CAF"),
    "AUT": ("Áo", "UEFA"),
    "COD": ("CHDC Congo", "CAF"),
    "PAR": ("Paraguay", "CONMEBOL"),
    "SWE": ("Thụy Điển", "UEFA"),
    "BIH": ("Bosnia & Herzegovina", "UEFA"),
    "KSA": ("Ả Rập Xê Út", "AFC"),
    "RSA": ("Nam Phi", "CAF"),
    "POR": ("Bồ Đào Nha", "UEFA"),
    "ALG": ("Algeria", "CAF"),
    "ECU": ("Ecuador", "CONMEBOL"),
    "JPN": ("Nhật Bản", "AFC"),
    "GHA": ("Ghana", "CAF"),
    "NZL": ("New Zealand", "OFC"),
    "JOR": ("Jordan", "AFC"),
    "AUS": ("Úc", "AFC"),
    "IRN": ("Iran", "AFC"),
    "HAI": ("Haiti", "CONCACAF"),
    "TUR": ("Thổ Nhĩ Kỳ", "UEFA"),
    "UZB": ("Uzbekistan", "AFC"),
    "TUN": ("Tunisia", "CAF"),
    "URU": ("Uruguay", "CONMEBOL"),
    "CZE": ("Séc", "UEFA"),
    "KOR": ("Hàn Quốc", "AFC"),
    "QAT": ("Qatar", "AFC"),
    "CUW": ("Curaçao", "CONCACAF"),
    "SCO": ("Scotland", "UEFA"),
    "PAN": ("Panama", "CONCACAF"),
    "IRQ": ("Iraq", "AFC"),
}

def fnum(x):
    try:
        return float(x or 0)
    except ValueError:
        return 0.0

with MASTER.open(encoding="utf-8-sig") as fh:
    rows = list(csv.DictReader(fh))

agg = {}
for r in rows:
    code = r["national_team"]
    d = agg.setdefault(code, {"gf": 0, "ga": 0, "ga_sum": 0, "rat": 0, "nplay": 0, "max_m": 0, "mins": 0})
    d["gf"] += fnum(r["goals"])
    d["ga_sum"] += fnum(r["goals_against"])
    m = fnum(r["matches"])
    if m > d["max_m"]:
        d["max_m"] = m
    mins = fnum(r["minutes"])
    d["mins"] += mins
    if mins > 0:
        d["nplay"] += 1
        d["rat"] += fnum(r["overall_rating"])
    # GA đội: thủ môn nhiều phút nhất
agg_gk = {}
for r in rows:
    if r.get("position_group") != "GK":
        continue
    code = r["national_team"]
    mins = fnum(r["minutes"])
    prev = agg_gk.get(code)
    if not prev or mins > prev[0]:
        agg_gk[code] = (mins, fnum(r["goals_against"]))

teams = []
for code, wc, stage in WC:
    name, conf = META[code]
    d = agg[code]
    rating = round(d["rat"] / d["nplay"], 1) if d["nplay"] else 0
    ga = int(agg_gk.get(code, (0, 0))[1])
    teams.append({
        "code": code,
        "name": name,
        "conf": conf,
        "wc": wc,
        "stage": stage,
        "group": conf,
        "gf": int(d["gf"]),
        "ga": ga,
        "matches": int(d["max_m"]),
        "rating": rating,
    })

def player_obj(r):
    pos = r.get("position_group") or r.get("position") or ""
    if pos not in ("FW", "MF", "DF", "GK"):
        pos = (r.get("position") or "MF")[:2]
    save_pct = fnum(r.get("save_pct"))
    return {
        "id": int(fnum(r["player_id"])),
        "name": r["player_name"],
        "team": r["national_team"],
        "club": r["club"] or "",
        "pos": pos,
        "rating": round(fnum(r["overall_rating"]), 1),
        "goals": int(fnum(r["goals"])),
        "assists": int(fnum(r["assists"])),
        "minutes": int(fnum(r["minutes"])),
        "matches": int(fnum(r["matches"])),
        "age": int(fnum(r["age"])),
        "tackles": int(fnum(r["tackles_won"])),
        "saves": int(fnum(r["saves"])),
        "savePct": round(save_pct, 1),
        "interceptions": int(fnum(r["interceptions"])),
    }

played = [r for r in rows if fnum(r["minutes"]) > 0]
qualified = [r for r in played if fnum(r["minutes"]) >= 180]

by_rating = sorted(qualified, key=lambda r: -fnum(r["overall_rating"]))[:40]
by_goals = sorted(played, key=lambda r: (-fnum(r["goals"]), -fnum(r["assists"]), -fnum(r["overall_rating"])))[:25]
by_tackles = sorted(played, key=lambda r: -fnum(r["tackles_won"]))[:20]
gks = [r for r in played if (r.get("position_group") or r.get("position")) == "GK" and fnum(r["minutes"]) >= 180]
by_saves = sorted(gks, key=lambda r: -fnum(r["saves"]))[:20]
by_savepct = sorted(gks, key=lambda r: -fnum(r["save_pct"]))[:15]
by_ast = sorted(played, key=lambda r: (-fnum(r["assists"]), -fnum(r["goals"])))[:15]

seen = set()
players = []
for bucket in (by_rating, by_goals, by_tackles, by_saves, by_savepct, by_ast):
    for r in bucket:
        pid = int(fnum(r["player_id"]))
        if pid in seen:
            continue
        seen.add(pid)
        players.append(player_obj(r))

payload = {
    "fifaUpdated": "",
    "wcNote": "Thứ hạng chung cuộc FIFA World Cup 2026 (vô địch → vòng bảng). Chỉ số cầu thủ từ master dataset folder vinh.",
    "teams": teams,
    "players": players,
}

header = """/**
 * Bảng xếp hạng — thứ hạng chung cuộc WC 2026 (thực tế) + chỉ số từ players_master_dataset.csv (vinh)
 * Đội: wc = hạng chung cuộc giải (1 Tây Ban Nha vô địch … 48 Iraq)
 *      stage = vòng kết thúc; gf/ga/rating lấy từ dataset (không invent FIFA ranking)
 * Cầu thủ: rating/bàn/tắc/cản phá từ master. Bỏ tỷ lệ chuyền (cột passing trống 100%).
 */
window.RANKING_DATA = """

js = header + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"
# json uses double quotes — convert to JS object already valid.

outs = [
    ROOT / "vinh" / "web_builder" / "js" / "ranking-data.js",
    ROOT / "vinh" / "player_research_1" / "ranking-data.js",
    ROOT / "khanh" / "ranking-data.js",
]
for o in outs:
    o.write_text(js, encoding="utf-8")
    print("wrote", o, "teams", len(teams), "players", len(players))
print("champion", teams[0])
print("top scorer sample", [p for p in players if p["goals"] >= 7][:4])
