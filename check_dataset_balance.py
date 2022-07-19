import os

train_path = "F:/FET_Face_recognition_data/Face recognition/new_data_train"
index_count = [0]*80

for file in os.listdir(train_path):
    if file.endswith("txt"):
        with open(f"{train_path}/{file}", "r+") as f:
            for line in f:
                index = line.split(" ")[0]
                index_count[int(index)] += 1

for i, count in enumerate(index_count):
    print(f"index {i}: {count}")

