import argparse
import os
import glob
import pickle
import cv2
import json
import shutil


def create_yolo_strcuture():
  if os.path.exists("yolov5"):
    if not os.path.exists(os.path.join("yolov5", "train")):
      os.makedirs(os.path.join("yolov5", "train", "images"))
      os.makedirs(os.path.join("yolov5", "train", "labels"))
    if not os.path.exists(os.path.join("yolov5", "val")):
      os.makedirs(os.path.join("yolov5", "val", "images"))
      os.makedirs(os.path.join("yolov5", "val", "labels"))
  else:
    print("no yolov5 folder found")
    exit()


def generate_yolo(path, keyword, mode, class_index):
  create_yolo_strcuture()
  files = os.listdir(path)
  yolo_output_label = []
  error_path = []

  if not(mode == "train" or mode == "val"):
    print("mode can only be train or val")
    exit()

  for content in files:
    print(f"handling {os.path.join(path, content)}")
    if content.startswith("."):
      print(f"skipping {content}")
      continue
    if os.path.isdir(os.path.join(path, content)):
      try:
        text_file_path = glob.glob(os.path.join(path, content, "R/*R.txt"))[0]
        image_file_path = glob.glob(os.path.join(path, content, f"R/{keyword}"))[0]
        print(text_file_path, image_file_path)
      except Exception as e:
        error_path.append(os.path.join(path, content))
        print(f"error, please check {os.path.join(path, content)}")

    img = cv2.imread(image_file_path)
    img_name = image_file_path.split("/")[-1]
    img_w, img_h, _ = img.shape
    yolo_output_label = f"{class_index} {(345+(345+220))/2/img_w} {img_h/2/img_h} {220/img_w} {511/img_h}"

    with open(f"yolov5/{mode}/labels/{img_name.split('.')[0]}.txt", "w") as f:
      f.write(yolo_output_label)
    shutil.copy(image_file_path, os.path.join("yolov5", f"{mode}", "images"))
    
  print("error files:")
  for path in error_path:
    print(path)


if __name__ == "__main__":
  # parser = argparse.ArgumentParser()
  # parser.add_argument("--path", type=str, help="path of training folders")
  # parser.add_argument("--keyword", type=str, help="might be multiple images in subdirectory, giving keyword to select the right image.")
  # parser.add_argument("--recursive", help="if data are all store inside subdirectory", action="store_true")
  # parser.add_argument("--output", type=str)

  # args = parser.parse_args()

  generate_yolo("./train", "*RO.jpg", "train", 0)
  generate_yolo("./val", "*RO.jpg", "val", 0)
