import os
import socket
import joblib
import math
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from preprocess_transform import preprocess_data

def start_receiver(host='localhost', port=9999, batch_size=32, learning_rate=0.0001):
    model = SGDRegressor(max_iter=1, tol=1e-3, eta0=learning_rate, warm_start=True)
    X_train, y_train = [], []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Receiver listening at {host}:{port}...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                for line in data.strip().split('\n'):
                    if line:
                        row = line.strip().split(',')
                        row_data = preprocess_data(row)
                        X_train.append(row_data[:-1])
                        y_train.append(float(row_data[-1]))

                        if len(X_train) >= batch_size:
                            model.partial_fit(X_train, y_train)
                            mse = mean_squared_error(y_train, model.predict(X_train))
                            print(f"Updated model | Batch size: {batch_size} | MSE: {mse:.2f} | RMSE: {math.sqrt(mse):.2f} | Learning rate: {learning_rate:.5f}")
                            X_train, y_train = [], []

            os.makedirs('model', exist_ok=True)
            model_path = os.path.join('model', 'trained_model.pkl')
            joblib.dump(model, model_path)
            print(f"Model đã được lưu vào: {model_path}")

if __name__ == "__main__":
    start_receiver()
