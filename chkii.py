import numpy as np
import os
from PIL import Image



def to_integral_image(img_arr):

    row_sum = np.zeros(img_arr.shape)
    # we need an additional column and row
    integral_image_arr = np.zeros((img_arr.shape[0] + 1, img_arr.shape[1] + 1))
    for x in range(img_arr.shape[1]): #COL, X
        for y in range(img_arr.shape[0]): #ROW, Y
            row_sum[y, x] = row_sum[y-1, x] + img_arr[y, x]
            integral_image_arr[y+1, x+1] = integral_image_arr[y+1, x-1+1] + row_sum[y, x]
    return integral_image_arr


def sum_region(integral_img_arr, top_left, bottom_right):
   
    top_left = (top_left[1], top_left[0])
    bottom_right = (bottom_right[1], bottom_right[0])
    if top_left == bottom_right:
        return integral_img_arr[top_left]
    top_right = (bottom_right[0], top_left[1])
    bottom_left = (top_left[0], bottom_right[1])
    return integral_img_arr[bottom_right] + integral_img_arr[top_left] - integral_img_arr[top_right] - integral_img_arr[bottom_left] 


def load_images(path):
    images = []
    for _file in os.listdir(path):
        img_arr = np.array(Image.open((os.path.join(path, _file))), dtype=np.float64)
        img_arr /= img_arr.max()
        images.append(img_arr)
    return images

imagesR = load_images("Face")
print imagesR
iiar = to_integral_image(imagesR)
print iiar
