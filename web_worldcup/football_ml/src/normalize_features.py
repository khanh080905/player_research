import pandas as pd
import numpy as np

print()
print("==============================================")
print("CHUAN HOA FEATURE THEO VI TRI")
print("==============================================")

# ==============================================
# DOC DATASET
# ==============================================

df = pd.read_csv(
    "data/players_features.csv"
)

print()
print("So cau thu :", len(df))


# ==============================================
# HAM PERCENTILE
# ==============================================

def percentile_score(series):

    result = pd.Series(
        np.nan,
        index=series.index,
        dtype=float
    )

    valid = series.notna()

    if valid.sum() <= 1:
        result.loc[valid] = 50
        return result

    result.loc[valid] = (
        series.loc[valid]
        .rank(method="average", pct=True)
        * 100
    )

    return result


# ==============================================
# FEATURE CHO TUNG VI TRI
# ==============================================

position_features = {

    "FW": [
        "goals_p90",
        "assists_p90",
        "shots_p90",
        "shots_on_target_p90"
    ],

    "MF": [
        "assists_p90",
        "tackles_won_p90",
        "interceptions_p90",
        "shots_p90"
    ],

    "DF": [
        "tackles_won_p90",
        "interceptions_p90"
    ],

    "GK": [
        "save_pct",
        "saves_p90",
        "clean_sheets_p90"
    ]
}


# ==============================================
# TAO CAC COT PERCENTILE
# ==============================================

print()
print("----------------------------------------------")
print("TAO PERCENTILE")
print("----------------------------------------------")

for position, features in position_features.items():

    mask = df["position"] == position

    print()
    print("Vi tri:", position)
    print("So cau thu:", mask.sum())

    for feature in features:

        if feature not in df.columns:
            print(
                "THIEU FEATURE:",
                feature
            )
            continue

        output_col = feature + "_pct"

        df.loc[mask, output_col] = (
            percentile_score(
                df.loc[mask, feature]
            )
        )

        count = df.loc[
            mask,
            output_col
        ].notna().sum()

        print(
            f"{feature:25} "
            f"{count}/{mask.sum()}"
        )


# ==============================================
# LUU FILE
# ==============================================

output = "data/players_normalized.csv"

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