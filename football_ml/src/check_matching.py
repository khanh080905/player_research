import pandas as pd
import unicodedata
from rapidfuzz import process, fuzz


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
# EXACT MATCH
# ==========================================

matched = 0
normal = 0
moved = 0
unmatched = []


for _, row in raw.iterrows():

    raw_name = norm(row["player_name"])
    raw_team = team_map.get(row["national_team"], "")

    # ------------------------------
    # Cach 1: ten giong nhau
    # ------------------------------

    if (raw_name, raw_team) in std_keys:

        matched += 1
        normal += 1
        continue


    # ------------------------------
    # Cach 2: dua tu cuoi len dau
    # ------------------------------

    parts = raw_name.split()

    if len(parts) >= 2:

        moved_name = " ".join(
            [parts[-1]] + parts[:-1]
        )

    else:

        moved_name = raw_name


    if (moved_name, raw_team) in std_keys:

        matched += 1
        moved += 1
        continue


    unmatched.append(
        (
            row["player_name"],
            row["national_team"],
            raw_name,
            raw_team
        )
    )


print("Normal:", normal)
print("Đưa tên cuối lên đầu:", moved)
print("Tổng match:", matched)
print("Unmatched:", len(unmatched))


# ==========================================
# FUZZY MATCH
# ==========================================

print("\n==========================================")
print("FUZZY MATCH - 364 UNMATCHED")
print("==========================================")


for original_name, original_team, raw_name, raw_team in unmatched:

    candidates = [
        name
        for (name, team) in std_keys.keys()
        if team == raw_team
    ]


    if not candidates:

        print(
            f"\n{original_name} | {original_team}"
            f"\n  -> KHONG CO DU LIEU FBREF"
        )

        continue


    # --------------------------------------
    # Tao them dang "ten cuoi len dau"
    # --------------------------------------

    parts = raw_name.split()

    queries = [raw_name]

    if len(parts) >= 2:

        moved_name = " ".join(
            [parts[-1]] + parts[:-1]
        )

        queries.append(moved_name)


    # --------------------------------------
    # Tim ket qua tot nhat
    # --------------------------------------

    best = None


    for query in queries:

        results = process.extract(
            query,
            candidates,
            scorer=fuzz.WRatio,
            limit=3
        )

        for candidate, score, _ in results:

            if best is None or score > best[1]:

                best = (
                    candidate,
                    score,
                    query
                )


    candidate = best[0]
    score = best[1]
    query_used = best[2]

    fbref_name = std_keys[(candidate, raw_team)]


    print(
        f"\n{original_name} | {original_team}"
    )

    print(
        f"  -> {fbref_name}"
        f" | score = {score:.1f}"
        f" | query = {query_used}"
    )