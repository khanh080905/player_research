import pandas as pd


# ==========================================
# DOC DU LIEU
# ==========================================

matched = pd.read_csv(
    "data/players_matched.csv"
)

standard = pd.read_csv(
    "data/player_standard_clean.csv"
)


# ==========================================
# DOI TEN DE DE GHep
# ==========================================

standard = standard.rename(
    columns={
        "player_name": "fbref_name"
    }
)


# ==========================================
# CHI LAY CAC COT THONG KE CAN THIET
# ==========================================

standard_columns = [
    "fbref_name",
    "position",
    "national_team",
    "age",
    "club",
    "matches",
    "starts",
    "minutes",
    "90s",
    "goals",
    "assists",
    "goals_assists",
    "goals_minus_pk",
    "penalties",
    "penalties_attempted",
    "yellow_cards",
    "red_cards"
]

standard = standard[
    standard_columns
]


# ==========================================
# DOI TEN CAC COT TRUNG VOI DATASET GOC
# ==========================================

standard = standard.rename(
    columns={
        "position": "std_position",
        "national_team": "std_national_team",
        "age": "std_age",
        "club": "std_club"
    }
)


# ==========================================
# MERGE
# ==========================================

result = matched.merge(
    standard,
    on="fbref_name",
    how="left"
)


# ==========================================
# KIEM TRA
# ==========================================

print()
print("==========================================")
print("MERGE STANDARD")
print("==========================================")

print("Players matched :", len(matched))
print("Players after merge :", len(result))


# Tim cot minutes cua bang Standard
standard_minutes_col = "minutes_y"

has_standard = result[standard_minutes_col].notna().sum()

print(
    "Co du lieu Standard :",
    has_standard
)

print(
    "Khong co du lieu Standard :",
    len(result) - has_standard
)


# ==========================================
# LUU FILE
# ==========================================

output_file = "data/players_stats.csv"

result.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print()
print("Da tao:")
print(output_file)