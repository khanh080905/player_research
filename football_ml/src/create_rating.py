import pandas as pd
import numpy as np


INPUT_FILE = "data/players_normalized.csv"
OUTPUT_FILE = "data/players_rated.csv"

# --------------------------------------------------
# DOC DIEM DU LIEU
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)


# --------------------------------------------------
# HAM LAY GIA TRI AN TOAN
# --------------------------------------------------

def get_value(row, column):
    value = row[column]

    if pd.isna(value):
        return np.nan

    return float(value)


# --------------------------------------------------
# DIEM POSITION
# --------------------------------------------------

def calculate_position_score(row):
    position = row["position"]

    if position == "FW":
        features = {
            "goals_p90_pct": 0.35,
            "assists_p90_pct": 0.25,
            "shots_p90_pct": 0.20,
            "shots_on_target_p90_pct": 0.20
        }

    elif position == "MF":
        features = {
            "assists_p90_pct": 0.30,
            "tackles_won_p90_pct": 0.25,
            "interceptions_p90_pct": 0.25,
            "shots_p90_pct": 0.20
        }

    elif position == "DF":
        features = {
            "tackles_won_p90_pct": 0.50,
            "interceptions_p90_pct": 0.50
        }

    elif position == "GK":
        features = {
            "save_pct_pct": 0.45,
            "saves_p90_pct": 0.30,
            "clean_sheets_p90_pct": 0.25
        }

    else:
        return 0.0

    # Chi tinh cac feature co du lieu
    available = {}
    for column, weight in features.items():
        value = get_value(row, column)

        if not pd.isna(value):
            available[column] = (value, weight)

    if len(available) == 0:
        return 0.0

    # Chuan hoa lai weight neu co feature bi thieu
    total_weight = sum(weight for value, weight in available.values())

    score = 0.0

    for value, weight in available.values():
        score += value * (weight / total_weight)

    return score


# --------------------------------------------------
# COMMON SCORE
# --------------------------------------------------

def calculate_common_score(row):
    minutes = float(row["minutes"])

    # Reliability dung moc 450 phut
    reliability = min(1.0, np.sqrt(minutes / 450.0))

    # 0 - 100
    return reliability * 100.0


# --------------------------------------------------
# OTHER SCORE
# --------------------------------------------------

def calculate_other_score(row):
    position = row["position"]

    if position == "GK":
        value = get_value(row, "clean_sheet_pct")

        if pd.isna(value):
            return 0.0

        return value

    else:
        value = get_value(row, "shot_on_target_pct")

        if pd.isna(value):
            return 0.0

        return value


# --------------------------------------------------
# TINH DIEM PENALTY
# --------------------------------------------------

def calculate_penalty(row):
    yellow = float(row["yellow_cards"]) if not pd.isna(row["yellow_cards"]) else 0
    red = float(row["red_cards"]) if not pd.isna(row["red_cards"]) else 0

    penalty = yellow * 1.0 + red * 4.0

    return penalty


# --------------------------------------------------
# TINH RATING BAN DAU
# --------------------------------------------------

df["position_score"] = df.apply(calculate_position_score, axis=1)

df["common_score"] = df.apply(calculate_common_score, axis=1)

df["other_score"] = df.apply(calculate_other_score, axis=1)

df["penalty"] = df.apply(calculate_penalty, axis=1)


# --------------------------------------------------
# RAW RATING
# --------------------------------------------------

df["raw_rating"] = (
    df["position_score"] * 0.80
    + df["common_score"] * 0.10
    + df["other_score"] * 0.10
)


# --------------------------------------------------
# RELIABILITY
# --------------------------------------------------

df["reliability"] = df["minutes"].apply(
    lambda x: min(1.0, np.sqrt(float(x) / 450.0))
)


# --------------------------------------------------
# CO DIEM VE TRUNG BINH CUA TUNG VI TRI
# --------------------------------------------------

position_means = df.groupby("position")["raw_rating"].mean().to_dict()


def calculate_reliable_rating(row):
    position = row["position"]

    raw_rating = row["raw_rating"]

    position_mean = position_means[position]

    reliability = row["reliability"]

    rating = (
        position_mean
        + (raw_rating - position_mean) * reliability
    )

    return rating


df["reliable_rating"] = df.apply(
    calculate_reliable_rating,
    axis=1
)


# --------------------------------------------------
# TRU PENALTY
# --------------------------------------------------

df["rating"] = df["reliable_rating"] - df["penalty"]


# --------------------------------------------------
# GIOI HAN 0 - 100
# --------------------------------------------------

df["rating"] = df["rating"].clip(0, 100)


# --------------------------------------------------
# LAM TRON
# --------------------------------------------------

df["rating"] = df["rating"].round(2)

df["position_score"] = df["position_score"].round(2)

df["common_score"] = df["common_score"].round(2)

df["other_score"] = df["other_score"].round(2)

df["raw_rating"] = df["raw_rating"].round(2)

df["reliability"] = df["reliability"].round(4)

df["reliable_rating"] = df["reliable_rating"].round(2)

df["penalty"] = df["penalty"].round(2)


# --------------------------------------------------
# LUU FILE
# --------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")


# --------------------------------------------------
# HIEN THI KET QUA
# --------------------------------------------------

print("==============================================")
print("TAO BENCHMARK RATING")
print("==============================================")

print()
print("So cau thu:", len(df))

print()
print("Thong ke rating:")
print(
    df.groupby("position")["rating"]
    .agg(["count", "mean", "min", "max"])
    .round(2)
)

print()
print("Phan bo rating:")

bins = [0, 20, 40, 60, 80, 100]

groups = pd.cut(
    df["rating"],
    bins=bins,
    include_lowest=True,
    right=False
)

print(groups.value_counts().sort_index())

print()
print("Top 5 moi vi tri:")

for position in ["FW", "MF", "DF", "GK"]:

    print()
    print("----------------------------------------------")
    print("TOP 5", position)
    print("----------------------------------------------")

    cols = [
        "player_name",
        "national_team",
        "club",
        "rating",
        "minutes",
        "reliability"
    ]

    print(
        df[df["position"] == position]
        .sort_values("rating", ascending=False)
        [cols]
        .head(5)
        .to_string(index=False)
    )

print()
print("==============================================")
print("HOAN THANH")
print("==============================================")