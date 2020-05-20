import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mp_image


src_folder = "C:/Repositories/Image_Analysis/data/voc"
fig = plt.figure(figsize=(12, 12))

for root, folders, filesnames in os.walk(src_folder):
    image_num = 0 
    num_folders = len(folders)
    
    for folder in sorted(folders):
        image_num += 1
        file_name = os.listdir(os.path.join(root,folder))[0]
        file_path = os.path.join(root,folder,file_name)
        image = mp_image.imread(file_path)
        a = fig.add_subplot(num_folders, 1, image_num)
        image_plot = plt.imshow(image)
        a.set_title(folder)

plt.show()