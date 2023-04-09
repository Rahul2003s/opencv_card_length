import cv2
import numpy as np

def getContours(img,cThr=[100,100],showCanny=False):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,cThr[0],cThr[1])
    kernal = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernal,iterations=3)
    imgThre = cv2.erode(imgDial , kernal, iterations=2)
    if showCanny:
        cv2.imshow('canny',imgThre)
    
    contours,hiearchy = cv2.findContours(imgThre,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for i in contours:
        area = cv2.contourArea(i)
        if area > minArea:
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,)