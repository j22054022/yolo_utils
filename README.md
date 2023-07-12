# yolo-utils

#### Required packages
`$ pip install numpy`
`$ pip install matplotlib`
`$ pip install opencv-python`

### Features
- adjust_class.py 修正特定label之class_index錯誤
> DIR_PATH = 欲修正存浪labels之資料夾路徑
> fixed_class_index = 欲修正的class_index
- convert_yolov4_train_txt.py 創建符合yolov4格式之train.txt
> DIR_PATH = 圖片當前位置之資料夾
> TRAIN_DIR = 訓練圖片儲存位置
- show_yolov4_result.py
> 將所有驗證圖片、show_yolov4_result.py、result.txt放置同一資料夾
> 所有label後的圖片會在pred資料夾
- seperate_train_val_data.py
> 先將所有資料放入名為train的資料夾後，讓所有資料依照8:1:1分為train, val ,test set
> python seperate_train_val_data.py
- structure_gen_csv.py
> 產生csv格式