# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 22:44:57 2018

@author: saswatdas
"""

import cv2
import numpy as np

#img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg')
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('star.jpg',0)
w, h = template.shape[::-1]


###################
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #retval, threshold = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
    #th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    
    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)
    
    cv2.imshow('frame',frame)
    #cv2.imshow('frame2',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()