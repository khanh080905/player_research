import pandas as pd

print()
print("==============================================")
print("KIEM TRA BENCHMARK RATING")
print("==============================================")

df = pd.read_csv(
    "data/players_rated.csv"
)


# ==============================================
# THONG KE THEO VI TRI
# ==============================================

print()
print("----------------------------------------------")
print("THONG KE THEO VI TRI")
print("----------------------------------------------")

stats = df.groupby("position")["rating"].agg(
    [
        "count",
        "mean",
        "min",
        "max"
    ]
)

print(
    stats.round(2)
)


# ==============================================
# TOP 10 MOI VI TRI
# ==============================================

for position in ["FW", "MF", "DF", "GK"]:

    print()
    print("----------------------------------------------")
    print("TOP 10", position)
    print("----------------------------------------------")

    top = (
        df[df["position"] == position]
        [
            [
                "player_name",
                "national_team",
                "club",
                "rating",
                "minutes",
                "goals",
                "assists"
            ]
        ]
        .sort_values(
            "rating",
            ascending=False
        )
        .head(10)
    )

    print(
        top.to_string(
            index=False
        )
    )


# ==============================================
# PHAN BO RATING
# ==============================================

print()
print("----------------------------------------------")
print("PHAN BO RATING")
print("----------------------------------------------")

bins = [
    0,
    20,
    40,
    60,
    80,
    100
]

labels = [
    "0-20",
    "20-40",
    "40-60",
    "60-80",
    "80-100"
]

df["rating_group"] = pd.cut(
    df["rating"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

print(
    df["rating_group"]
    .value_counts()
    .sort_index()
)


# ==============================================
# KIEM TRA RATING CAO
# ==============================================

print()
print("----------------------------------------------")
print("CAU THU RATING >= 80")
print("----------------------------------------------")

high = (
    df[df["rating"] >= 80]
    [
        [
            "player_name",
            "position",
            "national_team",
            "rating",
            "minutes",
            "goals",
            "assists"
        ]
    ]
    .sort_values(
        "rating",
        ascending=False
    )
)

print(
    high.to_string(
        index=False
    )
)


print()
print("==============================================")
print("HOAN THANH")
print("==============================================")