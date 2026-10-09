import os
import re
import unicodedata
import pandas as pd
import numpy as np
from rapidfuzz import process, fuzz

# ==========================================
# 1. CẤU HÌNH ĐƯỜNG DẪN & MÃ ĐỘI TUYỂN
# ==========================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

RAW_PATH = os.path.join(DATA_DIR, "players_raw.csv")
STD_PATH = os.path.join(DATA_DIR, "player_standard_clean.csv")
SHOOT_PATH = os.path.join(DATA_DIR, "player_shooting_clean.csv")
DEF_PATH = os.path.join(DATA_DIR, "player_defense_clean.csv")
KEEP_PATH = os.path.join(DATA_DIR, "player_keeper_clean.csv")

OUTPUT_PATH = os.path.join(DATA_DIR, "players_master_dataset.csv")

TEAM_MAP = {
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

EXCEPTIONS = {
    ("vinicius jose paixao de oliveira junior", "BR"): "Vinícius Júnior",
    ("gabriel fernando de jesus", "BR"): "Gabriel Jesus",
    ("rodrygo silva de goes", "BR"): "Rodrygo",
    ("raphael dias belloli", "BR"): "Raphinha",
    ("neymar da silva santos junior", "BR"): "Neymar",
    ("ederson santana de moraes", "BR"): "Ederson",
    ("alisson ramses becker", "BR"): "Alisson",
    ("marquinhos marcos aoas correa", "BR"): "Marquinhos",
    ("federico santiago valverde dipetta", "UY"): "Federico Valverde",
    ("darwin gabriel nunez ribeiro", "UY"): "Darwin Núñez",
    ("lautaro javier martinez", "AR"): "Lautaro Martínez",
    ("julian alvarez", "AR"): "Julián Álvarez",
    ("enzo jeremias fernandez", "AR"): "Enzo Fernández",
    ("alexis mac allister", "AR"): "Alexis Mac Allister"
}


# ==========================================
# 2. HÀM CHUẨN HÓA CHUỖI
# ==========================================
def norm(s):
    if pd.isna(s):
        return ""
    s = str(s)
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.lower().strip()

def clean_team_code(val):
    if pd.isna(val):
        return ""
    parts = str(val).strip().split()
    if len(parts) >= 2:
        return parts[0].upper()
    return str(val).strip().upper()

def clean_club_name(val):
    if pd.isna(val) or str(val).strip() == "" or str(val).strip().lower() == "nan":
        return "Free Agent"
    s = str(val).strip()
    s = re.sub(r'^\d+\.[a-z]{2,3}\s+', '', s)
    return s


# ==========================================
# 3. NẠP DỮ LIỆU & TIỀN XỬ LÝ SƠ BỘ
# ==========================================
print("🚀 Đang nạp các file dữ liệu CSV...")
df_raw = pd.read_csv(RAW_PATH)
df_std = pd.read_csv(STD_PATH)
df_shoot = pd.read_csv(SHOOT_PATH)
df_def = pd.read_csv(DEF_PATH)
df_keep = pd.read_csv(KEEP_PATH)

df_std["team_code"] = df_std["national_team"].apply(clean_team_code)
df_shoot["team_code"] = df_shoot["national_team"].apply(clean_team_code)
df_def["team_code"] = df_def["national_team"].apply(clean_team_code)
df_keep["team_code"] = df_keep["national_team"].apply(clean_team_code)

fbref_data = {}

for _, row in df_std.iterrows():
    name_norm = norm(row["player_name"])
    team = row["team_code"]
    key = (name_norm, team)
    fbref_data[key] = {
        "fbref_name": row["player_name"],
        "matches": row.get("matches", 0),
        "starts": row.get("starts", 0),
        "minutes": row.get("minutes", 0),
        "90s": row.get("90s", 0.0),
        "goals": row.get("goals", 0),
        "assists": row.get("assists", 0),
        "goals_assists": row.get("goals_assists", 0),
        "goals_minus_pk": row.get("goals_minus_pk", 0),
        "penalties": row.get("penalties", 0),
        "penalties_attempted": row.get("penalties_attempted", 0),
        "yellow_cards": row.get("yellow_cards", 0),
        "red_cards": row.get("red_cards", 0),
    }

for _, row in df_shoot.iterrows():
    key = (norm(row["player_name"]), row["team_code"])
    if key in fbref_data:
        fbref_data[key]["shots"] = row.get("shots", 0)
        fbref_data[key]["shots_on_target"] = row.get("shots_on_target", 0)

for _, row in df_def.iterrows():
    key = (norm(row["player_name"]), row["team_code"])
    if key in fbref_data:
        fbref_data[key]["tackles_won"] = row.get("tackles_won", 0)
        fbref_data[key]["interceptions"] = row.get("interceptions", 0)

for _, row in df_keep.iterrows():
    key = (norm(row["player_name"]), row["team_code"])
    if key in fbref_data:
        fbref_data[key]["goals_against"] = row.get("goals_against", 0.0)
        fbref_data[key]["ga90"] = row.get("ga90", 0.0)
        fbref_data[key]["shots_on_target_against"] = row.get("shots_on_target_against", 0.0)
        fbref_data[key]["saves"] = row.get("saves", 0.0)
        fbref_data[key]["save_pct"] = row.get("save_pct", 0.0)
        fbref_data[key]["clean_sheets"] = row.get("clean_sheets", 0.0)
        fbref_data[key]["clean_sheet_pct"] = row.get("clean_sheet_pct", 0.0)


# ==========================================
# 4. MATCHING VÀ TIỀN XỬ LÝ ĐIỀN 0 (IMPUTATION)
# ==========================================
print("\n🔄 Đang chạy Matching & Tiền xử lý dữ liệu khuyết...")

matched_records = []
for _, row in df_raw.iterrows():
    raw_name = str(row["player_name"])
    raw_norm = norm(raw_name)
    raw_nat = str(row["national_team"]).strip().upper()
    team_code = TEAM_MAP.get(raw_nat, raw_nat)
    
    match_key = None
    
    # Vòng 1
    if (raw_norm, team_code) in fbref_data:
        match_key = (raw_norm, team_code)
        
    # Vòng 2
    if not match_key:
        parts = raw_norm.split()
        if len(parts) >= 2:
            moved_norm = " ".join([parts[-1]] + parts[:-1])
            if (moved_norm, team_code) in fbref_data:
                match_key = (moved_norm, team_code)

    # Vòng 3
    if not match_key and (raw_norm, team_code) in EXCEPTIONS:
        target_fb_name = EXCEPTIONS[(raw_norm, team_code)]
        target_norm = norm(target_fb_name)
        if (target_norm, team_code) in fbref_data:
            match_key = (target_norm, team_code)

    # Vòng 4
    if not match_key:
        candidates = [k[0] for k in fbref_data.keys() if k[1] == team_code]
        if candidates:
            parts = raw_norm.split()
            queries = [raw_norm]
            if len(parts) >= 2:
                queries.append(" ".join([parts[-1]] + parts[:-1]))
                
            best_cand = None
            best_score = 0.0
            for q in queries:
                res = process.extractOne(q, candidates, scorer=fuzz.WRatio)
                if res and res[1] > best_score:
                    best_cand = res[0]
                    best_score = res[1]
                    
            if best_cand and best_score >= 75.0:
                match_key = (best_cand, team_code)

    rec = {
        "player_id": row.get("player_id"),
        "player_name": raw_name,
        "national_team": raw_nat,
        "nationality": row.get("nationality", "Unknown"),
        "club": clean_club_name(row.get("club")),
        "position": str(row.get("position", "MF")).upper(),
        "age": pd.to_numeric(row.get("age"), errors='coerce'),
        "height_cm": pd.to_numeric(row.get("height_cm"), errors='coerce'),
        "is_matched": 1 if match_key else 0
    }
    
    if match_key:
        stats = fbref_data[match_key]
        rec.update(stats)
    else:
        # Tiền xử lý: Điền 0 và 'Not in FBref' cho các cầu thủ không match được
        rec.update({
            "fbref_name": "Not in FBref", "matches": 0, "starts": 0, "minutes": 0, "90s": 0.0,
            "goals": 0, "assists": 0, "goals_assists": 0, "goals_minus_pk": 0,
            "penalties": 0, "penalties_attempted": 0, "yellow_cards": 0, "red_cards": 0,
            "shots": 0, "shots_on_target": 0, "tackles_won": 0, "interceptions": 0,
            "goals_against": 0.0, "ga90": 0.0, "shots_on_target_against": 0.0,
            "saves": 0.0, "save_pct": 0.0, "clean_sheets": 0.0, "clean_sheet_pct": 0.0
        })
        
    matched_records.append(rec)

df_master = pd.DataFrame(matched_records)


# ==========================================
# 5. TIỀN XỬ LÝ HOÀN THIỆN (IMPUTATION & FEATURE ENGINEERING)
# ==========================================
print("🧹 Đang thực hiện Tiền xử lý dữ liệu khuyết (Imputation = 0)...")

# Điền 0 / trung bình cho age/height nếu bị trống
df_master["age"] = df_master["age"].fillna(df_master["age"].median())
df_master["height_cm"] = df_master["height_cm"].fillna(df_master["height_cm"].median())

num_cols = ["matches", "starts", "minutes", "90s", "goals", "assists", "goals_assists", 
            "goals_minus_pk", "penalties", "penalties_attempted", "yellow_cards", "red_cards",
            "shots", "shots_on_target", "tackles_won", "interceptions", "goals_against", 
            "ga90", "shots_on_target_against", "saves", "save_pct", "clean_sheets", "clean_sheet_pct"]

for col in num_cols:
    df_master[col] = pd.to_numeric(df_master[col], errors='coerce').fillna(0)

def get_position_group(pos):
    pos = str(pos).upper()
    if 'GK' in pos:
        return 'GK'
    elif 'DF' in pos or 'CB' in pos or 'LB' in pos or 'RB' in pos:
        return 'DF'
    elif 'MF' in pos or 'CM' in pos or 'DM' in pos or 'AM' in pos:
        return 'MF'
    elif 'FW' in pos or 'ST' in pos or 'RW' in pos or 'LW' in pos:
        return 'FW'
    return 'MF'

df_master["position_group"] = df_master["position"].apply(get_position_group)

n90_actual = np.maximum(df_master["90s"].values, 0.1)

df_master["goals_p90"] = np.round(df_master["goals"] / n90_actual, 2)
df_master["assists_p90"] = np.round(df_master["assists"] / n90_actual, 2)
df_master["g_plus_a"] = df_master["goals"] + df_master["assists"]
df_master["g_plus_a_p90"] = np.round(df_master["g_plus_a"] / n90_actual, 2)
df_master["shots_p90"] = np.round(df_master["shots"] / n90_actual, 2)
df_master["shots_on_target_p90"] = np.round(df_master["shots_on_target"] / n90_actual, 2)
df_master["shot_accuracy_pct"] = np.where(
    df_master["shots"] > 0, 
    np.round((df_master["shots_on_target"] / df_master["shots"]) * 100, 1), 
    0.0
)
df_master["tackles_won_p90"] = np.round(df_master["tackles_won"] / n90_actual, 2)
df_master["interceptions_p90"] = np.round(df_master["interceptions"] / n90_actual, 2)

# Tính overall_rating
def calculate_overall_rating(row):
    pos = row["position_group"]
    mins = row["minutes"]
    n90_raw = row["90s"]
    n90_eff = max(n90_raw, 1.0)
    
    base_score = 65.0
    time_factor = min(1.0, mins / 360.0) * 6.0
    score = base_score + time_factor
    
    if pos == 'GK':
        if mins > 0:
            score += min(12.0, (row["clean_sheets"] * 3.0))
            score += min(8.0, (row["save_pct"] * 0.08))
            score -= (row["ga90"] * 1.5)
    elif pos == 'DF':
        score += min(10.0, (row["tackles_won"] / n90_eff) * 2.5)
        score += min(10.0, (row["interceptions"] / n90_eff) * 2.5)
        score += min(10.0, (row["g_plus_a"] * 2.5))
    elif pos == 'MF':
        score += min(12.0, (row["assists"] / n90_eff) * 5.0)
        score += min(10.0, (row["goals"] / n90_eff) * 4.0)
        score += min(6.0, (row["tackles_won"] / n90_eff) * 1.5)
        score += min(6.0, (row["interceptions"] / n90_eff) * 1.5)
    elif pos == 'FW':
        score += min(16.0, (row["goals"] / n90_eff) * 5.0)
        score += min(10.0, (row["assists"] / n90_eff) * 4.0)
        score += min(5.0, (row["shot_accuracy_pct"] * 0.05))
        
    score -= (row["yellow_cards"] * 1.0 + row["red_cards"] * 3.0)
    return float(np.round(np.clip(score, 55.0, 99.0), 1))

df_master["overall_rating"] = df_master.apply(calculate_overall_rating, axis=1)

# Export Master Dataset
df_master.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')

# Cập nhật cả file players_unmatched.csv với điền 0 đầy đủ
df_unmatched = df_master[df_master["is_matched"] == 0]
df_unmatched.to_csv(os.path.join(DATA_DIR, "players_unmatched.csv"), index=False, encoding='utf-8-sig')

print(f"\n✅ TIỀN XỬ LÝ HOÀN TẤT & ĐÃ XUẤT THÀNH CÔNG:")
print(f"  📍 Tệp Master Dataset: {OUTPUT_PATH}")
print(f"  📍 Tệp Cầu thủ chưa khớp (Đã điền 0): {os.path.join(DATA_DIR, 'players_unmatched.csv')}")
print(f"  ✨ Tổng số ô Null còn lại trong Master Dataset: {df_master.isnull().sum().sum()}")
