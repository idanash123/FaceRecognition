import os,time
import numpy as np
import cv2,sys
def main():

    eye_cascade = cv2.CascadeClassifier(str("src/haarcascade_eye.xml"))
    faceCascade = cv2.CascadeClassifier(str("src/haarcascade_frontalface_default.xml"))
    eyes = []
    video_capture = cv2.VideoCapture(0)
    #video_capture = cv2.VideoCapture("rtsp://192.168.1.1/MJPG")
    while True:
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
        cv2.imshow('Video', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()   
