# 🧪 Lab 4

## 🎯 Mục tiêu bài lab
Mục tiêu của Lab 4 là **giả lập một hệ thống gồm hai thành phần chính**:
1. **Server gửi dữ liệu (Sender):** Đóng vai trò phát dữ liệu theo luồng (streaming).
2. **Server nhận dữ liệu (Receiver):** Tiếp nhận dữ liệu và huấn luyện **mô hình học máy hoặc deep learning**.

## 🛠️ Cách sử dụng

1. **Cài đặt các thư viện phụ thuộc**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Chạy hệ thống**:
    Chạy file `main.py` để khởi động đồng thời cả **sender** (gửi dữ liệu) và **receiver** (huấn luyện mô hình):
    ```bash
    python main.py
    ```

    Hệ thống sẽ tự động bắt đầu việc huấn luyện mô hình với dữ liệu được gửi qua socket.

3. **Lưu mô hình**:
    Sau khi huấn luyện xong, mô hình sẽ được lưu vào thư mục `model` với tên `trained_model.pkl`.

4. **Đánh giá mô hình**:
    Để đánh giá mô hình đã huấn luyện với dữ liệu kiểm thử, chạy file `test_model.py`:
    ```bash
    python test_model.py
    ```
    Lệnh này sẽ:
    - Hiển thị các chỉ số đánh giá mô hình như MSE, MAE, R².
    - Lưu kết quả dự đoán vào file `results/prediction_results.csv`.
    - Hiển thị đồ thị so sánh giữa giá trị thực tế và dự đoán.

### 🔄 Quy trình làm việc của các file
- **`main.py`**: Điều phối các thread gửi và nhận dữ liệu, bắt đầu quá trình huấn luyện.
- **`stream_sender.py`**: Gửi dữ liệu theo các batch qua giao thức socket.
- **`stream_receiver.py`**: Nhận dữ liệu và huấn luyện mô hình.
- **`test_model.py`**: Đánh giá mô hình đã huấn luyện trên dữ liệu kiểm thử.
- **`preprocess_transform.py`**: Xử lý và chuyển đổi dữ liệu (tiền xử lý và kỹ thuật đặc trưng) trước khi huấn luyện.

### ⚙️ Cấu hình
Có thể điều chỉnh các tham số trong `main.py` để thay đổi cách thức hoạt động của hệ thống:
```python
host = 'localhost'       # Địa chỉ máy chủ
port = 9999              # Cổng giao tiếp  
batch_size = 256         # Kích thước batch dữ liệu
epochs = 100             # Số lượng epoch huấn luyện
learning_rate = 0.001    # Tốc độ học của mô hình
```
### 📂 Các file được tạo ra

- **`model/trained_model.pkl`**: Mô hình học máy đã huấn luyện.

- **`results/prediction_results.csv`**: Kết quả dự đoán với các chỉ số đánh giá và so sánh giữa giá trị thực tế và dự đoán.
