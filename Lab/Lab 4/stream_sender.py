import socket
import time
import pandas as pd

data = pd.read_csv('./data/insurance.csv')
train_data = data[:-64]
test_data = data[-64:]

def is_valid_row(row):
    if len(row) != 7:
        return False
    
    try:
        float(row[0])  # age
        float(row[2])  # bmi
        int(row[3])    # children
        float(row[6])  # charges

    except ValueError:
        return False
    
    if row[1].lower() not in ["male", "female"]:
        return False
    if row[4].lower() not in ["yes", "no"]:
        return False
    region_mapping = ['northeast', 'southeast', 'southwest', 'northwest']
    if row[5].lower() not in region_mapping:
        return False
    
    return True

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
                    row_data = [row.age, row.sex, row.bmi, row.children, row.smoker, row.region, row.charges]
                    if not is_valid_row(row_data):
                        print(f"Skipping invalid row: {row_data}")
                        continue
                    line = f"{row.age},{row.sex},{row.bmi},{row.children},{row.smoker},{row.region},{row.charges}"
                    s.sendall((line + '\n').encode())
                time.sleep(2)

if __name__ == "__main__":
    start_sender()
