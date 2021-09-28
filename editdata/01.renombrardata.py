import shutil
import os
import random


imagenes = list(os.listdir("./fotodeplaga"))
i = 0
for imagen in imagenes:
    # imagen = 20210819_080432.jpg
    imagen = "./fotodeplaga/" + imagen
    newname = "./fotodeplaga/" + str(i) + ".jpg"
    os.rename(imagen, newname)
    i = i + 1

""" a = [1, 2, 3, 4, 5, 6, 7, 8]
for numero in a:
    numero = numero + 1
    print(numero) """
