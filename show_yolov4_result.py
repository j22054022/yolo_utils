import os
import cv2
import numpy as np
import random

BRIGHT_COLOR = ((255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255))

def get_filename(s): 
    buf_s = ''
    for i in range (s.find('.jpg')+3, 0, -1): 
        if s[i] == '/': 
            break
        # print(s[i])
        buf_s += s[i]
    return(buf_s[::-1])

def get_bbox(s): 
    list_s = s.split('\t')
    class_name = list_s[0][0:list_s[0].find(':')]
    conf = int(list_s[0][list_s[0].find(':')+1:list_s[0].find('%')]) / 100
    left_x = list_s[1][list_s[1].find('x:')+1+1:list_s[1].find('top')]
    top_y = list_s[1][list_s[1].find('y:')+1+1:list_s[1].find('wid')]
    width = list_s[1][list_s[1].find('h:')+1+1:list_s[1].find('hei')]
    height = list_s[1][list_s[1].find('t:')+1+1:list_s[1].find(')')]
    # 因轉int，故就算以上方法會吃到空白鍵依舊不影響
    return [class_name, conf, (int(left_x), int(top_y)), (int(left_x) + int(width), int(top_y) + int(height))]

def check_img(filename, img): 
    cv2.imshow('pred_' + filename, img)
    cv2.waitKey(0)

f = open(os.path.join('result.txt'), 'r')

if not os.path.exists("pred"):
    os.mkdir("pred")


s = f.read()
list_s = s.split('\n')
print(list_s)

bbox_list = []
filename = ''

for readline in list_s:
    print(readline)
    if readline.find('.jpg') > -1:
        filename = get_filename(readline)
        print(filename)
    elif readline.find('%') > -1: 
        bbox_list.append(get_bbox(readline))
        print(get_bbox(readline))
    elif readline.find('ImagePath'): 
        if len(bbox_list) > 0:
            img = cv2.imread(filename)
            imageWidth = img.shape[1]
            imageHeight = img.shape[0]
            fontScale = min(imageWidth,imageHeight)*0.000468 + 0.295
            thickness = 2
            if fontScale < 0.5: 
                thickness = 1
            print(fontScale)
            # img = cv2.resize(img, (416, 416))
            for bbox in bbox_list:            
                print(bbox)
                class_name, conf, top_left, bottom_right = bbox
                color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                cv2.rectangle(img, top_left, bottom_right, color,2)
                # cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
                cv2.putText(img, class_name + ' ' + str(conf), (top_left[0],top_left[1]-5), cv2.FONT_HERSHEY_SIMPLEX, fontScale, color,thickness)

            # img = cv2.resize(img, (800, 800))
            # check_img(filename, img)
            imgdir = os.path.join('pred', 'pred_' + filename)
            cv2.imwrite(imgdir, img)
            bbox_list = []
            filename = ''
f.close()
