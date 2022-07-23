import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

def LookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))

def sandstorm(img):
    increaseLookupTable = LookupTable([0, 45, 105, 256], [0, 120, 195, 256])
    decreaseLookupTable = LookupTable([0, 90, 153, 256], [0, 22, 72, 256])
    blue_channel, green_channel,red_channel  = cv2.split(img)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    sum= cv2.merge((blue_channel, green_channel, red_channel ))
    median = cv2.GaussianBlur(sum, (3,3),0)
    return median

for i in os.listdir("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/images"): # Adding Haze image w.r.t depth maps.
    path = f"images/{i}"

    print(i)

    img = plt.imread(path)

    depth_path = f"depth_images/{i.split('.')[0]}_depth.jpg" # Obtain the depth images from the Monodepth2 scritps.
    depth_img = plt.imread(depth_path)

    depth_img_3c = np.zeros_like(img)
    depth_img_3c[:,:,0] = depth_img
    depth_img_3c[:,:,1] = depth_img
    depth_img_3c[:,:,2] = depth_img

    beta=0.82
    norm_depth_img = depth_img_3c/255
    trans = np.exp(-norm_depth_img*beta)

    A = 255
    hazy = img*trans + A*(1-trans)
    hazy = np.array(hazy, dtype=np.uint8)


    cv2.imwrite("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/hazed_images/" + str(i), cv2.cvtColor(hazy, cv2.COLOR_BGR2RGB))
    
for i in os.listdir("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/hazed_images/"):
    img = cv2.imread("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/hazed_images/" + i)
    img = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
    img = sandstorm(img)
    cv2.imwrite("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/sandstorm_images/" + str(i), img)