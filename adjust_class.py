import os

# abs path
DIR_PATH = ''
seek_class_index = ''
fixed_class_index = ''
file_list = os.listdir(DIR_PATH + '/')

for i in file_list: 
    if i.find('.txt') > -1: 
        print(i)
        f = open(i, 'r+')
        # f.truncate(0)
        f.seek(0)
        lines = f.read().splitlines()
        for data in lines:
            original = data.split(' ')
            data = data.split(' ')
            if data[0] == seek_class_index:
                data[0] = fixed_class_index
                data = ' '.join(data)
                f.write(f"{data}\n")
                print(f"{' '.join(original)} -> {data}")
            # print(data, type(data))
        f.close()