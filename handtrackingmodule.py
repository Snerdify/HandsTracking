import cv2
import mediapipe as mp 
import time



#create a class
class handDetector():
    def _init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        #create an object which has its own variable, to use the variable we use self.

        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        
        self.mpHands=self.mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon ,self.trackCon)
        self.mpDraw=self.mp.solutions.drawing_utils

    def findHands(self,img,draw=True ):


        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=self.hands.process(imgRGB)


        if results.multi_hand_landmarks:

            for handLms in results.multi_hand_landmarks:
           
                if draw:

                    self.mp.Draw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)  


            '''
            for id,lm in enumerate(handLms.landmark):
                print(id,lm)
                #checck the height ,widthand channels of the image
                h,w,c=img.shape
                #find the position of the centre
                cx,cy=int(lm.x*w),int(lm.y*h)
                #TRACK THE LANDMARK WITH INDEX 0
                if id==4:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)


            '''
        return img



   

    #check if you have multiple hands or not
    #print(results.multi_hand_landmarks)
    

    
def main():
    pTime=0
    cTime=0
    cap=cv2.VideoCapture(0)
    detector=handDetector()


    while True:
        success,img=cap.read()
        img = detector.findHands(img)
        #code for the frames fps

        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)

        cv2.imshow("Image",img)
        cv2.waitKey(1)






#whatever we write in the main part will showcase what will this code do
if __name__=='__main__':
    main()