import cv2
import mediapipe as mp
import pyautogui as pa
sw , sh = pa.size()
print(sw,sh)
mpHand = mp.solutions.hands
hand = mpHand.Hands()
draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
index_y=0


while True:
    success, vid = cap.read()
    rgbf = cv2.cvtColor(vid, cv2.COLOR_BGR2RGB)
    result = hand.process(rgbf)
    hands = result.multi_hand_landmarks
    if hands:
        for mark in hands:
            draw.draw_landmarks(vid, mark)
            for id, landmrk in enumerate(mark.landmark):
                    h, w, c = vid.shape
                    x = int(landmrk.x * w)
                    y = int(landmrk.y * h)
                    print(f"Index Finger Tip Position: {x}, {y} rgb color {c}")
                    if id == 8:
                        cv2.circle(img=vid,center=(x,y),radius=10,color=(0,255,0),)
                        index_x = sw / w*x
                        index_y = sh / h*y
                        pa.moveTo(index_x,index_y)

                    if id == 4:
                        cv2.circle(img=vid,center=(x,y),radius=10,color=(0,255,0),)
                        thumb_x = sw / w*x
                        thumb_y = sh / h*y
                        print(abs(index_y - thumb_y))
                        if abs(index_y - thumb_y)<20:
                            print('click')
                            print(abs(index_y - thumb_y))
                            pa.click()
                            pa.sleep(1)
    cv2.imshow('Mouse', vid)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
