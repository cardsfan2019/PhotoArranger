import numpy as np
import os
import matplotlib.pylab as plt
from PIL import Image
import cv2
import numpy as np
NUM_IMAGES = 24

small_image_names = os.listdir("images/")

small_images = []

i = 0

def rename():
    global i
    for image in small_image_names:
        os.rename("images/" + image, "images/image_" + str(i) + ".JPG")
        print(i)
        i = i + 1


#rename()

small_image_names = os.listdir("images/")
i = 0
for image in small_image_names:
    if (i < NUM_IMAGES):
        temp = Image.open("images/" + image)
        temp = np.asarray(temp)
        
        if len(temp.shape) == 2:
            temp = cv2.cvtColor(temp, cv2.COLOR_GRAY2RGB)
        final = cv2.resize(temp, (1000, 1000))
        small_images.append(final)
        print(i)
    i = i + 1

new_images = np.asarray(small_images)

np.save("image_comp", small_images)