import csv
import os
import glob


def generate_csv_annotation(path, keyword, mode):
  if not (mode == "train" or mode == "val"):
    print("mode can only be train or val")
    exit()

  with open(f"drfoot_{mode}.csv" ,"w") as f:
    writer = csv.writer(f)
    files = os.listdir(path)

    for content in files:
      print(f"handling {os.path.join(path, content)}")
      if content.startswith("."):
        print(f"skipping {content}")
        continue
      if os.path.isdir(os.path.join(path, content)):
        try:
          text_file_path = glob.glob(os.path.join(path, content, "*/*.txt"))
          image_file_path = glob.glob(os.path.join(path, content, f"*/{keyword}"))
          print(text_file_path, image_file_path)
        except Exception as e:
          print(f"error {os.path.join(path, content)}")

      for i, text_file in enumerate(text_file_path):
        with open(text_file) as ff:
          s = ff.read()
          s_split = s.split(",")
          x1 = float(s_split[0])
          y1 = float(s_split[1])
          x5 = float(s_split[-2])
          y5 = float(s_split[-1])
          row = [image_file_path[i].split("/")[-1], x1, y1, x5, y5]
          writer.writerow(row)


if __name__ == "__main__":
  generate_csv_annotation("./train", "*O.jpg", "train")
  generate_csv_annotation("./val", "*O.jpg", "val")
