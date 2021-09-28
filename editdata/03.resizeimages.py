import os
import random
import cv2

trainimagenes = list(os.listdir("./plaga/train/"))
testimagenes = list(os.listdir("./plaga/test/"))
print("resize TRAIN")
for img in trainimagenes:
    pathimg = './plaga/train/' + img
    imagen = cv2.imread(pathimg, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ', imagen.shape)
    scale_percent = 25.6  # percent of original size
    width = int(imagen.shape[1] * scale_percent / 100)
    height = int(imagen.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(imagen, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    cv2.imwrite(pathimg, resized)
print("resize TEST")
for img in testimagenes:
    pathimg = './plaga/test/' + img
    imagen = cv2.imread(pathimg, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ', imagen.shape)
    scale_percent = 30  # percent of original size
    width = int(imagen.shape[1] * scale_percent / 100)
    height = int(imagen.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(imagen, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    cv2.imwrite(pathimg, resized)
