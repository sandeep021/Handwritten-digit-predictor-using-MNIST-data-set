import os
import numpy as np
import cv2
from PIL import ImageGrab
import time
i=1
img=cv2.imread("image.png")
cv2.imshow("hello",img)
img_np=np.array(img)
print(img_np)

#def openfile():
    
