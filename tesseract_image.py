from pytesseract import image_to_string
from PIL import Image
import cv2
import os

def extract(location):
    image = cv2.imread(location)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU)
    filename = location
    cv2.imwrite(filename, gray[1])
    text = image_to_string(Image.open(filename))
##    os.remove(filename)
    return text

