import cv2
import numpy as np
import pytesseract
import random
s = 'ABCEEFGHIJKLMNOPQRSTUVWXYZ'
def getNumber():
    for i in range(1,9999):
        for a in s:
            for j in range(1,100):
                s='KA '+ str(j).zfill(2) + " " +a + " " + str(i).zfill(4)
                return s
def getRandomNumber():
    global s
    s='KA '+ str(random.randint(9,100)).zfill(2) + " " +random.choice(s) + " " + str(random.randint(1,9999)).zfill(4)
    return s

# img = np.zeros([50,175,3],dtype=np.uint8)
img1  = cv2.imread('number_plate_template.jpg',cv2.IMREAD_COLOR)
# img.fill(255) # or img[:] = 255
# font 
for font in range(8) :# cv2.FONT_HERSHEY_SIMPLEX 
    img = img1.copy()
    # org 
    org = (45, 45) 

    # fontScale 
    fontScale = 0.8 #random.choice(range(.8,15))/10

    # Black color in BGR 
    color = (0, 0, 0) 

    # Line thickness of 2 px 
    thickness = 2
    # Using cv2.putText() method 
    num = getRandomNumber()
    image = cv2.putText(img, num, org, font,  
                    fontScale, color, thickness, cv2.LINE_AA) 
    window_name = 'Image'   
    #Displaying the image 
    cv2.imshow(window_name, image)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    data_string = pytesseract.image_to_string(image, lang='eng', config='--oem 3')
    print(fontScale,num,data_string)
