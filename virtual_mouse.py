import cv2
import time
import pyautogui 
import handTrackingModule as htm
import math 
import numpy as np
from pynput.mouse import Button , Controller
import imutils
#######################################################
mouse=Controller()
pyautogui.FAILSAFE=False


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

pTime=0
cTime=0
detector=htm.handDetector(detectionCon=0.7)
while True:
    success,img=cap.read()
    img=cv2.flip(img,+1)
    img=detector.findHands(img)
    Lmlist,bbox=detector.findPosition(img,draw=False)
     

  
    
    
    
    if len(Lmlist)!=0:
       # print(Lmlist[4],Lmlist[8])
        x1,y1=Lmlist[12][1],Lmlist[12][2]
        x2,y2=Lmlist[8][1],Lmlist[8][2]
        
        finger=detector.fingerUp()
        pyautogui.moveTo(x2,y2)


        
        cx,cy=(x1+x2)//2 ,(y1+y2)//2
        cv2.circle(img,(x1,y1),10,(170,0,25),cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(170,0,25),cv2.FILLED)
        #cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img,(cx,cy),5,(120,0,25),cv2.FILLED)
        
        length=math.hypot(x2-x1 , y2-y1)
        cv2.putText(img,f"Distance:{str(length)}",(10,120),cv2.FONT_HERSHEY_COMPLEX,1,(255,117,89),2)

        


        
        
        if length<65:
            mouse.press(Button.left)
        else:
            mouse.release(Button.left)
        
        

       

      


    
            
    
      
    cTime=time.time()
    deno=(cTime-pTime)
    if(deno==0): 
        deno=deno+1
    fps=1/deno
    pTime=cTime

    cv2.putText(img,f'FPS {int(fps)}',(10,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
   

    cv2.imshow("potput",img)

    if(cv2.waitKey(1)==27):
        break

cap.release()
cv2.destroyAllWindows()


