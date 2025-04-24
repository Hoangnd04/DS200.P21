import socket
import time
import pandas as pd

data = pd.read_csv('./data/insurance.csv')
train_data = data[:-64]
test_data = data[-64:]

def start_sender(host='localhost', port=9999, batch_size=32, epochs=200):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to receiver!")
        print()

        for epoch in range(epochs):
            print(f"Starting Epoch {epoch+1}/{epochs}")

            shuffled_data = train_data.sample(frac=1).reset_index(drop=True)

            for i in range(0, len(shuffled_data), batch_size):
                batch = shuffled_data.iloc[i:i+batch_size]
                for row in batch.itertuples(index=False):
                    line = f"{row.age},{row.sex},{row.bmi},{row.children},{row.smoker},{row.region},{row.charges}"
                    s.sendall((line + '\n').encode())
                time.sleep(2)

if __name__ == "__main__":
    start_sender()
