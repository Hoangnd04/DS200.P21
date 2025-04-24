import kagglehub
import shutil
import os

path = kagglehub.dataset_download("mirichoi0218/insurance")
print("Dataset đã được tải về:", path)

dest = "./data"
if not os.path.exists(dest):
    os.makedirs(dest)

shutil.copytree(path, dest, dirs_exist_ok=True)

print("Dataset đã được copy vào thư mục:", dest)
