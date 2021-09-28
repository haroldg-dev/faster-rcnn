import os
import glob
import pandas as pd
import numpy as np
import cv2

os.chdir(r"./")
myFiles = glob.glob("*.txt")
# imgs = os.path.join('/home/francoxr/Downloads/kevindatos/', '*.jpg')
imgs = os.listdir('/home/francoxr/Downloads/kevindatos/')
jpgs = []
txts = []
for file in imgs:
    if file.endswith('.jpg'):
        jpgs.append(file)
    else:
        txts.append(file)
print(jpgs)
print(txts)

final_df = []

for img in jpgs:
    path = '/home/francoxr/Downloads/kevindatos/'+ img
    print(path)
    photo = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    dimensions = photo.shape
    height = photo.shape[0]
    width = photo.shape[1]
    name_img = img
    image_id = "sickalfa"
    item = path.replace('.jpg','.txt')    
    with open(item, "rt") as fd:
        lines = fd.read()
        lines = lines.split("\n")
        for line in lines:
            row = []
            bbox_temp = []

            print(line)
            splited = line.split()
            row.append(name_img)
            row.append(image_id)
            row.append(width)
            row.append(height)
            try:
                x_center = float(splited[1]) * width
                y_center = float(splited[2]) * height
                c = float(splited[3]) * width
                d = float(splited[4]) * height
                a = x_center - (c / 2)
                b = y_center - (d / 2)
                bbox_temp.append(a)
                bbox_temp.append(b)
                bbox_temp.append(c)
                bbox_temp.append(d)
                row.append(bbox_temp)
                final_df.append(row)
            except Exception as e:
                print(e)
                print(final_df)
df = pd.DataFrame(final_df, columns=["name_img", "image_id", "width", "height", "bbox"])
df.to_csv("saved.csv", index=False)
