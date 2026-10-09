import pandas as pd

print()
print("==============================================")
print("TAO DATASET ML SACH")
print("==============================================")

# ==============================================
# DOC DU LIEU
# ==============================================

df = pd.read_csv("data/players_ml_raw.csv")

print()
print("So cau thu ban dau :", len(df))


# ==============================================
# CHON CAC COT CAN THIET
# ==============================================

columns = [
    # ID / thong tin cau thu
    "player_id",
    "fbref_name",
    "national_team",
    "club",
    "position",
    "age",
    "height_cm",

    # Match information
    "matches_standard",
    "starts_standard",
    "minutes_standard",
    "90s_standard",

    # Standard
    "goals_standard",
    "assists_standard",
    "goals_assists",
    "goals_minus_pk",
    "penalties",
    "penalties_attempted",
    "yellow_cards_standard",
    "red_cards_standard",

    # Shooting
    "shots_y",
    "shots_on_target_y",
    "shot_on_target_pct",
    "shots_p90",
    "shots_on_target_p90",
    "goals_per_shot",
    "goals_per_sot",

    # Defense
    "tackles_won_y",
    "interceptions_y",

    # Goalkeeper
    "goals_against",
    "ga90",
    "shots_on_target_against",
    "saves_y",
    "save_pct",
    "clean_sheets",
    "clean_sheet_pct",
    "pk_attempted",
    "pk_allowed",
    "pk_saved",
    "pk_missed",
    "pk_save_pct"
]


# ==============================================
# KIEM TRA CAC COT
# ==============================================

missing_columns = []

for col in columns:

    if col not in df.columns:
        missing_columns.append(col)


if len(missing_columns) > 0:

    print()
    print("LOI: Thieu cac cot:")

    for col in missing_columns:
        print("-", col)

    raise SystemExit


# ==============================================
# TAO DATASET
# ==============================================

ml = df[columns].copy()


# ==============================================
# DOI TEN COT CHO DE SU DUNG
# ==============================================

rename_columns = {

    "fbref_name": "player_name",

    "matches_standard": "matches",
    "starts_standard": "starts",
    "minutes_standard": "minutes",
    "90s_standard": "90s",

    "goals_standard": "goals",
    "assists_standard": "assists",

    "yellow_cards_standard": "yellow_cards",
    "red_cards_standard": "red_cards",

    "shots_y": "shots",
    "shots_on_target_y": "shots_on_target",

    "tackles_won_y": "tackles_won",
    "interceptions_y": "interceptions",

    "saves_y": "saves"
}

ml.rename(
    columns=rename_columns,
    inplace=True
)


# ==============================================
# CHUYEN CAC COT SO SANG NUMERIC
# ==============================================

numeric_columns = [
    "age",
    "height_cm",
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
    "red_cards",
    "shots",
    "shots_on_target",
    "shot_on_target_pct",
    "shots_p90",
    "shots_on_target_p90",
    "goals_per_shot",
    "goals_per_sot",
    "tackles_won",
    "interceptions",
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

for col in numeric_columns:

    if col in ml.columns:

        ml[col] = pd.to_numeric(
            ml[col],
            errors="coerce"
        )


# ==============================================
# SAP XEP COT
# ==============================================

first_columns = [
    "player_id",
    "player_name",
    "national_team",
    "club",
    "position",
    "age",
    "height_cm"
]

other_columns = [
    col for col in ml.columns
    if col not in first_columns
]

ml = ml[
    first_columns + other_columns
]


# ==============================================
# LUU FILE
# ==============================================

output = "data/players_ml.csv"

ml.to_csv(
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

print("So cau thu :", len(ml))
print("So cot     :", len(ml.columns))

print()
print("Vi tri:")

print(
    ml["position"].value_counts()
)


print()
print("Da tao:")
print(output)


print()
print("==============================================")
print("HOAN THANH")
print("==============================================")