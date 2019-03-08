import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from os import listdir

def show_image(img):
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()

def rotate(img):
    rows, cols = img.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), -90, 1)
    return  cv2.warpAffine(img, M, (cols, rows))

images_dir = os.path.join("../images/")
for image in listdir(images_dir):
    img = cv2.imread(os.path.join(images_dir, image), 0)
    img = rotate(img)
    img = cv2.Canny(img, 100, 200)
    show_image(img)

