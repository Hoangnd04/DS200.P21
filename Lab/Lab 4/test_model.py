import pandas as pd
import joblib
import numpy as np
from preprocess_transform import preprocess_data
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Đang tải dữ liệu và mô hình...")
data = pd.read_csv('./insurance_data/insurance.csv')[-64:]
model = joblib.load("trained_model.pkl")


print("Đang tiền xử lý dữ liệu...")
X_test, y_test = [], []
for row in data.itertuples(index=False):
    processed = preprocess_data([
        row.age, row.sex, row.bmi, row.children, row.smoker, row.region, row.charges
    ])
    X_test.append(processed[:-1])
    y_test.append(processed[-1])

print("Đang dự đoán...")
y_pred = model.predict(X_test)

print("\nĐÁNH GIÁ MÔ HÌNH:")
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"• MSE (Mean Squared Error): {mse:.2f}")
print(f"• RMSE (Root MSE): {np.sqrt(mse):.2f}")
print(f"• MAE (Mean Absolute Error): {mae:.2f}")
print(f"• R-squared (R²): {r2:.2f}")

results = pd.DataFrame({
    'STT': range(1, len(y_test)+1),
    'Actual': y_test,
    'Predicted': y_pred,
    'Chênh lệch': y_test - y_pred,
    'Sai số (%)': np.abs((y_test - y_pred)/y_test)*100
})

pd.set_option('display.float_format', '{:.2f}'.format)
print("\nCHI TIẾT DỰ ĐOÁN (10 mẫu đầu):")
print(results.head(10))

print("\nTHỐNG KÊ SAI SỐ:")
print(results['Sai số (%)'].describe().to_frame().T)

plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
plt.xlabel('Giá trị thực tế')
plt.ylabel('Giá trị dự đoán')
plt.title('So sánh Actual vs Predicted')
plt.grid(True)

plt.subplot(1, 2, 2)
sns.histplot(results['Chênh lệch'], kde=True)
plt.xlabel('Sai số (Actual - Predicted)')
plt.title('Phân bố sai số')
plt.axvline(x=0, color='r', linestyle='--')
plt.grid(True)

plt.tight_layout()
plt.show()

os.makedirs('results', exist_ok=True)
results.to_csv('results/prediction_results.csv', index=False)
print("\nKết quả đã được lưu vào file 'results/prediction_results.csv'")