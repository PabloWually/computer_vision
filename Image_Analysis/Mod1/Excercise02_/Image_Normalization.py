import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mp_image
from skimage import exposure

# Load the image from the source file
image_file = "C:/Repositories/Image_Analysis/data/voc/automobile/000142.jpg"
image = mp_image.imread(image_file)

""" #Display histogram usin ravel to flatten the 3 dimentions
plt.hist(image.ravel()) """

""" # Display the statistics of an image is as a cumulative distribution function (CDF) plot
plt.hist(image.ravel(), bins=255, cumulative=True) """

""" """ #Manipulating the contrast whit diferent Techniques
# Contrast stretching
p2 = np.percentile(image, 2)
p98 = np.percentile(image, 98)
image_ct = exposure.rescale_intensity(image, in_range=(p2, p98))

# Histogram Equalization
image_eq = exposure.equalize_hist(image)

# Show the images
fig = plt.figure(figsize=(20, 12))

# Subplot for original image
a=fig.add_subplot(3,3,1)
imgplot = plt.imshow(image)
a.set_title('Original')

# Subplot for contrast stretched image
a=fig.add_subplot(3,3,2)
imgplot = plt.imshow(image_ct)
a.set_title('Contrast Stretched')

# Subplot for equalized image
a=fig.add_subplot(3,3,3)
imgplot = plt.imshow(image_eq)
a.set_title('Histogram Equalized')

# Subplots for histograms
a=fig.add_subplot(3,3,4)
imgplot = plt.hist(image.ravel())

a=fig.add_subplot(3,3,5)
imgplot = plt.hist(image_ct.ravel())

a=fig.add_subplot(3,3,6)
imgplot = plt.hist(image_eq.ravel())

# Subplots for CDFs

a=fig.add_subplot(3,3,7)
imgplot = plt.hist(image.ravel(), bins=255, cumulative=True)

a=fig.add_subplot(3,3,8)
imgplot = plt.hist(image_ct.ravel(), bins=255, cumulative=True)

a=fig.add_subplot(3,3,9)
imgplot = plt.hist(image_eq.ravel(), bins=255, cumulative=True)

plt.show()
