""" 
You can also flip images. One way to do this is to take advantage of the fact that an image is a Numpy array,
and Numpy has a flip method: 
"""

import numpy as np 
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mp_image
import cv2

src_folder = "C:/Repositories/Image_Analysis/data/voc"
cv_image = cv2.imread(os.path.join(src_folder,"train", "000712.jpg"))
cv_image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB) #Imagen con correccion

upended_cv_image_rgb = np.flip(cv_image_rgb, axis=0)
mirrored_cv_image_rgb = np.flip(cv_image_rgb, axis=1)

fig = plt.figure(figsize = (12, 12))

a = fig.add_subplot(1,3,1)
image_plot_1 = plt.imshow(cv_image_rgb)
a.set_title("Original")

a = fig.add_subplot(1, 3, 3)
image_plot_3 = plt.imshow(upended_cv_image_rgb)
a.set_title("Flipped Vertically")

a = fig.add_subplot(1, 3, 2)
image_plot_2 = plt.imshow(mirrored_cv_image_rgb)
a.set_title("Flipped Vertically")

plt.show()