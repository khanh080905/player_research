# Báo Cáo Phân Tích & Các Vấn Đề Của Bộ Dữ Liệu Football ML

---

## 📌 1. Tổng Quan Dữ Liệu Hiện Tại

Dự án nghiên cứu dữ liệu cầu thủ hiện lưu trữ 7 tệp CSV chính tại đường dẫn `player_research/football_ml/data/`:

| Tệp Dữ Liệu | Số Dòng | Số Cột | Trạng Thái Dữ Liệu |
| :--- | :---: | :---: | :--- |
| `player_standard_clean.csv` | 1,039 | 17 | Đầy đủ dữ liệu (Tiêu chuẩn) |
| `player_shooting_clean.csv` | 1,039 | 18 | Khả dụng (Khuyết tỷ lệ sút) |
| `player_keeper_clean.csv` | 62 | 26 | Đầy đủ dữ liệu (Thủ môn) |
| `player_defense_clean.csv` | 1,039 | 24 | **Mất dữ liệu 14/24 cột (100% null)** |
| `player_gca_clean.csv` | 1,039 | 24 | **Mất dữ liệu 16/24 cột (100% null)** |
| `player_passing_clean.csv` | 1,039 | 28 | **Mất dữ liệu 19/28 cột (100% null)** |
| `players_raw.csv` | 1,248 | 41 | **Mất dữ liệu 32/41 cột chỉ số trận đấu** |

---

## 🚨 2. Chi Tiết Các Vấn Đề Phát Hiện (Data Issues)

### 🔴 Vấn đề 1: Mất dữ liệu nghiêm trọng ở các tệp chỉ số nâng cao
Rất nhiều cột chỉ số quan trọng trong các tệp làm sạch (`clean`) đang bị để trống hoàn toàn (**100% missing values**):

1. **`player_defense_clean.csv`**:
   * **Các cột bị trống 100%**: `tackles_total`, `tackles_def_3rd`, `tackles_mid_3rd`, `tackles_att_3rd`, `tackles_attempted`, `tackle_success_pct`, `tackles_lost`, `blocks`, `blocked_shots`, `blocked_passes`, `clearances`, `errors`, `tackles_plus_interceptions`...
   * **Dữ liệu hiện có**: Chỉ chứa `tackles_won` và `interceptions`.
2. **`player_gca_clean.csv`**:
   * **Các cột bị trống 100%**: Toàn bộ chỉ số Tạo cơ hội dứt điểm (SCA) và Tạo bàn thắng (GCA) như `sca`, `sca_p90`, `sca_pass_live`, `sca_pass_dead`, `sca_take_ons`, `sca_shots`, `gca`, `gca_p90`, `gca_pass_live`...
3. **`player_passing_clean.csv`**:
   * **Các cột bị trống 100%**: Tất cả thông số phân loại đường chuyền (`short_*`, `medium_*`, `long_*`), tổng khoảng cách chuyền (`total_distance`, `progressive_distance`), đường chuyền vào 1/3 sân cuối (`passes_into_final_third`), tạt bóng...
4. **`players_raw.csv`**:
   * Hồ sơ danh sách World Cup 2026 chứa thông tin định danh (`player_name`, `national_team`, `club`, `age`, `height_cm`), nhưng toàn bộ 32 cột chỉ số trận đấu đi kèm bị bỏ trống hoàn toàn.

---

### 🟡 Vấn đề 2: Bất đồng bộ & Lệch dữ liệu ghép nối (Unmatched Players)
* **Chênh lệch số lượng**: `players_raw.csv` chứa **1,248 cầu thủ**, trong khi các tệp FBref (`player_standard_clean.csv`...) chỉ chứa **1,039 cầu thủ**.
* **Xung đột chuẩn hóa tên**:
  * Tệp Raw để định dạng: `HỌ Tên` (ví dụ: `MASTIL Melvin`, `MANDI Aissa`).
  * Tệp FBref để định dạng: `Tên Họ` (ví dụ: `Melvin Mastil`, `Aissa Mandi`).
  * Có ký tự đặc biệt tiếng Pháp, Tây Ban Nha, Ả Rập...
* **Kết quả từ script `check_matching.py`**:
  * Khớp tên trực tiếp: **675 cầu thủ**
  * Khớp tên sau khi đảo ngược `Tên <-> Họ`: **209 cầu thủ**
  * **Còn lại 364 cầu thủ (khoảng 30%) chưa ghép nối được** và cần xử lý bằng thuật toán mờ (Fuzzy Matching) hoặc crawler bổ sung.

---

### 🟠 Vấn đề 3: Phép chia cho 0 ở các chỉ số Tỷ lệ (Zero Division / NaN Metrics)
Trong tệp `player_shooting_clean.csv`:
* `shot_on_target_pct` & `goals_per_shot` bị thiếu **359 giá trị (34.6%)**.
* `goals_per_sot` bị thiếu **643 giá trị (61.9%)**.
* *Nguyên nhân:* Do cầu thủ không thực hiện cú sút nào (mẫu số bằng 0). Cần xử lý thế giá trị `0.0` thay vì để `NaN` để tránh gây lỗi cho mô hình Machine Learning.

---

### 🔵 Vấn đề 4: Thiếu Pipeline Hợp nhất Dữ liệu (Master Dataset ETL)
* Dữ liệu hiện tại đang nằm rải rác ở 7 tệp CSV độc lập.
* Thiếu mã nguồn hoàn chỉnh để Merge / Join tất cả các chỉ số (Standard, Shooting, Defense, Passing, Keeper) của cầu thủ thành 1 bảng duy nhất (Master Feature Table) phục vụ bài toán huấn luyện mô hình ML.

---

## 🛠️ 3. Đề Xuất Hướng Giải Quyết (Action Plan)

1. **Crawl / Bổ sung dữ liệu bị thiếu**:
   * Kiểm tra lại mã nguồn cào dữ liệu FBref/StatsBomb để lấy đầy đủ các cột bị khuyết trong `player_defense`, `player_passing`, và `player_gca`.
2. **Hoàn thiện Script Matching (`src/check_matching.py`)**:
   * Áp dụng `rapidfuzz` với ngưỡng tương đồng (threshold >= 85%) để tự động map 364 cầu thủ chưa ghép nối.
3. **Tiền xử lý & Điền dữ liệu khuyết (Imputation)**:
   * Thay thế các giá trị `NaN` ở các chỉ số tỷ lệ bằng `0.0`.
4. **Xây dựng Pipeline Hợp nhất (Data Merger)**:
   * Viết script Python (sử dụng Pandas) hợp nhất 7 tệp dữ liệu thành tệp `players_master_features.csv` chuẩn hóa sẵn sàng cho Machine Learning.
