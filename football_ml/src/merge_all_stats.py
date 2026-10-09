import pandas as pd

print()
print("==============================================")
print("MERGE CAC BO DU LIEU FBREF")
print("==============================================")

# ==============================================
# DOC DU LIEU
# ==============================================

matched = pd.read_csv("data/players_fbref.csv")
standard = pd.read_csv("data/player_standard_clean.csv")
shooting = pd.read_csv("data/player_shooting_clean.csv")
defense = pd.read_csv("data/player_defense_clean.csv")
keeper = pd.read_csv("data/player_keeper_clean.csv")

print()
print("Players FBref :", len(matched))
print("Standard      :", len(standard))
print("Shooting      :", len(shooting))
print("Defense       :", len(defense))
print("Keeper        :", len(keeper))


# ==============================================
# 1. STANDARD
# ==============================================

result = matched.merge(
    standard,
    left_on="fbref_name",
    right_on="player_name",
    how="left",
    suffixes=("", "_standard")
)

print()
print("Sau khi merge Standard :", len(result))


# ==============================================
# 2. SHOOTING
# ==============================================

shooting_cols = [
    "player_name",
    "shots",
    "shots_on_target",
    "shot_on_target_pct",
    "shots_p90",
    "shots_on_target_p90",
    "goals_per_shot",
    "goals_per_sot"
]

shooting_use = shooting[shooting_cols].copy()

result = result.merge(
    shooting_use,
    left_on="fbref_name",
    right_on="player_name",
    how="left"
)

result.rename(
    columns={
        "player_name": "player_name_shooting"
    },
    inplace=True
)

print("Sau khi merge Shooting :", len(result))


# ==============================================
# 3. DEFENSE
# ==============================================

defense_cols = [
    "player_name",
    "tackles_won",
    "interceptions"
]

defense_use = defense[defense_cols].copy()

result = result.merge(
    defense_use,
    left_on="fbref_name",
    right_on="player_name",
    how="left"
)

result.rename(
    columns={
        "player_name": "player_name_defense"
    },
    inplace=True
)

print("Sau khi merge Defense  :", len(result))


# ==============================================
# 4. KEEPER
# ==============================================

keeper_cols = [
    "player_name",
    "goals_against",
    "ga90",
    "shots_on_target_against",
    "saves",
    "save_pct",
    "clean_sheets",
    "clean_sheet_pct",
    "pk_attempted",
    "pk_allowed",
    "pk_saved",
    "pk_missed",
    "pk_save_pct"
]

keeper_use = keeper[keeper_cols].copy()

result = result.merge(
    keeper_use,
    left_on="fbref_name",
    right_on="player_name",
    how="left"
)

result.rename(
    columns={
        "player_name": "player_name_keeper"
    },
    inplace=True
)

print("Sau khi merge Keeper   :", len(result))


# ==============================================
# XOA CAC COT TEN TRUNG
# ==============================================

drop_cols = [
    "player_name_standard",
    "player_name_shooting",
    "player_name_defense",
    "player_name_keeper"
]

for col in drop_cols:

    if col in result.columns:
        result.drop(columns=[col], inplace=True)


# ==============================================
# LUU FILE
# ==============================================

output = "data/players_ml_raw.csv"

result.to_csv(
    output,
    index=False,
    encoding="utf-8-sig"
)


# ==============================================
# THONG KE
# ==============================================

print()
print("----------------------------------------------")
print("KET QUA")
print("----------------------------------------------")

print("So cau thu :", len(result))
print("So cot     :", len(result.columns))

print()
print("Da tao:")
print(output)

print()
print("==============================================")
print("HOAN THANH")
print("==============================================")