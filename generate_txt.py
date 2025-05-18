"""
    生成train.txt、valid.txt、test.txt

"""

import os
import random


def split_dataset(input_folder, train_txt, val_txt, test_txt, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1):
    # 获取输入文件夹中所有图像文件
    all_images = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # 打乱文件列表
    random.shuffle(all_images)

    # 计算数据集大小
    total_images = len(all_images)
    train_size = int(train_ratio * total_images)
    val_size = int(val_ratio * total_images)
    test_size = total_images - train_size - val_size

    # 划分数据集
    train_images = all_images[:train_size]
    val_images = all_images[train_size:train_size + val_size]
    test_images = all_images[train_size + val_size:]

    # 将文件名写入训练集、验证集和测试集的txt文件
    with open(train_txt, 'w') as f:
        for image in train_images:
            f.write(image.split(".")[0] + '\n')

    with open(val_txt, 'w') as f:
        for image in val_images:
            f.write(image.split(".")[0] + '\n')

    with open(test_txt, 'w') as f:
        for image in test_images:
            f.write(image.split(".")[0] + '\n')

    print(
        f"Dataset split: {len(train_images)} for train, {len(val_images)} for validation, {len(test_images)} for test.")


# 输入文件夹路径和输出txt文件路径
input_folder = "D:\\RhodesIsland\\__ProgrammingWorks__\\Py\\model\\swin_transformer\\data\\my_test_data\\annotations\\labels" # 这里替换为你的输入文件夹路径
# input_folder = "F:\\segment\\Efficient-Transformer-main\\data\\my_test_data\\annotations\\labels" 
train_txt = 'data\\my_test_data\\annotations\\train.txt'  # 训练集文件
val_txt = 'data\\my_test_data\\annotations\\val.txt'  # 验证集文件
test_txt = 'data\\my_test_data\\annotations\\test.txt'  # 测试集文件

# 执行数据集划分
split_dataset(input_folder, train_txt, val_txt, test_txt)
