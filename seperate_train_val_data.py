import os

count = 0
total_count = 0

for folder in os.listdir(os.getcwd()):
    if folder.endswith("train"):

        files = sorted(os.listdir(folder))
        print(files)
        half_iter = int(len(files)//2//100*20)
        print(half_iter)
        if not os.path.exists("val"):
            os.makedirs("val")
        if not os.path.exists("test"):
            os.makedirs("test")

        val_count = 0
        test_count = 0
        for i in range(half_iter*2):
            if i <= half_iter:
                os.system(f"mv {folder}/{files[-1]} val/")
                # os.system(f"mv {folder}/{files[-2]} val/")
                print(f"mv {folder}/{files[-1]} val/")
                # print(f"mv {folder}/{files[-2]} val/")
                val_count += 1
            else:
                os.system(f"mv {folder}/{files[-1]} test/")
                # os.system(f"mv {folder}/{files[-2]} test/")
                print(f"mv {folder}/{files[-1]} test/")
                # print(f"mv {folder}/{files[-2]} test/")
                test_count += 1
            files.pop()
            # files.pop()
            total_count += 1
            i += 1
            # pass

        # print(f"{folder} made {count/2} valsets")

print(f"total made {val_count} valSets")
print(f"total made {test_count} testSets")