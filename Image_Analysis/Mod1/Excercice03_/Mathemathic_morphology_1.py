import os
import numpy as np
from skimage import morphology as sk_mm
from skimage import io as sk_io
import skimage.color as sk_col
from matplotlib import pyplot as plt

# Load the image from the source file
#C:/Repositories/Image_Analysis/data/voc/plane/008372.jpg
image_file = "C:/Repositories/Image_Analysis/data/voc/plane/008372.jpg"
image = sk_io.imread(image_file)

# Convert to grayscale so we only have one channel
bw_image = sk_col.rgb2gray(image)

# Apply operations
eroded_image = sk_mm.erosion(bw_image)
dilated_image = sk_mm.dilation(bw_image)
closed_image = sk_mm.closing(bw_image)
opened_image = sk_mm.opening(bw_image)

# Display it
fig = plt.figure(figsize=(20,20))

# Plot original image
a=fig.add_subplot(5, 1, 1)
plt.imshow(bw_image, cmap="gray")
a.set_title("Original")

# Plot eroded image
a=fig.add_subplot(5, 1, 2)
plt.imshow(eroded_image, cmap="gray")
a.set_title("Eroded")

# Plot dilated image
a=fig.add_subplot(5, 1, 3)
plt.imshow(dilated_image, cmap="gray")
a.set_title("Dilated")

# Plot closed image
a=fig.add_subplot(5, 1, 4)
plt.imshow(closed_image, cmap="gray")
a.set_title("Closed")

# Plot opened image
a=fig.add_subplot(5, 1, 5)
plt.imshow(opened_image, cmap="gray")
a.set_title("Opened")

plt.show()