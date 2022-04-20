import os
import shutil

IMAGE_FOLDER_PATH = 'C:/Users/mark8/Documents/GitHub/test_video_capture/tanya_20220413.mp4/images'
LABEL_FOLDER_PATH = 'C:/Users/mark8/Documents/GitHub/test_video_capture/tanya_20220413.mp4/labels'
SAVED_FOLDER_PATH = 'C:/Users/mark8/Downloads/Face recognition/tanya_buf'

files = os.listdir(IMAGE_FOLDER_PATH)

# 每16張拿一張

for i in range(0, len(files), 15):
    print(files[i])
    shutil.copy(IMAGE_FOLDER_PATH+'/'+files[i], SAVED_FOLDER_PATH+'/'+files[i])
    shutil.copy(LABEL_FOLDER_PATH+'/'+files[i][:files[i].find(".jpg")]+'.txt',SAVED_FOLDER_PATH+'/'+files[i][:files[i].find(".jpg")]+'.txt')