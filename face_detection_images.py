import cv2
import argparse
import os
import numpy as np

def main(net, name, image, classes, save_path):
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    # print(f'detections = {detections} \ntype={type(detections)}\nshape={detections.shape}')
    label_str = ''
    # detections.shape[2] 有很多conf，但大部分都是0.1以下
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        # print(confidence)
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            # text = "{:.2f}%".format(confidence * 100)
            # y = startY - 10 if startY - 10 > 10 else startY + 10
            # cv2.rectangle(image, (startX, startY), (endX, endY),
            # (0, 0, 255), 2)
            # cv2.putText(image, text, (startX, y),
            # cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            # cv2.imshow('image', image)
            # cv2.waitKey(0)
            yolo_center_x = round((endX + startX) / 2 / w, 6)
            yolo_center_y = round((endY + startY) / 2 / h, 6)
            yolo_width = round((endX - startX) / w, 6)
            yolo_height = round((endY - startY) / h, 6)
            for j, c in enumerate(classes):
                if name.find(c) != -1:
                    label_str += f'{j} {yolo_center_x} {yolo_center_y} {yolo_width} {yolo_height}'
                    break
                else:
                    label_str=''
            print(label_str)
            label_dir = save_path + '/' + name + '.txt'
            f = open(label_dir, "w+")
            f.write(label_str)
            f.close()

def check_file_img(path):
    files = os.listdir(path)
    for i, file in enumerate(files):
        file = file.lower()
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.bmp'):
            continue
        else:
            print(f'{files[i]} is not a image')

if __name__ == '__main__':
    IMAGES_PATH = 'C:/Users/mark8/Downloads/FET/images'
    LABELS_SAVE_PATH = IMAGES_PATH[:IMAGES_PATH.find("images")] + "labels"
    CLASS_PATH = 'C:/Users/mark8/Downloads/FET/custom_classes.txt'
    # filename must be associated with classes name, i.e. bill_5566.jpg and bill
    NET = cv2.dnn.readNetFromCaffe(
                "C:/Users/mark8/Downloads/Face recognition/deploy.prototxt.txt",
                "C:/Users/mark8/Downloads/Face recognition/" +
                ("res10_300x300_ssd_iter_140000.caffemodel"))

    if not os.path.exists(LABELS_SAVE_PATH): 
        os.makedirs(LABELS_SAVE_PATH)

    check_file_img(IMAGES_PATH)
    files = os.listdir(IMAGES_PATH)
    f = open(CLASS_PATH,"r")
    classes = f.readlines()

    for i, c in enumerate(classes):
        if c.find("\n") != -1:
            classes[i] = c[:c.find("\n")]

    for i, file in enumerate(files):
        name = file[:file.find(".")]
        image = cv2.imread(IMAGES_PATH + "/" + file)
        # print(file)
        # print(classes)
        # print(file.find(classes[9]))
        main(NET, name, image, classes, LABELS_SAVE_PATH)
        print(f'{i}\n{file}\n')
    