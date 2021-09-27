import os
import glob
import pandas as pd
import numpy as np

os.chdir(r'./')
myFiles = glob.glob('*.txt')
width = 2064
height = 1185
image_id = "pepegrillo"
final_df = []
for item in myFiles:

    with open(item, 'rt') as fd:
        lines = fd.read()
        lines = lines.split("\n")
        for line in lines:
            row = []
            bbox_temp = []

            print(line)
            splited = line.split()
            row.append(image_id)
            row.append(width)
            row.append(height)
            try:
                x_center = float(splited[1])*width
                y_center = float(splited[2])*height
                c = float(splited[3])*width
                d = float(splited[4])*height
                a = x_center - (c/2)
                b = y_center - (d/2)
                bbox_temp.append(a)
                bbox_temp.append(b)
                bbox_temp.append(c)
                bbox_temp.append(d)
                row.append(bbox_temp)
                final_df.append(row)
            except Exception as e:
                print(e)
            print(final_df)
df = pd.DataFrame(final_df, columns=[
    'image_id', 'width', 'height', 'bbox'])
df.to_csv("saved.csv", index=False)
