import cv2
import mediapipe as mp
import time

mpdraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

pTime=0

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1920)
while True:
    success , vid = cap.read()
    imgRGB = cv2.cvtColor(vid,cv2.COLOR_BGR2RGB )
    result = pose.process(vid)
    print(result.pose_landmarks)
    if result.pose_landmarks:
        mpdraw.draw_landmarks(vid,result.pose_landmarks,mpPose.POSE_CONNECTIONS)



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime

    cv2.putText(vid,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,3),3)
    cv2.imshow("Img",vid)


    cv2.waitKey(1)