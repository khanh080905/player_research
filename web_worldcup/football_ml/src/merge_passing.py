import pandas as pd

print()
print("==========================================")
print("MERGE STANDARD + PASSING")
print("==========================================")

# ==========================================
# 1. Doc du lieu
# ==========================================

matched = pd.read_csv("data/players_matched.csv")
standard = pd.read_csv("data/player_standard_clean.csv")
passing = pd.read_csv("data/player_passing_clean.csv")

print("Players matched      :", len(matched))
print("Players Standard     :", len(standard))
print("Players Passing      :", len(passing))


# ==========================================
# 2. Merge Standard
# ==========================================

result = matched.merge(
    standard,
    left_on="fbref_name",
    right_on="player_name",
    how="left",
    suffixes=("", "_standard")
)

standard_count = result["player_name"].notna().sum()

print("Co du lieu Standard  :", standard_count)


# ==========================================
# 3. Merge Passing
# ==========================================

result = result.merge(
    passing,
    left_on="fbref_name",
    right_on="player_name",
    how="left",
    suffixes=("", "_passing")
)

passing_count = result["player_name_passing"].notna().sum()

print("Co du lieu Passing   :", passing_count)
print("Khong co Passing     :", len(result) - passing_count)


# ==========================================
# 4. Xoa cot trung lap
# ==========================================

if "player_name_standard" in result.columns:
    result.drop(columns=["player_name_standard"], inplace=True)

if "player_name_passing" in result.columns:
    result.drop(columns=["player_name_passing"], inplace=True)


# ==========================================
# 5. Luu file
# ==========================================

output = "data/players_stats.csv"

result.to_csv(
    output,
    index=False,
    encoding="utf-8-sig"
)

print()
print("Da tao lai:")
print(output)
print()