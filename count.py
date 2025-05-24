# 统计健康的和染病的样本数，以调整权重
import os
import numpy as np
import rasterio
from collections import Counter

label_dir = "./data/my_test_data/annotations/labels"
class_pixel_counts = Counter()
id = 0

for filename in os.listdir(label_dir):
    if filename.endswith(".tif"):
        with rasterio.open(os.path.join(label_dir, filename)) as src:
            mask = src.read(1)  # 读取第一波段
            classes, counts = np.unique(mask, return_counts=True)
            for cls, cnt in zip(classes, counts):
                class_pixel_counts[cls] += cnt
    id += 1
    if (id % 500 == 0): print (id)

healthy_count, pwd_count = class_pixel_counts[0], class_pixel_counts[1]
total_count = healthy_count + pwd_count
print("Class counts: ", class_pixel_counts)
print("Healthy ratio & weights:", healthy_count / total_count, total_count * pwd_count / (total_count * healthy_count + total_count * pwd_count))
print("PWD ratio & weights:", pwd_count / total_count, total_count * healthy_count / (total_count * healthy_count + total_count * pwd_count))