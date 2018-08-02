import pyautogui as pyg
import time
import cv2
import tesseract_image as ti
import numpy as np

## some general locations
Next = "pic\\Next.png"
Next2 = "pic\\next4.png"
Capture = "pic\\capture.png"
Custom = "pic\\custom.png"
icecream = "pic\\icecream.png"
play = "pic\\play2.png"
drag = "pic\\tobedragged.png"
drag2 = "pic\\tobedragged2.png"
problem =  "pic\\result.png"
name_of_the_file = ""
count=True

## next video
def next_video():
    global count
    if (pyg.locateOnScreen(Next) is not None ):
            pyg.click(pyg.locateCenterOnScreen(Next))
            pyg.click(500,500)
            print("Next Found")
    elif (pyg.locateOnScreen(Next2) is not None ):
            pyg.click(pyg.locateCenterOnScreen(Next2))
            pyg.click(500,500)
            print("Next Found")
    else:
        print("Next not found")
        count= False

## mark the area
def mark():
    pyg.moveTo(467,92)
    pyg.dragTo(1919,1038)


## extract name
def extract_name():
    global name_of_the_file
    pyg.screenshot("pic\\screenshot1.png")
    image = cv2.imread("pic\\screenshot1.png")
    image = image[140:990,515:1890]
    filename = "pic\\screenshot1.png"
    cv2.imwrite(filename,image)
    #cv2.imshow("cropped",image)
    name_of_the_file = ti.extract(filename).split('\n')[0]

##dragging
def tobedrag():
    pyg.click(pyg.locateCenterOnScreen(drag))
    pyg.dragTo(1905,750)
    pyg.click(pyg.locateCenterOnScreen(drag2))
    pyg.dragTo(1905,750)
    
    
## capture
def capture():
    if(pyg.locateOnScreen(Capture) is not None):
        pyg.moveTo(pyg.locateCenterOnScreen(Capture))
        time.sleep(1)
        pyg.click(pyg.locateCenterOnScreen(Custom))
        mark()
        pyg.click(500,500)
        extract_name()
        pyg.hotkey('ctrl','shift','r')
        time.sleep(3)
        tobedrag()
        pyg.click(500,500)
        pyg.click(pyg.locateCenterOnScreen(play))
    else :
        pyg.click(pyg.locateCenterOnScreen(icecream))
        pyg.moveTo(pyg.locateCenterOnScreen(Capture))
        time.sleep(1)
        pyg.click(pyg.locateCenterOnScreen(Custom))
        mark()
        pyg.click(500,500)
        extract_name()
        pyg.hotkey('ctrl','shift','r')
        time.sleep(3)
        tobedrag()
        pyg.click(500,500)
        pyg.click(pyg.locateCenterOnScreen(play))

## naming the file
def name():
    pyg.click(777,530)
    pyg.typewrite(name_of_the_file)
    time.sleep(1)
    pyg.click(1107,591)

## stopping
def stopping():
    pyg.screenshot("pic\\check.png")
    image = cv2.imread("pic\\check.png")
    image = image[140:990,515:1890]
    filename = "pic\\check.png"
    cv2.imwrite(filename,image)
    time.sleep(15)
    pyg.screenshot("pic\\check1.png")
    image = cv2.imread("pic\\check1.png")
    image = image[140:990,515:1890]
    filename ="pic\\check1.png"
    cv2.imwrite(filename,image)
    image2 = cv2.imread("pic\\check.png")
    difference = cv2.subtract(image,image2)
    result = not np.any(difference)
    if(result):
        pyg.hotkey('ctrl','shift','s')
        time.sleep(3)
        name()
        print(name_of_the_file)
        return False
    else:
        return True

if __name__ == "__main__":
    
    time.sleep(10)
##    extract_name()
##    print(name_of_the_file)
    while(count):
        if(pyg.locateOnScreen(problem) is None):
            capture()
            while(stopping()):
                 time.sleep(5)
        pyg.click(500,500)
        time.sleep(1)
        next_video()
        time.sleep(10)
##    exit()
        
    

    


    

