import os
import shutil

IMPORT_DIR = "train"
EXPORT_DIR = "train_separated"
NAMES = "../new_face.names"

classes = []
filenames = [filename for filename in os.listdir(IMPORT_DIR) if filename.endswith(".txt")]

with open(NAMES, "r") as f:
    classes = [name.strip("\n") for name in f.readlines()]

print(f"classes: {classes}")

if not os.path.exists(EXPORT_DIR):
    os.mkdir(EXPORT_DIR)
    for cls in classes:
        try:
            os.mkdir(os.path.join(EXPORT_DIR, cls))
        except Exception as e:
            print(e)

for filename in filenames:
    with open(os.path.join(IMPORT_DIR, filename), "r") as f:
        labels = [l.strip("\n") for l in f.readlines()]
        for label in labels:
            cls_index,_,_,_,_ = label.split(" ")
            if os.path.exists(f.name.split(".")[0]+".jpg"):
                print(f"copying {f.name} image -> {os.path.join(EXPORT_DIR, classes[int(cls_index)])}")
                shutil.copy(f.name.split(".")[0]+".jpg", os.path.join(EXPORT_DIR, classes[int(cls_index)]))
            else:
                print(f"{f.name} image not exists")


