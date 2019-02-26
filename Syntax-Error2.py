# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 20:09:52 2018

@author: saswatdas
"""

import cv2
import sys
import pytesseract
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #retval, threshold = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
    #th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    
    #cv2.imshow('frame',th)
    cv2.imshow('image',frame)
    
    # Uncomment the line below to provide path to tesseract manuall
    # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    # Define config parameters.
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    config = ('-l eng --oem 1 --psm 3')
    # Run tesseract OCR on image
    text = pytesseract.image_to_string(frame, config=config)
    # Print recognized text
    print(text)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
  