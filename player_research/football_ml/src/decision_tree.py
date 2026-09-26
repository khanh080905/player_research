import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 1. Import đầy đủ các thư viện cần thiết
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
# 1. Import thêm PredictionErrorDisplay ở đầu file
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, PredictionErrorDisplay
# 2. Đọc dữ liệu từ file Master Dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "players_master_dataset.csv")

data = pd.read_csv(DATA_PATH)

target = "overall_rating"

# 3. Lọc chỉ lấy các cột DỮ LIỆU SỐ (bỏ các cột tên chữ)
numeric_data = data.select_dtypes(include=[np.number]).fillna(0)

# Loại bỏ các cột ID không có ý nghĩa dự đoán
cols_to_drop = [target, "player_id", "is_matched"]
feature_cols = [c for c in numeric_data.columns if c not in cols_to_drop]

X = numeric_data[feature_cols]
y = numeric_data[target]

# 4. Tách tập Train (80%) và Test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Chuẩn hóa dữ liệu bằng StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Cấu hình dải tham số cho Random Forest Regressor
param_grid = {
    "n_estimators": [100, 150, 200],
    "criterion": ["squared_error", "absolute_error"],
    "max_depth": [10, 15, None]
}

# 7. Khởi tạo GridSearchCV (dùng Regressor & scoring R2)
grid_search = GridSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1,
    verbose=2
)

print("🔍 Đang huấn luyện và tìm kiếm tham số tối ưu...")
grid_search.fit(X_train_scaled, y_train)

# 8. In kết quả tốt nhất
print("\n🏆 Tham số tốt nhất:", grid_search.best_params_)
print(f"⭐ R² score tốt nhất trên tập Train (CV): {grid_search.best_score_:.4f}")

# 9. Đánh giá mô hình trên tập Test
best_model = grid_search.best_estimator_
y_predict = best_model.predict(X_test_scaled)

r2 = r2_score(y_test, y_predict)
mae = mean_absolute_error(y_test, y_predict)
rmse = np.sqrt(mean_squared_error(y_test, y_predict))

print("\n📊 BÁO CÁO ĐÁNH GIÁ TRÊN TẬP TEST:")
print(f"  - R² Score: {r2:.4f}")
print(f"  - MAE (Lỗi trung bình): {mae:.4f}")
print(f"  - RMSE: {rmse:.4f}")


# plt.figure(figsize=(8, 6))
# plt.scatter(y_test, y_predict, alpha=0.6, color='blue')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2) # Đường lý tưởng
# plt.xlabel('Điểm Thực Tế (Actual Rating)')
# plt.ylabel('Điểm Dự Đoán (Predicted Rating)')
# plt.title('Đồ Thị So Sánh Actual vs Predicted')
# plt.grid(True)
# plt.show()
print("\n🎨 Đang hiển thị đồ thị so sánh Actual vs Predicted...")
PredictionErrorDisplay.from_predictions(y_test, y_predict, kind="actual_vs_predicted")
plt.show()