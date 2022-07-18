import os

count = 0
total_count = 0

for folder in os.listdir(os.getcwd()):
    if folder.endswith("labels"):

        files = sorted(os.listdir(folder))
        print(files)
        num_val = int(len(files)/2/100*20)
        print(num_val)
        if not os.path.exists("val"):
            os.makedirs("val")
    
        count = 0
        for i in range(num_val):
            os.system(f"mv {folder}/{files[-1]} val/")
            os.system(f"mv {folder}/{files[-2]} val/")
            print(f"mv {folder}/{files[-1]} val/")
            print(f"mv {folder}/{files[-2]} val/")
            files.pop()
            files.pop()
            count += 1
            total_count += 1
            # pass
        
        print(f"{folder} made {count} valsets")

print(f"total made {total_count} valsets")
