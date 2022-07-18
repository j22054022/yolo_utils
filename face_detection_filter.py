import os
import face_recognition
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pypinyin import pinyin, lazy_pinyin, Style
from pypinyin.contrib.tone_convert import to_normal
import shutil

def change_file_to_txt(filename): 
    return ''.join(filename.split('.')[0])+'.txt'

def ch2en(name): 
    if name.find('-') > -1: 
        name = ''.join(name.split('-'))
    split_name_list = []
    order_buf = ''
    
    for item in pinyin(str(name)): 
        if ''.join(item).find('.') > -1: 
            split_name_list.append(''.join(item))
        else: 
            split_name_list.append(to_normal(''.join(item)).capitalize())
        
#     print(split_name_list)
    return (''.join(split_name_list))

def rename2ch(DIR_PATH): 
    file_list = os.listdir(DIR_PATH)
    for file in file_list: 
        new_name = ch2en(file)
        os.rename(DIR_PATH + '/' + file, DIR_PATH + '/' + new_name)
        print(f'{DIR_PATH}/{file} -> {DIR_PATH}/{new_name}')

def copy_img(DIR_PATH,current_file, NAME):
    shutil.copy(DIR_PATH + '/' + current_file, NAME + '_' + 'labels')

def isascii(s):
    """Check if the characters in string s are in ASCII, U+0-U+7F."""
    return len(s) == len(s.encode())




DATASET_PATH = '/home/jason/udn/udn_人臉辨識測試資料'
folder_list = os.listdir(DATASET_PATH)
CLASS = '0'

print(folder_list)
for x in folder_list: 
    
    DIR_PATH = DATASET_PATH + '/' + x
    NAME = ''.join(DIR_PATH.split('/')[-1])
    
    print(f"processing {x}")
    print(os.listdir(DIR_PATH))
    file_list = os.listdir(DIR_PATH)
    valid_count = 1
    invalid_count = 0

    if not os.path.exists(NAME + '_' + 'labels'): 
        os.makedirs(NAME + '_' + 'labels')

    for i in file_list: 
      # hidden file during uploading'
        if i == '.ipynb_checkpoints' or i.find('txt') > -1 or i.find('xlsx') > -1: 
            continue

        image = face_recognition.load_image_file(DIR_PATH + '/' + i )
        # face_locations format : {(y_min,x_max,y_max,x_min), (), ...}
        face_locations = face_recognition.face_locations(image)
  
        if not len(face_locations) == 1: 
            invalid_count+= 1
            print(f'invalid_count = {invalid_count} \n {i} has no label!')
            try: 
                os.remove(DIR_PATH + '/' + i)
            except: 
                print(f'could not rm file {i}')
            try: 
                os.remove(DIR_PATH + '/' + i.replace('.jpeg', '.txt'))
            except: 
                print(f'{i} has no corresponding label txt file!')
            continue
  
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        shape = image.shape
        label_str = ''
        # roi = image[face_locations[0][0]:face_locations[0][2], face_locations[0][3]:face_locations[0][1]]
        for j in face_locations: 
            y_min, x_max, y_max, x_min = j
            w = shape[1]
            h = shape[0]
            yolo_center_x = round((x_max + x_min) / 2 / w, 6)
            yolo_center_y = round((y_max + y_min) / 2 / h, 6)
            yolo_width = round((x_max - x_min) / w, 6)
            yolo_height = round((y_max - y_min) / h, 6)
    # cv2.circle(roi,(int((825-676)/2), int((1074-924)/2)), 1, (0, 255, 255), 3)

    # print(face_locations)
    # print(y_min, x_max, y_max, x_min)
    # print('class' + ' ' + str(yolo_center_x) + ' ' + str(yolo_center_y) + ' ' + str(yolo_width) + ' ' + str(yolo_height))
    # cv2_imshow(roi)
    # cv2_imshow(image)

        label_str += CLASS + ' ' + str(yolo_center_x) + ' ' + str(yolo_center_y) + ' ' + str(yolo_width) + ' ' + str(yolo_height) + '\n'

        print(f'valid_count = {valid_count} \n name = {i} \n face_locations = {face_locations} \n label_str = {label_str}')
        f = open(NAME + '_' + 'labels' + '/' + change_file_to_txt(i), 'w+')
        f.write(label_str)
        f.close()
        copy_img(DIR_PATH, i, NAME)
        valid_count += 1
    
    if isascii(NAME) == False: 
        rename2ch(os.getcwd() + '/' + NAME + '_' + 'labels')
    f = open('class.txt', 'a+')
    f.write(ch2en(NAME) + '\n')
    f.close()
    CLASS = str(int(CLASS) + 1)
