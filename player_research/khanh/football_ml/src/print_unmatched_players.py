import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_PATH = os.path.join(BASE_DIR, "data", "players_master_dataset.csv")
CSV_UNMATCHED_PATH = os.path.join(BASE_DIR, "data", "players_unmatched.csv")
REPORT_PATH = os.path.join(BASE_DIR, "UNMATCHED_PLAYERS_REPORT.md")

print("🚀 Đang nạp tệp Master Dataset...")
df = pd.read_csv(MASTER_PATH)

# Lọc danh sách cầu thủ chưa khớp (is_matched == 0)
unmatched = df[df["is_matched"] == 0].copy()

print(f"\n==========================================")
print(f"📌 DANH SÁCH {len(unmatched)} CẦU THỦ CHƯA KHỚP (UNMATCHED)")
print(f"==========================================")

# 1. Xuất ra tệp CSV riêng
unmatched.to_csv(CSV_UNMATCHED_PATH, index=False, encoding='utf-8-sig')

# 2. Xuất toàn bộ 204 cầu thủ ra tệp Markdown báo cáo
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write(f"# 📋 Danh Sách {len(unmatched)} Cầu Thủ Chưa Khớp Dữ Liệu FBref\n\n")
    f.write("Dưới đây là toàn bộ danh sách cầu thủ có tên trong danh sách đăng ký World Cup 2026 (`players_raw.csv`) nhưng **chưa có dữ liệu thống kê chuyên môn trong FBref**:\n\n")
    f.write("| STT | Tên Cầu Thủ | Đội Tuyển | CLB | Vị Trí | Tuổi |\n")
    f.write("| :---: | :--- | :---: | :--- | :---: | :---: |\n")
    
    for idx, row in enumerate(unmatched.iterrows(), 1):
        r = row[1]
        f.write(f"| {idx} | **{r['player_name']}** | {r['national_team']} | {r['club']} | {r['position']} | {r['age']} |\n")

print(f"\n✅ ĐÃ XUẤT THÀNH CÔNG TỆP CSV CẦU THỦ CHƯA KHỚP:")
print(f"  📍 Đường dẫn tệp CSV: {CSV_UNMATCHED_PATH}")
print(f"  📍 Đường dẫn báo cáo MD: {REPORT_PATH}")
