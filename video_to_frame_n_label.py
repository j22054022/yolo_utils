# import torch
import cv2
import numpy as np
import zipfile
import os

def video2image(video_path, output_path):
    # output_path = "/home/datasets/image/"
    if os.path.exists(video_path) and os.path.exists(output_path):
        print(f"video detected {video_path}")
        vname = video_path.split("/")[-1].split(".")[0]
        cap = cv2.VideoCapture(video_path)
        count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"writing frame {count}")
                cv2.imwrite(os.path.join(output_path, f"{vname}_frame_{str(count).zfill(6)}.jpg"), frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
                count = count + 1
            else:
                print("end of capturing")
                print("existing...")
                break
    else:
        print("no video detected")
                
                
def check_existing_labels(zip_path, output_path):
    # output_path = "/home/datasets/label/"
    if os.path.exists(zip_path):
        print(f"zipped label file detected {zip_path}")
        zname = zip_path.split("/")[-1].split(".")[0]
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            # it will recursivly getting a list of files in zip file
            # print(zip_ref.namelist())
            for filename in zip_ref.namelist():
                if filename.endswith(".txt") and filename != "train.txt":
                    # print(filename)
                    zip_ref.extract(filename, output_path)
                    for root, dirs, files in os.walk(output_path):
                        # print(list(os.walk(output_path)))
                        filename = filename.split("/")[-1]
                        if filename in files:
                            # the path which unzipped file's actual location
                            target_path = os.path.join(root, filename)
                            print(f"move {target_path} -> {os.path.join(output_path, zname+'_'+filename)}")
                            os.rename(target_path, os.path.join(output_path, zname+"_"+filename))
    else:
        print("no zip file detected")
                    

if __name__ == "__main__":
    
    # vdir = "/home/tape/data/train/videos"
    vdir = "/home/tape/data/val/videos"
    vfiles = [x for x in os.listdir(vdir) if x.endswith("mp4")]
    print(vfiles)
    
    for video_path in vfiles:
        video2image(os.path.join(vdir, video_path), "/home/tape/datasets/val/images")
    
    
    ldir = "/home/tape/data/train/labels"
    # ldir = "/home/tape/data/val/labels"
    lfiles = [x for x in os.listdir(ldir) if x.endswith("zip")]
    print(lfiles)
    # check_existing_labels("/home/data/labels/01_ch0_2023021514+1.zip", "/home/datasets/labels")
    """
    for zip_path in lfiles:
        check_existing_labels(os.path.join(ldir, zip_path), "/home/tape/datasets/val/labels/")
    """
            
