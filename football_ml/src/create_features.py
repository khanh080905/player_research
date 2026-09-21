import pandas as pd
import numpy as np

print()
print("==============================================")
print("TAO FEATURE PER 90")
print("==============================================")

# ==============================================
# DOC DATASET
# ==============================================

df = pd.read_csv("data/players_ml.csv")

print()
print("So cau thu :", len(df))


# ==============================================
# HAM TINH PER 90
# ==============================================

def per90(value, minutes):

    if pd.isna(value) or pd.isna(minutes):
        return np.nan

    if minutes <= 0:
        return np.nan

    return value / minutes * 90


# ==============================================
# CAC FEATURE PER 90
# ==============================================

df["goals_p90_calc"] = df.apply(
    lambda row: per90(
        row["goals"],
        row["minutes"]
    ),
    axis=1
)

df["assists_p90"] = df.apply(
    lambda row: per90(
        row["assists"],
        row["minutes"]
    ),
    axis=1
)

df["tackles_won_p90"] = df.apply(
    lambda row: per90(
        row["tackles_won"],
        row["minutes"]
    ),
    axis=1
)

df["interceptions_p90"] = df.apply(
    lambda row: per90(
        row["interceptions"],
        row["minutes"]
    ),
    axis=1
)

df["saves_p90"] = df.apply(
    lambda row: per90(
        row["saves"],
        row["minutes"]
    ),
    axis=1
)

df["clean_sheets_p90"] = df.apply(
    lambda row: per90(
        row["clean_sheets"],
        row["minutes"]
    ),
    axis=1
)


# ==============================================
# KIEM TRA
# ==============================================

print()
print("----------------------------------------------")
print("CAC FEATURE MOI")
print("----------------------------------------------")

new_features = [
    "goals_p90_calc",
    "assists_p90",
    "tackles_won_p90",
    "interceptions_p90",
    "saves_p90",
    "clean_sheets_p90"
]

for col in new_features:

    count = df[col].notna().sum()

    print(
        f"{col:30} {count}/{len(df)}"
    )


# ==============================================
# DOI TEN GOALS P90
# ==============================================

df.rename(
    columns={
        "goals_p90_calc": "goals_p90"
    },
    inplace=True
)


# ==============================================
# LUU FILE
# ==============================================

output = "data/players_features.csv"

df.to_csv(
    output,
    index=False,
    encoding="utf-8-sig"
)


print()
print("----------------------------------------------")
print("KET QUA")
print("----------------------------------------------")

print("So cau thu :", len(df))
print("So cot     :", len(df.columns))

print()
print("Da tao:")
print(output)

print()
print("==============================================")
print("HOAN THANH")
print("==============================================")