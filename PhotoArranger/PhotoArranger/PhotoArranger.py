import numpy as np
import os
import matplotlib.pylab as plt
import math
import cv2
from PIL import Image
import imageio

small_images = np.load("image_comp.npy")
(num_images, height, width, depth) = small_images.shape

full_x = width*4
full_y = height*6

scale = 1

largeImageStartX = 0
largeImageStartY = 0

final_image = np.zeros((full_y, full_x, 3), dtype=int)

for image in small_images: #stores the index of the closest picture to the original
    print(largeImageStartX, ",", largeImageStartY)
    for i in range(round(height * scale)):
        for j in range(round(width * scale)):
            final_image[largeImageStartY + i][largeImageStartX + j] = image[i][j]
    if largeImageStartX == full_x - round((width * scale)):
        largeImageStartX = 0
        largeImageStartY = round(largeImageStartY + (height * scale))
    else:
        largeImageStartX = round(largeImageStartX + (width * scale))


imageio.imwrite('mosaic4.jpg', final_image)