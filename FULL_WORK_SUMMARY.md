# 📋 Báo Cáo Tổng Hợp Toàn Bộ Công Việc Đã Thực Hiện

**Dự án**: World Cup 2026 Portal & Football Player Research  
**Thư mục làm việc**: `/home/pham_vinh/Desktop/bai_tap_nhom_mnm`  
**Ngày cập nhật**: 21/09/2026  

---

## 📌 1. Tổng Quan Dự Án

Dự án phát triển hệ thống **Tra cứu & Nghiên cứu Dữ liệu Cầu thủ hướng tới World Cup 2026**, bao gồm việc xây dựng **Giao diện Web Frontend Portal** và **Hệ thống Tiền xử lý & Hợp nhất Dữ liệu Master (Data Engineering)** phục vụ cho các bài toán phân tích & thống kê bóng đá.

---

## 💻 2. Chi Tiết Các Công Việc Đã Thực Hiện

### 🌐 PHẦN A: GIAO DIỆN WEB FRONTEND (`player_research/`)

1. **Khung Cấu Trúc HTML (`index.html`)**:
   * Đã dựng xong cấu trúc trang chủ **World Cup 2026 Portal**.
   * Đã thiết kế thanh điều hướng Sticky Header Navigation với các mục liên kết:
     * `Trang chủ` (`index.html`)
     * `Bảng xếp hạng` (`standings.html`)
     * `Tìm kiếm cầu thủ` (`players.html`)
     * `Trận đấu` (`matches.html`)
     * `Dự đoán cầu thủ` (`predict.html`)
   * Tích hợp logo chính thức FIFA World Cup 2026 (SVG) và bộ icon FontAwesome 6.2.1.
2. **Thiết Kế Style CSS (`style.css`)**:
   * Đã xây dựng giao diện **Dark Mode** tông đen/xám tối (`#121212` và `#000000`) chuẩn phong cách FIFA.
   * Tích hợp font chữ **Spartan** từ Google Fonts.
   * Định dạng khung bao `main-wrapper` căn giữa (max-width 1280px) kèm hiệu ứng đổ bóng.

---

### 🗃️ PHẦN B: QUẢN LÝ & SAO LƯU DỮ LIỆU (`football_ml/data/`)

1. **Tạo Bản Sao Lưu Dữ Liệu An Toàn (`data_backup/`)**:
   * Đã sao lưu 100% dữ liệu gốc từ `data/` sang thư mục `player_research/football_ml/data_backup/` để đảm bảo không mất mát dữ liệu gốc trong quá trình xử lý.
2. **Đánh Giá & Phát Hiện Lỗi Dữ Liệu (`DATA_ISSUES_REPORT.md`)**:
   * Đã phân tích 7 tệp CSV gốc và phát hiện các vấn đề:
     * Lỗi dữ liệu khuyết 100% ở các cột chỉ số nâng cao (`defense`, `gca`, `passing`).
     * Lệch ghép nối giữa danh sách World Cup 2026 (`players_raw.csv` - 1,248 cầu thủ) và dữ liệu FBref (`player_standard_clean.csv` - 1,039 cầu thủ).
     * Lỗi phép chia cho 0 ở các cột tỷ lệ dứt điểm.

---

### 🔄 PHẦN C: KHỚP NỐI & TIỀN XỬ LÝ DỮ LIỆU MASTER

1. **Thuật Toán Matching Cầu Thủ 4 Vòng (`src/build_master_dataset.py`)**:
   * **Vòng 1 (Exact Match)**: Bỏ dấu NFD Unicode + Chuyển chữ thường -> Khớp 122 cầu thủ.
   * **Vòng 2 (Name Reversal Match)**: Đảo thứ tự `Họ <-> Tên` -> Khớp thêm 762 cầu thủ.
   * **Vòng 3 (Exception Map)**: Ánh xạ từ điển ngoại lệ gán tay cho các siêu sao tên biệt danh khác biệt.
   * **Vòng 4 (Fuzzy Match)**: Lọc theo Đội tuyển & Tuổi, dùng `rapidfuzz` với điểm tương đồng `score >= 75%` -> Khớp thêm 160 cầu thủ.
   * **Tỷ lệ khớp thành công**: **1,044 / 1,248 cầu thủ (đạt 83.7%)**.
2. **Phân Tích & Xuất Danh Sách Cầu Thủ Chưa Khớp**:
   * Đã viết script `src/print_unmatched_players.py` trích xuất 204 cầu thủ chưa khớp.
   * **Nguyên nhân 204 ca chưa khớp**: Do 204 cầu thủ này có tên trong danh sách World Cup nhưng **hoàn toàn KHÔNG TỒN TẠI trong bộ dữ liệu FBref** (hoặc là cầu thủ dự bị không ra sân phút nào).
   * **Đã xuất tệp CSV riêng**: [data/players_unmatched.csv](file:///home/pham_vinh/Desktop/bai_tap_nhom_mnm/player_research/football_ml/data/players_unmatched.csv).
   * **Đã xuất tệp Báo cáo Markdown**: [UNMATCHED_PLAYERS_REPORT.md](file:///home/pham_vinh/Desktop/bai_tap_nhom_mnm/player_research/football_ml/UNMATCHED_PLAYERS_REPORT.md).
3. **Tiền Xử Lý Dữ Liệu Khuyết (Imputation = 0)**:
   * **Xử lý toàn bộ chỉ số số (Numeric Metrics)**: Điền `0` cho các chỉ số đếm (`goals`, `assists`, `minutes`, `tackles_won`...) và `0.0` cho các chỉ số tỷ lệ/per 90.
   * **Xử lý văn bản (Categorical)**: Điền `"Not in FBref"` cho `fbref_name` khuyết và `"Free Agent"` cho `club` khuyết.
   * **Kết quả**: ✨ **Tỉ lệ ô Null còn lại trong Master Dataset = 0 (Sạch 100%)**.
4. **Kỹ Sư Đặc Trưng & Cột Target (Feature Engineering)**:
   * Tạo các chỉ số Per 90 (`goals_p90`, `assists_p90`, `g_plus_a_p90`, `shots_p90`, `tackles_won_p90`...).
   * Phân nhóm 4 vị trí chính (`GK`, `DF`, `MF`, `FW`).
   * Tính toán cột Target `overall_rating` (Thang điểm 55.0 - 99.0 đã được chuẩn hóa theo thời lượng thi đấu).

---

## 📊 3. Danh Sách Các Tệp Đã Tạo & Cập Nhật

| Tệp Dữ Liệu / Mã Nguồn | Loại Tệp | Mục Đích & Nội Dung |
| :--- | :---: | :--- |
| **[players_master_dataset.csv](file:///home/pham_vinh/Desktop/bai_tap_nhom_mnm/player_research/football_ml/data/players_master_dataset.csv)** | `CSV` | **Tệp Master hoàn chỉnh** (1,248 cầu thủ, 44 cột, sạch 100% không còn ô Null) |
| **[players_unmatched.csv](file:///home/pham_vinh/Desktop/bai_tap_nhom_mnm/player_research/football_ml/data/players_unmatched.csv)** | `CSV` | Tệp chứa 204 cầu thủ chưa khớp (đã được điền 0 đầy đủ) |
| **[build_master_dataset.py](file:///home/pham_vinh/Desktop/bai_tap_nhom_mnm/player_research/football_ml/src/build_master_dataset.py)** | `Python` | Mã nguồn tự động hóa toàn bộ quá trình Matching, Tiền xử lý & Hợp nhất |
| **[print_unmatched_players.py](file:///home/pham_vinh/Desktop/bai_tap_nhom_mnm/player_research/football_ml/src/print_unmatched_players.py)** | `Python` | Mã nguồn trích xuất & tạo báo cáo cầu thủ chưa khớp |
| **[DATA_ISSUES_REPORT.md](file:///home/pham_vinh/Desktop/bai_tap_nhom_mnm/player_research/football_ml/DATA_ISSUES_REPORT.md)** | `Markdown` | Báo cáo chi tiết các vấn đề của bộ dữ liệu thô |
| **[UNMATCHED_PLAYERS_REPORT.md](file:///home/pham_vinh/Desktop/bai_tap_nhom_mnm/player_research/football_ml/UNMATCHED_PLAYERS_REPORT.md)** | `Markdown` | Danh sách 204 cầu thủ chưa khớp dữ liệu FBref |
| **`data_backup/`** | `Folder` | Thư mục sao lưu nguyên vẹn 7 tệp dữ liệu CSV ban đầu |

---

## 🎯 4. Trạng Thái Hiện Tại & Các Bước Tiếp Theo Khuyên Dùng

* **Trạng thái Dữ liệu**: **Đã hoàn thiện 100%**. Bộ dữ liệu [players_master_dataset.csv](file:///home/pham_vinh/Desktop/bai_tap_nhom_mnm/player_research/football_ml/data/players_master_dataset.csv) đã sẵn sàng phục vụ tra cứu, phân tích hoặc tích hợp vào Web.
* **Các bước tiếp theo (Tùy chọn)**:
  1. Viết mã JavaScript (`scripts.js`) để nạp tệp Master Dataset và hiển thị lên giao diện Web.
  2. Xây dựng các trang giao diện phụ (`players.html`, `standings.html`...).
