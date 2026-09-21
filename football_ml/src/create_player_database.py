import pandas as pd

print()
print("==============================================")
print("TAO DATABASE CAU THU")
print("==============================================")

# ==============================================
# DOC DU LIEU
# ==============================================

players_raw = pd.read_csv(
    "data/players_raw.csv"
)

players_matched = pd.read_csv(
    "data/players_matched.csv"
)

print()
print("So cau thu raw     :", len(players_raw))
print("So cau thu matched :", len(players_matched))


# ==============================================
# 1. TAO DATABASE 1248 CAU THU
# ==============================================

players_database = players_raw.copy()

players_database["fbref_matched"] = 0


# ==============================================
# XAC DINH CAU THU DA MATCH FBREF
# ==============================================

matched_ids = set(
    players_matched["player_id"].astype(str)
)

players_database.loc[
    players_database["player_id"].astype(str).isin(matched_ids),
    "fbref_matched"
] = 1


# ==============================================
# LUU DATABASE
# ==============================================

players_database.to_csv(
    "data/players_database.csv",
    index=False,
    encoding="utf-8-sig"
)


# ==============================================
# 2. TAO DATABASE FBREF 888 CAU THU
# ==============================================

players_fbref = players_matched.copy()

players_fbref.to_csv(
    "data/players_fbref.csv",
    index=False,
    encoding="utf-8-sig"
)


# ==============================================
# THONG KE
# ==============================================

total_players = len(players_database)

matched_count = (
    players_database["fbref_matched"] == 1
).sum()

unmatched_count = (
    players_database["fbref_matched"] == 0
).sum()


print()
print("----------------------------------------------")
print("KET QUA")
print("----------------------------------------------")

print("Tong database       :", total_players)
print("Da match FBref      :", matched_count)
print("Chua match FBref    :", unmatched_count)

print()
print("Da tao:")
print("data/players_database.csv")
print("data/players_fbref.csv")

print()
print("==============================================")
print("HOAN THANH")
print("==============================================")