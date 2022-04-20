import cv2
import argparse
import os
import numpy as np

def video_detect():
    COUNTER = 0
    while capture.isOpened(): 
        success, frame = capture.read()
        if not success: 
            print('Ignoring empty camera frame')
            break
        image = frame
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
                text = "{:.2f}%".format(confidence * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                # cv2.rectangle(image, (startX, startY), (endX, endY),
                # (0, 0, 255), 2)
                # cv2.putText(image, text, (startX, y),
                # cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                yolo_center_x = round((endX + startX) / 2 / w, 6)
                yolo_center_y = round((endY + startY) / 2 / h, 6)
                yolo_width = round((endX - startX) / w, 6)
                yolo_height = round((endY - startY) / h, 6)
                label_str += f'10 {yolo_center_x} {yolo_center_y} {yolo_width} {yolo_height}'
                print(label_str)
                img_dir = os.path.join('test_video_capture/' + VIDEO_NAME + '/' + 'images', VIDEO_NAME + '-'  + str(COUNTER) + '.jpg')
                cv2.imwrite(img_dir, frame)
                label_dir = os.path.join('test_video_capture/' + VIDEO_NAME + '/' + 'labels' + '/' + VIDEO_NAME + '-'  + str(COUNTER) + '.txt')
                f = open(label_dir, "w+")
                f.write(label_str)
                f.close()
        COUNTER += 1

if __name__ == '__main__':
    VIDEO_PATH = 'C:/Users/mark8/Downloads/tanya_20220413.mp4'
    VIDEO_NAME = 'tanya_20220413.mp4'

    capture = cv2.VideoCapture(VIDEO_PATH)
    net = cv2.dnn.readNetFromCaffe(
                "C:/Users/mark8/Downloads/Face recognition/deploy.prototxt.txt",
                "C:/Users/mark8/Downloads/Face recognition/" +
                ("res10_300x300_ssd_iter_140000.caffemodel"))

    if not os.path.exists('./test_video_capture/'+ VIDEO_NAME): 
        os.makedirs('./test_video_capture/'+ VIDEO_NAME)
        os.makedirs('./test_video_capture/'+ VIDEO_NAME  + '/' + 'images')
        os.makedirs('./test_video_capture/'+ VIDEO_NAME + '/' + 'labels')

    video_detect()