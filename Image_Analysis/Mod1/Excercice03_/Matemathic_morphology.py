import numpy as np
from skimage import morphology as sk_mm
from matplotlib import pyplot as plt

square = np.array([[0, 0, 0, 0, 0],
                   [0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0],
                   [0, 0, 0, 0, 0]], dtype=np.uint8)

struct_element = sk_mm.selem.diamond(1)

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" # Apply erosion
eroded_square = sk_mm.erosion(square, struct_element)

fig = plt.figure(figsize=(6, 6))
# Plot original image
a=fig.add_subplot(1, 2, 1)
plt.imshow(square, cmap="binary")
a.set_title("Original")

# Plot eroded image
a=fig.add_subplot(1, 2, 2)
plt.imshow(eroded_square, cmap="binary")
a.set_title("Eroded") """
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" #Apply dilation
dilated_square = sk_mm.dilation(square, struct_element)

# Display it
fig = plt.figure(figsize=(6, 6))

# Plot original image
a=fig.add_subplot(1, 2, 1)
plt.imshow(square, cmap="binary")
a.set_title("Original")

# Plot dilated image
a=fig.add_subplot(1, 2, 2)
plt.imshow(dilated_square, cmap="binary")
a.set_title("Dilated") """
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Apply closing and opening
closed_square = sk_mm.closing(square, struct_element)
opened_square = sk_mm.opening(square, struct_element)

# Display it
fig = plt.figure(figsize=(9, 6))

# Plot original image
a=fig.add_subplot(1, 3, 1)
image_plot_1 = plt.imshow(square, cmap="binary")
a.set_title("Original")

# Plot closed image
a=fig.add_subplot(1, 3, 2)
image_plot_2 = plt.imshow(closed_square, cmap="binary")
a.set_title("Closed")

# Plot opened image
a=fig.add_subplot(1, 3, 3)
image_plot_2 = plt.imshow(opened_square, cmap="binary")
a.set_title("Opened")
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

plt.show()