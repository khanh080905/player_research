import pandas as pd
import os

files = [
    "player_standard_clean.csv",
    "player_shooting_clean.csv",
    "player_defense_clean.csv",
    "player_gca_clean.csv",
    "player_keeper_clean.csv"
]

print()
print("==============================================")
print("KIEM TRA CHAT LUONG DU LIEU FBREF")
print("==============================================")

for filename in files:

    path = os.path.join("data", filename)

    df = pd.read_csv(path)

    print()
    print("----------------------------------------------")
    print(filename)
    print("----------------------------------------------")

    print("So dong :", len(df))
    print("So cot  :", len(df.columns))

    for col in df.columns:

        non_empty = df[col].notna().sum()

        print(
            f"{col:35} "
            f"{non_empty:4}/{len(df)}"
        )

print()
print("==============================================")
print("HOAN THANH")
print("==============================================")