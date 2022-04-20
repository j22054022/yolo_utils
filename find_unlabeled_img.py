import os


# this path contain both labels and images just like yolov4 folder
DATA_PATH = 'C:/Users/mark8/Downloads/FET_val_full/data_val'
REMOVE_FILE = False

files = os.listdir(DATA_PATH)
img_files = []

for file in files:
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.bmp'):
        img_files.append(file)

for img in img_files:
    found = False
    for file in files:
        if img[:img.find('.')] + '.txt' == file:
            found = True
            break
    if found:
        continue
    else:
        print(f'{img} has no label file')
        if REMOVE_FILE:
            os.remove(DATA_PATH + '/' + img)
            print(f'{img} removed')