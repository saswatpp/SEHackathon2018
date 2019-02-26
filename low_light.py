import cv2
import numpy as np
import pytesseract


import ocr2
#import ttos

cap = cv2.VideoCapture('http://192.168.43.1:8080/video')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

while(True):
    while(True):
        ret, img = cap.read()
        cv2.imshow('image',img)
        if ((cv2.waitKey(1) & 0xFF) == ord('q')):
            break


    # Apply dilation and erosion to remove some noise
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(img, kernel, iterations=1)
    #img = cv2.erode(img, kernel, iterations=1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #kernel = np.ones((5,5),np.float32)/25
    #dst = cv2.filter2D(img,-1,kernel)
    #retval, threshold = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
    #th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    #dst = cv2.fastNlMeansDenoisingColored(th,None,10,10,7,21)
    cv2.imshow('image1',gray)
    #cv2.imshow('frame2',gray)
    #print("gray:")
    #th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    #blur = cv2.GaussianBlur(th,(15,15),0)
    text=(ocr2.ocr(gray))
    #cv2.imshow('image2',g)
    #ttos.text_to_speech(text)
    print(text)
    # print("normal:")
    # ocr2.ocr(th)
    if ((cv2.waitKey(1) & 0xFF) == ord('e')):
        break
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
