import os

# abs path
DIR_PATH = ''
fixed_class_index = ''
file_list = os.listdir(DIR_PATH + '/')

for i in file_list: 
    if i.find('.txt') > -1: 
        print(i)
        f = open(i, 'r+')
        data = f.readline()
        f.truncate(0)
        f.seek(0)
        data = data.split(' ')
        data[0] = fixed_class_index
        data = ' '.join(data)
        f.write(data)
        # print(data, type(data))
        f.close()