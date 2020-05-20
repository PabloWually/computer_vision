import os
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
from scipy import ndimage
import skimage.color as sc
import numpy as np

def edge_sobel(image):
    image = sc.rgb2gray(image) # Convert color image to gray scale
    dx = ndimage.sobel(image, 1)  # horizontal derivative
    dy = ndimage.sobel(image, 0)  # vertical derivative
    mag = np.hypot(dx, dy)  # magnitude
    mag *= 255.0 / np.amax(mag)  # normalize (Q&D)
    mag = mag.astype(np.uint8)
    return mag

# Load the image from the source file
#C:/Users/User/Desktop
#C:/Repositories/Image_Analysis/data/voc/plane
image_file = "C:/Users/User/Documents/otraCompu/FO/DCIM/100CONCI/DSC_1348.jpg"
image = Image.open(image_file)
edges_image = image.filter(ImageFilter.FIND_EDGES)

""" #


# Display it
fig = plt.figure(figsize=(16, 12))

# Plot original image
a=fig.add_subplot(1, 2, 1)
image_plot_1 = plt.imshow(image)
a.set_title("Original")

# Plot filtered image
a=fig.add_subplot(1, 2, 2)
image_plot_2 = plt.imshow(edges_image)
a.set_title("Edges") """

sobel_image = edge_sobel(np.array(image))

# Display it
fig = plt.figure(figsize=(16, 12))

# Plot original image
a=fig.add_subplot(1, 3, 1)
image_plot_1 = plt.imshow(image)
a.set_title("Original")

# Plot PIL FIND_EDGES image
a=fig.add_subplot(1, 3, 2)
image_plot_2 = plt.imshow(edges_image)
a.set_title("Edges")

# Plot Sobel image
a=fig.add_subplot(1, 3, 3)
image_plot_2 = plt.imshow(sobel_image, cmap="gray") # Need to use a gray color map as we converted this to a grayscale image
a.set_title("Sobel")

plt.show()