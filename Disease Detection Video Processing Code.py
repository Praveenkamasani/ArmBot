# VIDEO PROCESSING CODE

import cv2
import numpy as np
import math
import time
import serial
ser = serial.Serial('COM6',9600)
#Initializing the RGB values for healthy and diseased
lb_green=np.array([33,80,40])
ub_green=np.array([102,255,255])
#Disease RGB values Got from A website named --> https://imagecolorpicker.com/
lb_brown=np.array([20,100,100])
ub_brown=np.array([30,255,255])
greenarea=0
brownarea=0
greentotal=0
browntotal=0
cam=cv2.VideoCapture(0)
kernelOpen=np.ones((15,15))
52kernelClose=np.ones((30,30))
while True:
getval= ser.readline()
ret,img=cam.read()
#IMAGE PREPROCESSING
mg=cv2.resize(img,(500,500))
cv2.imshow("orginal",img)
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 cv2.imshow("HSV",imgHSV)
#MASKING DISEASE
mask=cv2.inRange(imgHSV,lb_brown,ub_brown)
 maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
 cv2.imshow("masking BROWN",maskClose)
_,cnt,hie=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(cnt)):
x,y,w,h=cv2.boundingRect(cnt[i])
brownarea=cv2.contourArea(cnt[i])
 if(brownarea > 0):
53 cv2.drawContours(img,cnt,-1,(0,0,255),2)
 browntotal=browntotal+brownarea
print browntotal,"DISEASE"
 cv2.imshow("masking BROWN",mask)
#MASKING GREEN
mask=cv2.inRange(imgHSV,lb_green,ub_green)
maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
cv2.imshow("masking GREEN",maskClose)
_,cnt,hie=cv2.findContours(maskOpen,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE
)
 cv2.drawContours(img,cnt,-1,(0,255,0),2)
for i in range(len(cnt)):
 x,y,w,h=cv2.boundingRect(cnt[i])
 greenarea=cv2.contourArea(cnt[i])
 greentotal=greentotal+greenarea
 print greentotal,"GREEN"
 cv2.imshow("masking GREEN",mask)
 if(greentotal==0):
 greentotal=1
disease_percentage=(browntotal/(greentotal+browntotal))*100
 print "Disease percentage :",disease_percentage,"%"
54 cv2.imshow("cam",img)
#RECOGNITION
if (disease_percentage>5):
 val="1"
 ser.write(val)
browntotal=0
greentotal=0
 cv2.waitKey(20)