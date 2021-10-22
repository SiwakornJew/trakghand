import cv2
import time
import numpy as np
import HandTrackingModule as hp
cap=cv2.VideoCapture(0)
pTime = 0
cTime = 0
detertor =hp.handDetector()
while True:
    success, img =cap.read()
    img = detertor.findHands(img)
    lmList=detertor.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])
    cTime =time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255, 0,),3)
    cv2.imshow("Image",img) 
    cv2.waitKey(1)  
