import os
import cv2
import numpy as np
import random

# ref: https://reurl.cc/M07ENn

def random_noise(img_path,percentage):
    # 参数image：，noise_num：
    img = cv2.imread(img_path)
    img_noise = img
    # cv2.imshow("src", img)
    # print(img_noise.shape)
    rows, cols, chn = img_noise.shape
    noise_num = int(round((rows*cols)/100*percentage))
    # 加噪声
    for i in range(noise_num):
        x = np.random.randint(0, rows)#随机生成指定范围的整数
        y = np.random.randint(0, cols)
        img_noise[x, y, :] = 255
    return img_noise


def sp_noise(path,prob):
    '''
    添加椒盐噪声
    image:原始图片
    prob:噪声比例
    '''
    image = cv2.imread(path)
    # noised result image
    output = np.zeros(image.shape,np.uint8)
    # salt pepper noise image
    noise_out = np.zeros(image.shape,np.uint8)
    prob = prob/2
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob: 
                # pepper noise
                output[i][j] = 0
                noise_out[i][j] = 0
            elif rdn > thres:
                # salt noise
                output[i][j] = 255
                noise_out[i][j] = 255
            else:
                # no noise(stay original pixel)
                output[i][j] = image[i][j]
                noise_out[i][j] = 100
    return output


def gaussian_noise(path, mean=0, var=0.001):
    ''' 
        添加高斯噪声
        image:原始图像
        mean : 平均值
        var : 變異數，變異數越大，高斯分布越平坦，越容易出現超過[-1,1]分布的值
    '''
    image = cv2.imread(path)
    image = np.array(image/255, dtype=float)#将原始图像的像素值进行归一化，除以255使得像素值在0-1之间
    noise = np.random.normal(mean, var ** 0.5, image.shape)#创建一个平均值mean，變異數var呈高斯分布的图像矩阵(將變異數開根號轉為標準差standard deviation)
    output = image + noise#将噪声和原始图像进行相加得到加噪后的图像
    if output.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    output = np.clip(output, low_clip, 1.0)#clip函数将元素的大小限制在了low_clip和1之间了，小于的用low_clip代替，大于1的用1代替，有-1沒關係，因為後續會轉為unsign
    output = np.uint8(output*255)#解除归一化，乘以255将加噪后的图像的像素值恢复
    # cv2.imshow("gaussian", output)
    # cv2.waitKey(0)
    noise = np.uint8(noise*255)
    return [output, noise]

"""
def copy_txt(folder_path, oldname, newname):
    f = open(path, 'r')
    lines = f.read()
    new_f = open(path, "w+")
    new_f.write(lines)
    f.close()
    new_f.close()
"""

if __name__ == '__main__':
    IMAGE_FOLDER = 'C:/Users/mark8/Downloads/Face recognition/data_train'
    BUF_FOLDER = 'C:/Users/mark8/Downloads/Face recognition/data_buf'
    COUNTER = 0
    # if not os.path.exists('./image_augmentation'): 
    #     os.makedirs('./image_augmentation')
    #     os.makedirs('./image_augmentation/'+ 'images')
    #     os.makedirs('./image_augmentation/'+ 'labels')
    files = [file for file in os.listdir(IMAGE_FOLDER) if file.find('txt') == -1]
    # print(files)
    test_filename = 'Adele0121.jpg'
    for filename in files:
        COUNTER += 1
        print(f'{COUNTER}')
        if filename.find('tanya') != -1:
            print(f'skip tanya')
            continue
        print(filename+'...')
        f = open(IMAGE_FOLDER + '/' + filename[:filename.find('.')] + '.txt')
        lines = f.read()
        """
        # random noise 佔總像素3%與5%
        percentage = 3
        img_noise = random_noise(IMAGE_FOLDER+'/'+filename, percentage)
        save_name = 'aug_random_noise_'+str(percentage)+'%'+'_'+filename
        cv2.imwrite(BUF_FOLDER + '/' + save_name, img_noise)
        new_f = open(BUF_FOLDER + '/' + save_name[:save_name.find('.')] + '.txt', "w+")
        new_f.write(lines)
        new_f.close()

        percentage = 5
        img_noise = random_noise(IMAGE_FOLDER+'/'+filename, percentage)
        save_name = 'aug_random_noise_'+str(percentage)+'%'+'_'+filename
        cv2.imwrite(BUF_FOLDER + '/' + save_name, img_noise)
        new_f = open(BUF_FOLDER + '/' + save_name[:save_name.find('.')] + '.txt', "w+")
        new_f.write(lines)
        new_f.close()
        """

        """
        # 每個像素會是噪音的機率 使用0.1與0.2
        prob = 0.1
        img_noise = sp_noise(IMAGE_FOLDER+'/'+filename, prob)
        save_name = 'aug_sp_noise_'+str(int(prob*100))+'%'+'_'+filename
        cv2.imwrite(BUF_FOLDER + '/' + save_name, img_noise)
        new_f = open(BUF_FOLDER + '/' + save_name[:save_name.find('.')] + '.txt', "w+")
        new_f.write(lines)
        new_f.close()

        prob = 0.2
        img_noise = sp_noise(IMAGE_FOLDER+'/'+filename, prob)
        save_name = 'aug_sp_noise_'+str(int(prob*100))+'%'+'_'+filename
        cv2.imwrite(BUF_FOLDER + '/' + save_name, img_noise)
        new_f = open(BUF_FOLDER + '/' + save_name[:save_name.find('.')] + '.txt', "w+")
        new_f.write(lines)
        new_f.close()

        """
        # 高斯分布
        mean = 0
        var = 0.001
        img_noise, gauss_noise = gaussian_noise(IMAGE_FOLDER+'/'+filename)
        save_name = 'aug_gaussian_noise_'+ filename
        # cv2.imwrite('gaussian_noise_'+str(mean)+'_'+str(var) + '.jpg', gauss_noise)
        cv2.imwrite(BUF_FOLDER + '/' + save_name, img_noise)
        new_f = open(BUF_FOLDER + '/' + save_name[:save_name.find('.')] + '.txt', "w+")
        new_f.write(lines)
        new_f.close()
        
        f.close()