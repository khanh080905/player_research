import pandas as pd

print()
print("==============================================")
print("KIEM TRA DU LIEU ML")
print("==============================================")

df = pd.read_csv("data/players_ml_raw.csv")

print()
print("So cau thu :", len(df))
print("So cot     :", len(df.columns))

print()
print("----------------------------------------------")
print("CHI TIET CAC COT")
print("----------------------------------------------")

for col in df.columns:

    total = len(df)
    non_empty = df[col].notna().sum()
    empty = total - non_empty
    percent = non_empty / total * 100

    print(
        f"{col:35} "
        f"{non_empty:4}/{total} "
        f"({percent:6.2f}%)"
    )


print()
print("----------------------------------------------")
print("CAC COT CO DU LIEU DUOI 10%")
print("----------------------------------------------")

for col in df.columns:

    percent = df[col].notna().sum() / len(df) * 100

    if percent < 10:

        print(
            f"{col:35} "
            f"{percent:6.2f}%"
        )


print()
print("----------------------------------------------")
print("CAC COT CO DU LIEU TREN 90%")
print("----------------------------------------------")

for col in df.columns:

    percent = df[col].notna().sum() / len(df) * 100

    if percent >= 90:

        print(
            f"{col:35} "
            f"{percent:6.2f}%"
        )


print()
print("==============================================")
print("HOAN THANH")
print("==============================================")