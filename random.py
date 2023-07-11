from PIL import Image
import numpy as np
from numpy import asarray
import os
from os import listdir

folder= "/content/train/cumulus"

img = Image.open('/content/train/cumulus/stratocumulus.jpg')
imageToMatrice = np.asarray(img)
data = asarray(img)
print(imageToMatrice.shape)


for i in data:
  #print(i)
  np.savetxt("foo.csv", i, delimiter=",")
print(i)
