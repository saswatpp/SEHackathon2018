# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 16:46:27 2018

@author: saswatdas
"""
import cv2
import numpy as np
#from matplotlib import pyplot as plt
#'http://192.168.43.1:8080/video'

cap = cv2.VideoCapture('http://192.168.43.1:8080/video')

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #retval, threshold = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow('frame',th)
    #cv2.imshow('frame2',gray)
    #blur = cv2.GaussianBlur(th,(15,15),0)
    #cv2.imshow('Gaussian Blurring',blur)
    #median = cv2.medianBlur(th,15)
    #cv2.imshow('Median Blur',median)
    #bilateral = cv2.bilateralFilter(th,15,75,75)
    #cv2.imshow('bilateral Blur',bilateral)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()