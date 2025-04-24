import numpy as np

def preprocess_data(row):
    """
    Tiền xử lý một dòng dữ liệu từ CSV dạng list string.

    Parameters:
    - row: List[str], ví dụ ["19", "female", "27.9", "0", "yes", "southwest", "16884.924"]

    Returns:
    - List[float]: features + label
    """
    
    if len(row) < 7:
        print(f"Incomplete row: {row}")
        return None 

    sex = 1 if row[1].strip().lower() == "male" else 0
    smoker = 1 if row[4].strip().lower() == "yes" else 0
    region_mapping = {'northeast': 0, 'southeast': 1, 'southwest': 2, 'northwest': 3}
    region_str = row[5].strip().lower()
    if region_str not in region_mapping:
        raise ValueError(f"Region không hợp lệ: {region_str}")
    region = region_mapping[region_str]
    features = [
        float(row[0]),   # age
        sex,
        float(row[2]),   # bmi
        int(row[3]),     # children
        smoker,
        region
    ]
    label = float(row[6])

    return features + [label]
