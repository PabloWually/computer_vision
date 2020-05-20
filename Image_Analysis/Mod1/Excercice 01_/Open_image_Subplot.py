import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mp_image
from PIL import Image
import skimage as sk
from skimage import io as sk_io
from skimage import transform as sk_transform
import cv2

src_folder = "C:/Repositories/Image_Analysis/data/voc"
images = []

pil_image = Image.open(os.path.join(src_folder,"automobile","000522.jpg"))
images.append(np.array(pil_image)) #numpy format
#images.append(pil_image) #pil format

sk_image = sk_io.imread(os.path.join(src_folder,"plane","000228.jpg"))
#images.append(Image.fromarray(sk_image)) #pil format
images.append(sk_image) #numpy format
#sk_image.shape #show the shape of imagen

cv_image = cv2.imread(os.path.join(src_folder,"train", "000712.jpg"))
#images.append(cv_image) #Imagen sin correcion
images.append(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)) #Imagen con correccion

""" #Image in gray scale 
sk_gray_image = sk.color.rgb2gray(sk_image) 
plt.imshow(sk_gray_image, 'gray')
sk_gray_image.shape """

""" #Rotation with PIL Library
rotated_pil_image = pil_image.rotate(90, expand=1)
plt.imshow(rotated_pil_image)
#The expand parameter tells PIL to change the image dimenions to fit the rotated orientation. Without this, we'd get an image with the original dimensions with a resized """

""" #Rotation with Scikit-Image Library
rotated_sk_image = sk_transform.rotate(sk_image, 90, resize=True)
plt.imshow(rotated_sk_image) """

fig = plt.figure(figsize=(12,12))

image_num = 0
num_images = len(images)

for image_idx in range(num_images):
    a = fig.add_subplot(1,num_images,image_idx+1)
    image_plot = plt.imshow(images[image_idx])
    a.set_title("Image" + str(image_idx+1))

plt.show()
