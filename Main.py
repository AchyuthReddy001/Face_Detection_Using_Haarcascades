import cv2
import Face_Recog

#webcam
video_cap=cv2.VideoCapture(0)

while True:
    _,frame=video_cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=Face_Recog.detect(gray,frame)
    cv2.imshow("LiveCap",canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_cap.release()
cv2.destroyAllWindows