import pandas as pd
import unicodedata


raw = pd.read_csv("data/players_raw.csv")
std = pd.read_csv("data/player_standard_clean.csv")


team_map = {
    'ALG':'DZ', 'ARG':'AR', 'AUT':'AT', 'AUS':'AU', 'BIH':'BA',
    'BEL':'BE', 'BRA':'BR', 'CAN':'CA', 'CIV':'CI', 'COL':'CO',
    'CPV':'CV', 'CUW':'CW', 'CZE':'CZ', 'DEU':'DE', 'ECU':'EC',
    'EGY':'EG', 'ENG':'ENG', 'ESP':'ES', 'FRA':'FR', 'GHA':'GH',
    'HRV':'HR', 'HAI':'HT', 'IRQ':'IQ', 'IRN':'IR', 'JPN':'JP',
    'KOR':'KR', 'MAR':'MA', 'MEX':'MX', 'NLD':'NL', 'NOR':'NO',
    'NZL':'NZ', 'PAN':'PA', 'PRT':'PT', 'PRY':'PY', 'QAT':'QA',
    'SAU':'SA', 'SCO':'SCT', 'SWE':'SE', 'SEN':'SN', 'TUN':'TN',
    'TUR':'TR', 'USA':'US', 'URY':'UY', 'UZB':'UZ', 'ZAF':'ZA',
    'COD':'CD', 'CRO':'HR', 'GER':'DE', 'JOR':'JO', 'NED':'NL',
    'PAR':'PY', 'POR':'PT', 'KSA':'SA', 'RSA':'ZA', 'SUI':'CH',
    'URU':'UY'
}


def norm(s):
    s = str(s)

    s = unicodedata.normalize("NFD", s)

    s = "".join(
        c for c in s
        if unicodedata.category(c) != "Mn"
    )

    return s.lower().strip()


# ==========================================
# TAO DICTIONARY FBREF
# ==========================================

std_keys = {}

for _, row in std.iterrows():

    name = norm(row["player_name"])
    team = str(row["national_team"]).split()[0].upper()

    std_keys[(name, team)] = row["player_name"]


# ==========================================
# DOC MANUAL MAPPING
# ==========================================

manual_file = "data/manual_mapping.csv"

manual = pd.read_csv(manual_file)

manual_dict = {}

for _, row in manual.iterrows():

    decision = str(row["decision"]).strip().upper()

    if decision != "MATCH":
        continue

    raw_name = norm(row["raw_name"])

    fifa_team = str(row["team"]).strip().upper()

    # Chuyen ma FIFA sang ma FBref
    team = team_map.get(fifa_team, "")

    fbref_name = str(row["fbref_name"]).strip()

    manual_dict[(raw_name, team)] = fbref_name

# ==========================================
# MATCHING
# ==========================================

matched_indices = set()

match_type = {}

normal = 0
moved = 0
manual_count = 0


for index, row in raw.iterrows():

    raw_name = norm(row["player_name"])
    raw_team = team_map.get(
        row["national_team"],
        ""
    )


    # ======================================
    # 1. MANUAL MATCH
    # ======================================

    if (raw_name, raw_team) in manual_dict:

        matched_indices.add(index)

        match_type[index] = "manual"

        manual_count += 1

        continue


    # ======================================
    # 2. EXACT MATCH
    # ======================================

    if (raw_name, raw_team) in std_keys:

        matched_indices.add(index)

        match_type[index] = "normal"

        normal += 1

        continue


    # ======================================
    # 3. MOVED NAME MATCH
    # ======================================

    parts = raw_name.split()

    if len(parts) >= 2:

        moved_name = " ".join(
            [parts[-1]] + parts[:-1]
        )

    else:

        moved_name = raw_name


    if (moved_name, raw_team) in std_keys:

        matched_indices.add(index)

        match_type[index] = "moved"

        moved += 1

        continue


# ==========================================
# KET QUA
# ==========================================

matched = len(matched_indices)

unmatched = len(raw) - matched


print()
print("==========================================")
print("MATCH RESULT")
print("==========================================")

print(
    "Normal exact match :",
    normal
)

print(
    "Moved name match   :",
    moved
)

print(
    "Manual match       :",
    manual_count
)

print(
    "Tong match         :",
    matched
)

print(
    "Unmatched           :",
    unmatched
)


# ==========================================
# LAY 887 CAU THU
# ==========================================

players_matched = raw.loc[
    sorted(matched_indices)
].copy()


# ==========================================
# TIM FBREF NAME
# ==========================================

fbref_names = []
match_types = []


for index, row in players_matched.iterrows():

    raw_name = norm(row["player_name"])

    raw_team = team_map.get(
        row["national_team"],
        ""
    )


    fbref_name = None
    current_match_type = None


    # ======================================
    # MANUAL
    # ======================================

    if (raw_name, raw_team) in manual_dict:

        fbref_name = manual_dict[
            (raw_name, raw_team)
        ]

        current_match_type = "manual"


    # ======================================
    # EXACT
    # ======================================

    elif (raw_name, raw_team) in std_keys:

        fbref_name = std_keys[
            (raw_name, raw_team)
        ]

        current_match_type = "normal"


    # ======================================
    # MOVED
    # ======================================

    else:

        parts = raw_name.split()

        if len(parts) >= 2:

            moved_name = " ".join(
                [parts[-1]] + parts[:-1]
            )

        else:

            moved_name = raw_name


        if (moved_name, raw_team) in std_keys:

            fbref_name = std_keys[
                (moved_name, raw_team)
            ]

            current_match_type = "moved"


    fbref_names.append(fbref_name)
    match_types.append(current_match_type)


# ==========================================
# THEM THONG TIN MATCHING
# ==========================================

players_matched["fbref_name"] = fbref_names
players_matched["match_type"] = match_types


# ==========================================
# LUU FILE
# ==========================================

output_file = "data/players_matched.csv"


players_matched.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


# ==========================================
# KIEM TRA CUOI
# ==========================================

print()
print("==========================================")
print("DA TAO DATASET MATCHED")
print("==========================================")

print(
    "So cau thu:",
    len(players_matched)
)

print(
    "File:",
    output_file
)

print()
print("Match type trong dataset:")

print(
    players_matched["match_type"].value_counts()
)