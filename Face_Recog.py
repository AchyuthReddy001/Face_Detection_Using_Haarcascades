import cv2
import matplotlib.pyplot as plt

Face_cascade=cv2.CascadeClassifier("opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml")

def detect(gray,frame):
    face=Face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
    return frame


