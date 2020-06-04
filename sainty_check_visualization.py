import cv2
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

img_path = "./test/living_room_0/"
img_list_depth = glob.glob(img_path + '*_depth_0_final.png')
img_list_depth = sorted(img_list_depth, key=lambda x: int(
    x.split("/")[-1].split("_")[0]))

img_list_rgb = glob.glob(img_path + '*_image_0.png')
img_list_rgb = sorted(img_list_rgb, key=lambda x: int(
    x.split("/")[-1].split("_")[0]))

img_list_seg = glob.glob(img_path + '*_segmentation_0_final.png')
img_list_seg = sorted(img_list_seg, key=lambda x: int(
    x.split("/")[-1].split("_")[0]))

# for n in range(len(img_list_rgb)):
#     print(img_list_depth[n])


for n in range(len(img_list_rgb)):
    rgb = cv2.imread(img_list_rgb[n])
    depth = cv2.imread(img_list_depth[n])
    seg = cv2.imread(img_list_seg[n])

    fig = plt.figure(figsize=(25, 25))
    fig.add_subplot(1, 3, 1)
    plt.title(img_list_rgb[n])
    plt.imshow(rgb)
    fig.add_subplot(1, 3, 2)
    plt.imshow(depth)
    fig.add_subplot(1, 3, 3)
    plt.imshow(seg)

    plt.show()
