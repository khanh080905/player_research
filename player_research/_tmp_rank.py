import csv
from collections import defaultdict
from pathlib import Path

p = Path(r"D:\xampp\htdocs\player_research\vinh\player_research_1\football_ml\data")
master = p / "players_master_dataset.csv"
keeper = p / "player_keeper_clean.csv"
passing = p / "player_passing_clean.csv"
defense = p / "player_defense_clean.csv"

with master.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print("master n", len(rows))
print("cols", list(rows[0].keys()))

teams = defaultdict(lambda: dict(
    max_m=0, goals=0, assists=0, ga=0, saves=0, tackles=0,
    mins=0, n=0, nplay=0, rat_sum=0, rat_play=0, gk_wins=0, gk_draws=0, gk_loss=0
))
for r in rows:
    t = r["national_team"]
    d = teams[t]
    d["n"] += 1
    m = float(r["matches"] or 0)
    if m > d["max_m"]:
        d["max_m"] = m
    d["goals"] += float(r["goals"] or 0)
    d["assists"] += float(r["assists"] or 0)
    d["ga"] += float(r["goals_against"] or 0)
    d["saves"] += float(r["saves"] or 0)
    d["tackles"] += float(r["tackles_won"] or 0)
    mins = float(r["minutes"] or 0)
    d["mins"] += mins
    rat = float(r["overall_rating"] or 0)
    d["rat_sum"] += rat
    if mins > 0:
        d["nplay"] += 1
        d["rat_play"] += rat

print("\nTEAM maxM G A GA rat")
for t, d in sorted(teams.items(), key=lambda x: (-x[1]["max_m"], -x[1]["goals"], x[1]["ga"] - x[1]["goals"])):
    rp = d["rat_play"] / (d["nplay"] or 1)
    print(f"{t:22} maxM={d['max_m']:.0f} G={d['goals']:.0f} A={d['assists']:.0f} GA={d['ga']:.0f} GD={d['goals']-d['ga']:.0f} play={d['nplay']} rat={rp:.1f}")

print("\nTOP GOALS")
for r in sorted(rows, key=lambda r: (-float(r["goals"] or 0), -float(r["assists"] or 0)))[:25]:
    print(r["player_name"], r["national_team"], r["position"], "G", r["goals"], "A", r["assists"], "min", r["minutes"], "m", r["matches"], "rat", r["overall_rating"], "tw", r["tackles_won"])

print("\nTOP TACKLES")
for r in sorted(rows, key=lambda r: -float(r["tackles_won"] or 0))[:20]:
    print(r["player_name"], r["national_team"], r["position"], r["tackles_won"], "min", r["minutes"], "m", r["matches"])

print("\nTOP SAVES")
gks = [r for r in rows if r.get("position_group") == "GK"]
for r in sorted(gks, key=lambda r: -float(r["saves"] or 0))[:20]:
    print(r["player_name"], r["national_team"], "saves", r["saves"], "pct", r["save_pct"], "ga", r["goals_against"], "min", r["minutes"], "m", r["matches"])

print("\nTOP SAVE PCT min>=180")
for r in sorted([r for r in gks if float(r["minutes"] or 0) >= 180], key=lambda r: -float(r["save_pct"] or 0))[:15]:
    print(r["player_name"], r["national_team"], "pct", r["save_pct"], "saves", r["saves"], "min", r["minutes"])

print("\nTOP RATING minutes>0")
played = [r for r in rows if float(r["minutes"] or 0) > 0]
for r in sorted(played, key=lambda r: -float(r["overall_rating"] or 0))[:25]:
    print(r["player_name"], r["national_team"], r["position"], r["overall_rating"], "G", r["goals"], "A", r["assists"], "min", r["minutes"], "m", r["matches"])

with keeper.open(encoding="utf-8") as f:
    krows = list(csv.DictReader(f))
print("\nKEEPER cols", list(krows[0].keys()))
print("sample", krows[0])
print("\nGK W-D-L")
for r in sorted(krows, key=lambda r: -float(r.get("wins") or 0))[:30]:
    print(r["player_name"], r["national_team"], "W", r.get("wins"), "D", r.get("draws"), "L", r.get("losses"), "m", r.get("matches"), "saves", r.get("saves"))

with passing.open(encoding="utf-8") as f:
    prows = list(csv.DictReader(f))
print("\nPASSING nonempty counts")
keys = list(prows[0].keys())
for k in keys:
    n = sum(1 for r in prows if (r.get(k) or "").strip() not in ("", "Matches"))
    print(k, n)

with defense.open(encoding="utf-8") as f:
    drows = list(csv.DictReader(f))
print("\nDEFENSE nonempty")
for k in drows[0].keys():
    n = sum(1 for r in drows if (r.get(k) or "").strip() not in ("", "Matches"))
    print(k, n)

# max matches players per team
print("\nPlayers with max matches per high teams")
by = defaultdict(list)
for r in played:
    by[r["national_team"]].append(r)
for t in sorted(by, key=lambda t: -max(float(x["matches"] or 0) for x in by[t]))[:12]:
    mx = max(float(x["matches"] or 0) for x in by[t])
    print(t, "max", mx, "n", sum(1 for x in by[t] if float(x["matches"] or 0) == mx))
