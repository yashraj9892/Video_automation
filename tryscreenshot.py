import pyautogui as pyg
import cv2
import time
import numpy as np
time.sleep(10)

pyg.screenshot("C:\\Users\\yashr\\Pictures\\check.png")
image = cv2.imread("C:\\Users\\yashr\\Pictures\\check.png")
image = image[92:1038,467:1919]
filename ="C:\\Users\\yashr\\Pictures\\check.png"
cv2.imwrite(filename,image)
print(1)
time.sleep(5)
pyg.screenshot("C:\\Users\\yashr\\Pictures\\check1.png")
image = cv2.imread("C:\\Users\\yashr\\Pictures\\check1.png")
image = image[92:1038,467:1919]
filename ="C:\\Users\\yashr\\Pictures\\check1.png"
cv2.imwrite(filename,image)
image2 = cv2.imread("C:\\Users\\yashr\\Pictures\\check.png")
difference = cv2.subtract(image,image2)
result = not np.any(difference)

if(result):
    print("yes")
else:
    print("No")
