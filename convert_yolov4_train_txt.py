import os

DIR_PATH = ''
file_list = os.listdir(os.getcwd() + '/' + DIR_PATH)
TRAIN_DIR = '/workspace/Face_detection/data_train/'
train_str=''

for i in file_list: 
    if i.find('.py') > -1 or i.find('.txt') > -1: 
        continue
    train_str += TRAIN_DIR + i + '\n'

print(train_str)

f = open('train.txt', 'w+')
f.write(train_str)
f.close()