import pandas as pd
import unicodedata
import re


RAW_FILE = "data/players_raw.csv"
STD_FILE = "data/player_standard_clean.csv"
MANUAL_FILE = "data/manual_mapping.csv"


def norm(s):
    s = str(s)

    s = unicodedata.normalize("NFD", s)

    s = "".join(
        c for c in s
        if unicodedata.category(c) != "Mn"
    )

    s = s.lower().strip()

    s = re.sub(r"[^a-z0-9]+", " ", s)

    s = re.sub(r"\s+", " ", s).strip()

    return s


# ==========================================
# TEAM MAP
# ==========================================

team_map = {
    'ALG':'DZ','ARG':'AR','AUT':'AT','AUS':'AU',
    'BIH':'BA','BEL':'BE','BRA':'BR','CAN':'CA',
    'CIV':'CI','COL':'CO','CPV':'CV','CUW':'CW',
    'CZE':'CZ','DEU':'DE','ECU':'EC','EGY':'EG',
    'ENG':'ENG','ESP':'ES','FRA':'FR','GHA':'GH',
    'HRV':'HR','HAI':'HT','IRQ':'IQ','IRN':'IR',
    'JPN':'JP','KOR':'KR','MAR':'MA','MEX':'MX',
    'NLD':'NL','NOR':'NO','NZL':'NZ','PAN':'PA',
    'PRT':'PT','PRY':'PY','QAT':'QA','SAU':'SA',
    'SCO':'SCT','SWE':'SE','SEN':'SN','TUN':'TN',
    'TUR':'TR','USA':'US','URY':'UY','UZB':'UZ',
    'ZAF':'ZA','COD':'CD','CRO':'HR','GER':'DE',
    'JOR':'JO','PAR':'PY','POR':'PT','KSA':'SA',
    'RSA':'ZA','SUI':'CH','URU':'UY'
}


# ==========================================
# LOAD
# ==========================================

raw = pd.read_csv(RAW_FILE)
std = pd.read_csv(STD_FILE)
manual = pd.read_csv(MANUAL_FILE)


# ==========================================
# NORMALIZE
# ==========================================

raw["name_norm"] = raw["player_name"].apply(norm)
std["name_norm"] = std["player_name"].apply(norm)

raw["team_code"] = raw["national_team"].map(team_map)

std["team_code"] = (
    std["national_team"]
    .astype(str)
    .str.split()
    .str[0]
    .str.upper()
)


# ==========================================
# TRACK MATCHES
# ==========================================

matched_raw = set()
matched_std = set()


# ==========================================
# 1. NORMAL EXACT MATCH
# ==========================================

std_key_map = {}

for std_idx, row in std.iterrows():

    key = (
        row["name_norm"]
        + "|"
        + str(row["team_code"])
    )

    if key not in std_key_map:
        std_key_map[key] = []

    std_key_map[key].append(std_idx)


normal_count = 0

for raw_idx, row in raw.iterrows():

    key = (
        row["name_norm"]
        + "|"
        + str(row["team_code"])
    )

    candidates = std_key_map.get(key, [])

    candidates = [
        x for x in candidates
        if x not in matched_std
    ]

    if len(candidates) == 1:

        std_idx = candidates[0]

        matched_raw.add(raw_idx)
        matched_std.add(std_idx)

        normal_count += 1


# ==========================================
# 2. MOVE LAST NAME TO FRONT
# ==========================================

moved_count = 0

for raw_idx, row in raw.iterrows():

    if raw_idx in matched_raw:
        continue

    parts = row["name_norm"].split()

    if len(parts) < 2:
        continue

    moved_name = " ".join(
        [parts[-1]] + parts[:-1]
    )

    key = (
        moved_name
        + "|"
        + str(row["team_code"])
    )

    candidates = std_key_map.get(key, [])

    candidates = [
        x for x in candidates
        if x not in matched_std
    ]

    if len(candidates) == 1:

        std_idx = candidates[0]

        matched_raw.add(raw_idx)
        matched_std.add(std_idx)

        moved_count += 1


# ==========================================
# 3. MANUAL MATCH
# ==========================================

manual_count = 0

for _, m in manual.iterrows():

    if str(m["decision"]).upper() != "MATCH":
        continue

    raw_name = norm(m["raw_name"])
    fbref_name = norm(m["fbref_name"])
    team = str(m["team"]).upper()

    team_code = team_map.get(team)

    raw_candidates = raw.index[
        (raw["name_norm"] == raw_name)
        &
        (raw["team_code"] == team_code)
    ].tolist()

    std_candidates = std.index[
        (std["name_norm"] == fbref_name)
        &
        (std["team_code"] == team_code)
    ].tolist()

    if len(raw_candidates) == 1 and len(std_candidates) == 1:

        raw_idx = raw_candidates[0]
        std_idx = std_candidates[0]

        if (
            raw_idx not in matched_raw
            and
            std_idx not in matched_std
        ):

            matched_raw.add(raw_idx)
            matched_std.add(std_idx)

            manual_count += 1


# ==========================================
# REAL UNMATCHED PLAYERS
# ==========================================

unmatched_indexes = [
    idx
    for idx in raw.index
    if idx not in matched_raw
]


unmatched = raw.loc[
    unmatched_indexes,
    [
        "player_name",
        "national_team",
        "position",
        "club"
    ]
].copy()


# ==========================================
# RESULT
# ==========================================

print()
print("==========================================")
print("REAL MATCH RESULT")
print("==========================================")

print(
    f"Normal exact match : {normal_count}"
)

print(
    f"Moved name match   : {moved_count}"
)

print(
    f"Manual match       : {manual_count}"
)

print(
    f"Tong match         : {len(matched_raw)}"
)

print(
    f"Unmatched           : {len(unmatched)}"
)


# ==========================================
# SAVE
# ==========================================

output_file = "data/unmatched_players.csv"

unmatched.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print()
print("==========================================")
print("UNMATCHED PLAYERS")
print("==========================================")

print(
    unmatched.to_string(index=False)
)

print()
print("==========================================")
print("DA LUU")
print("==========================================")

print(output_file)