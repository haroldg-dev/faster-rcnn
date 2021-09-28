import os
import random
import shutil
imagenes = list(os.listdir("./fotodeplaga"))
random.shuffle(imagenes)
i = 0
os.makedirs("./plaga/train/")
os.mkdir("./plaga/test/")
while i < 77:
    if (i < 50):
        imagen = "./fotodeplaga/" + imagenes[i]
        newname = "./plaga/train/" + imagenes[i]
        shutil.copyfile(imagen, newname)
    if (i > 50 and i < 77):
        imagen = "./fotodeplaga/" + imagenes[i]
        newname = "./plaga/test/" + imagenes[i]
        shutil.copyfile(imagen, newname)
    i = i + 1

datafinal = list(os.listdir("./plaga/train"))
print(datafinal)
datafinal = list(os.listdir("./plaga/test"))
print(datafinal)
