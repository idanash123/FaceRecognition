import os,time
import numpy as np
import cv2,sys
from Tkinter import *
import cv2.cv as cv
from thread import start_new_thread

def window():
    root = Tk()
    canvas = Canvas(root, width=500, height=300, bd = 10, bg = 'white')
    canvas.grid(row = 0, column = 0, columnspan = 2)
    b = Button(width = 10, height = 2, text = 'Button1')
    b.grid(row = 1, column = 0)
    b2 = Button(width = 10, height = 2, text = 'Button2')
    b2.grid(row = 1,column = 1)
    start_new_thread(main,(canvas,))   
    root.mainloop() 
    
def main(canvas):
    eye_cascade = cv2.CascadeClassifier(str("src/haarcascade_eye.xml"))
    faceCascade = cv2.CascadeClassifier(str("src/haarcascade_frontalface_default.xml"))
    eyes = []
    #video_capture = cv2.VideoCapture("rtsp://192.168.1.1/MJPG")
    video_capture = cv.CaptureFromCAM("rtsp://192.168.1.1/MJPG")
    while True:
        time.sleep(0.001)
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        
        # Draw a rectangle around the faces
        if len(faces)>0:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                break
        cv2.imwrite("./idan1.jpeg",frame)
        '''
        if len(eyes)>0:
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        '''
        # Display the resulting frame
        img = cv.QueryFrame(frame)
        canvas.create_image(0,0, image=img)

        #cv2.imshow('Video',frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    window()

