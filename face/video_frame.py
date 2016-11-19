import os,time
import numpy as np
import cv2,sys
def main():
    counter = 1
    video_capture = cv2.VideoCapture(0)
    tic = time.time()
    while True:
        ret, frame = video_capture.read()
        if ret:
            cv2.imshow('Video', frame)
            if time.time() - tic > 0.3:
                tic = time.time()
                cv2.imwrite("photos/frame%05d.jpeg"%counter,frame)
                counter+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()   
