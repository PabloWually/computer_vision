""" 
You may have noted that by default, Matplotlib plots images with an axis that shows the height and width
of the image in pixels - the plots themselves are scaled to be displayed in the Notebook; but what if you
actually want to resize an image?

One way is to use PIL's thumbnail method:
"""
import os
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def resize_image(src_image, size=(200,200), bg_color="white"): 
    # resize the image so the longest dimension matches our target size
    src_image.thumbnail(size, Image.ANTIALIAS)
    
    # Create a new square background image
    new_image = Image.new("RGB", size, bg_color)
    
    # Paste the resized image into the center of the square background
    new_image.paste(src_image, (int((size[0] - src_image.size[0]) / 2), int((size[1] - src_image.size[1]) / 2)))
  
    # return the resized image
    return new_image

src_folder = "C:/Repositories/Image_Analysis/data/voc"
pil_image = Image.open(os.path.join(src_folder,"automobile","000522.jpg"))

o_h, o_w = pil_image.size
print('Original size', o_h, 'x', o_w)

target_size = (150,150)

#Image resized
resized_img = pil_image.copy()
resized_img.thumbnail(target_size, Image.ANTIALIAS)

""" resized_img = pil_image.resize(target_size)
#Image without scaled """

""" #Image with bachground
pad_color = "black"
resized_img = resize_image(pil_image.copy(), target_size, pad_color) """


n_h, n_w = resized_img.size
print('New size', n_h, 'x', n_w)

fig = plt.figure(figsize=(12,12))
a = fig.add_subplot(1,2,1)
imgplot = plt.imshow(pil_image)
a.set_title('Before')

a=fig.add_subplot(1,2,2)
imgplot = plt.imshow(resized_img)
a.set_title('After')

plt.show()