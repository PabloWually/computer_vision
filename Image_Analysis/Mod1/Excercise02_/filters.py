import os
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

# Load the image from the source file
image_file = "C:/Repositories/Image_Analysis/data/voc/plane/002279.jpg"
image = Image.open(image_file)

""" #Common Filters 
blurred_image = image.filter(ImageFilter.BLUR)
sharpened_image = image.filter(ImageFilter.SHARPEN)

# Display it
fig = plt.figure(figsize=(16, 12))

# Plot original image
a=fig.add_subplot(1, 3, 1)
image_plot_1 = plt.imshow(image)
a.set_title("Original")

# Plot blurred image
a=fig.add_subplot(1, 3, 2)
image_plot_2 = plt.imshow(blurred_image)
a.set_title("Blurred")

# Plot sharpened image
a=fig.add_subplot(1, 3, 3)
image_plot_3 = plt.imshow(sharpened_image)
a.set_title("Sharpened") """

#Cutom filters
my_kernel = (100, 150, -50,
             -100, 20, -100,
            -10, 10, 20)

filtered_image = image.filter(ImageFilter.Kernel((3,3), my_kernel))

# Display it
fig = plt.figure(figsize=(16, 12))

# Plot original image
a=fig.add_subplot(1, 2, 1)
image_plot_1 = plt.imshow(image)
a.set_title("Original")

# Plot filtered image
a=fig.add_subplot(1, 2, 2)
image_plot_2 = plt.imshow(filtered_image)
a.set_title("Custom Filter")

plt.show()