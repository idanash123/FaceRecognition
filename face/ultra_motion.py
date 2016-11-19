import os,time
import numpy as np
import cv2,sys
faces_num = 0
def main():
    # Get user supplied values
    scale = 1.1
    size = 40
    neighbors = 2
    done = False
    record = False
    debug = True
    faceCascade = cv2.CascadeClassifier(str("src/haarcascade_frontalface_default.xml"))
    eye_cascade = cv2.CascadeClassifier(str("src/haarcascade_eye.xml"))
    mouthCascade = cv2.CascadeClassifier(str("src/Mouth.xml"))
    noseCascade = cv2.CascadeClassifier(str("src/haarcascade_mcs_nose.xml"))
    glassesCascade = cv2.CascadeClassifier(str("src/eye_glasses.xml"))
    video_capture = cv2.VideoCapture(0)

    # Read the image
    # Detect faces in the image
    while True:
        ret, frame = video_capture.read()
        if ret:
            #image = cv2.imread(imagePath)
            #frame = image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=scale,
                minNeighbors=neighbors,
                minSize=(size, size),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            # Draw a rectangle around the faces
            eye_counter = 0
            face_counter = 0
            feature_width = 10
            if len(faces)>0:
                for (x, y, w, h) in faces:
                    mouth_found = False
                    nose_found = False
                    eye_found = False
                    eye_up = 1
                    face_counter+=1
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    nose = noseCascade.detectMultiScale(roi_gray)
                    mouth = mouthCascade.detectMultiScale(roi_gray)
                    #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    print 'face  : x = %s  y = %s  w = %s  h = %s'%(x,y,w,h)
                    print "number of eyes = %s"%len(eyes)
                    print "number of mouthes = %s"%len(mouth)
                    print "number of noses = %s"%len(nose)
                    if len(eyes) < 2:
                        eyes = glassesCascade.detectMultiScale(roi_gray)
                        print len(eyes)
                    for i in range(len (eyes)):
                        if eye_found :
                            break
                        for (ex,ey,ew,eh) in eyes:
                            #print 'eye : x = %s  y = %s  w = %s  h = %s'%(ex,ey,ew,eh)
                            #cv2.rectangle(roi_color,(ex+ew/2,ey+eh/2),(ex+ew/2,ey+eh/2),(255,255, 255),feature_width)
                            #cv2.rectangle(roi_color,(ex+ew,ey+eh/2),(ex+ew,ey+eh/2),(255, 255, 255),5)
                            #cv2.rectangle(roi_color,(ex+ew/2,ey),(ex+ew/2,ey),(255, 255, 255),5)
                            #cv2.rectangle(roi_color,(ex,ey+eh/2),(ex,ey+eh/2),(255, 255, 255),5)
                            #cv2.rectangle(roi_color,(ex+ew/2,ey+eh),(ex+ew/2,ey+eh),(255, 255, 255),5)
                            eye_counter+=1
                            if eye_counter > eye_up:
                                if abs(ey_1-ey) < 20 and abs(ex_1-ex) > 20 and abs(eh_1 -eh ) < 20:
                                    print 'eye_2 : x = %s  y = %s  w = %s  h = %s'%(ex,ey,ew,eh)
                                    cv2.rectangle(roi_color,(ex+ew/2,ey+eh/2),(ex+ew/2,ey+eh/2),(0,255, 255),feature_width)
                                    cv2.rectangle(roi_color,(ex_1+ew_1/2,ey_1+eh_1/2),(ex_1+ew_1/2,ey_1+eh_1/2),(0,255, 255),feature_width)
                                    ex_2 = ex
                                    ey_2 = ey
                                    ew_2 = ew
                                    eh_2 = eh
                                    eye_found = True
                                    eye_counter = 0
                                    eye_up = 1
                                    if debug :
                                        cv2.line(roi_color,(ex+ew,ey+eh/2),(ex+ew/2,ey+eh),(0, 255, 255),2)
                                        cv2.line(roi_color,(ex+ew/2,ey),(ex+ew,ey+eh/2),(0, 255, 255),2)
                                        cv2.line(roi_color,(ex+ew/2,ey),(ex,ey+eh/2),(0, 255, 255),2)
                                        cv2.line(roi_color,(ex+ew/2,ey+eh),(ex,ey+eh/2),(0, 255, 255),2)
                                        cv2.line(roi_color,(ex_1+ew_1,ey_1+eh_1/2),(ex_1+ew_1/2,ey_1+eh_1),(0, 255, 255),2)
                                        cv2.line(roi_color,(ex_1+ew_1/2,ey_1),(ex_1+ew_1,ey_1+eh_1/2),(0, 255, 255),2)
                                        cv2.line(roi_color,(ex_1+ew_1/2,ey_1),(ex_1,ey_1+eh_1/2),(0, 255, 255),2)
                                        cv2.line(roi_color,(ex_1+ew_1/2,ey_1+eh_1),(ex_1,ey_1+eh_1/2),(0, 255, 255),2)
                                    if record:
                                        cv2.line(roi_color,(ex_1+ew_1/2,ey_1+eh_1/2),(ex_2+ew_2/2,ey_2+eh_2/2),(255, 255, 255),2)
                                    break
                                else:
                                    eye_counter = 0
                                    eye_up += 1
                            elif eye_counter == eye_up:
                                print 'eye_1 : x = %s  y = %s  w = %s  h = %s'%(ex,ey,ew,eh)
                                ex_1 = ex
                                ey_1 = ey
                                ew_1 = ew
                                eh_1 = eh
                    for (mx,my,mw,mh) in mouth:    
                        if not eye_found or mouth_found :
                            break
                        else:
                            if my>ey+20 and h <my+mh+20:
                                print 'mouth : x = %s  y = %s  w = %s  h = %s'%(mx,my,mw,mh)
                                cv2.rectangle(roi_color,(mx+mw/2,my+mh/2),(mx+mw/2,my+mh/2),(255, 0, 255),feature_width)
                                if debug:
                                    cv2.line(roi_color,(mx+mw/2,my),(mx,my+mh/2),(255, 0, 255),2)
                                    cv2.line(roi_color,(mx+mw/2,my),(mx+mw,my+mh/2),(255, 0, 255),2)
                                    cv2.line(roi_color,(mx+mw,my+mh/2),(mx+mw/2,my+mh),(255, 0, 255),2)
                                    cv2.line(roi_color,(mx,my+mh/2),(mx+mw/2,my+mh),(255, 0, 255),2)
                                mouth_found = True
                                if record:
                                    cv2.line(roi_color,(ex_1+ew_1/2,ey_1+eh_1/2),(mx+mw/2,my+mh/2),(255, 255, 255),2)
                                    cv2.line(roi_color,(ex_2+ew_2/2,ey_2+eh_2/2),(mx+mw/2,my+mh/2),(255, 255, 255),2)
                                break
                    for (nx,ny,nw,nh) in nose:
                        if not mouth_found or nose_found:
                            break
                        else:
                            print 'nose : x = %s  y = %s  w = %s  h = %s'%(nx,ny,nw,nh)
                            if ny<my and ny >ey and (ny+y+20 > (y+y+h)/2) and (ny+y-20 < (y+y+h)/2):
                                if (ex_1+ex_2)/2<nx+20 and (ex_1+ex_2)/2>nx-20:
                                    nose_found = True
                                    cv2.rectangle(roi_color,(nx+nw/2,ny+nh/2),(nx+nw/2,ny+nh/2),(255, 255, 0),feature_width)
                                    if debug:
                                        cv2.line(roi_color,(nx+nw/2,ny),(nx,ny+nh/2),(255, 255, 0),2)
                                        cv2.line(roi_color,(nx+nw/2,ny),(nx+nw,ny+nh/2),(255, 255, 0),2)
                                        cv2.line(roi_color,(nx+nw,ny+nh/2),(nx+nw/2,ny+nh),(255, 255, 0),2)
                                        cv2.line(roi_color,(nx,ny+nh/2),(nx+nw/2,ny+nh),(255, 255, 0),2)
                                    done = True
                                    if record:
                                        cv2.line(roi_color,(ex_1+ew_1/2,ey_1+eh_1/2),(nx+nw/2,ny+nh/2),(255, 255, 255),2)
                                        cv2.line(roi_color,(ex_2+ew_2/2,ey_2+eh_2/2),(nx+nw/2,ny+nh/2),(255, 255, 255),2)
                                        cv2.line(roi_color,(nx+nw/2,ny+nh/2),(mx+mw/2,my+mh/2),(255, 255, 255),2)
                                    break
                    if debug and done:
                        done = False
                        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                        ##face rec
                        cv2.line(frame,(x+w/2,y),(x,y+h/2),(0, 0, 255),2)
                        cv2.line(frame,(x+w/2,y),(x+w,y+h/2),(0, 0, 255),2)
                        cv2.line(frame,(x+w,y+h/2),(x+w/2,y+h),(0, 0, 255),2)
                        cv2.line(frame,(x,y+h/2),(x+w/2,y+h),(0, 0, 255),2)
                        #T draw'
                        cv2.line(frame,(x+w/2,y),(nx+nw/2+x,ny+nh/2+y),(0, 0, 0),10)
                        cv2.line(frame,(nx+nw/2+x,ny+nh/2+y),(mx+mw/2+x,my+mh/2+y),(0, 0, 0),10)
                        cv2.line(frame,(nx+nw/2+x,ny+nh/2+y),(x+w/2,y+h),(0, 0, 0),10)
                        cv2.line(frame,(ex_1+ew_1/2+x,ey_1+eh_1+y),(ex+ew/2+x,ey+eh+y),(0, 0, 0),10)
                        #cv2.line(frame,(ex_2+x,ey_2+eh_2/2+y),(ex_1+ew_1+x,ey_1+eh_1/2+y),(0, 0, 0),10)
                        #cv2.line(frame,(ex_1+x,ey_1+eh_1/2+y),(ex_2+ew_2+x,ey_2+eh_2/2+y),(0, 0, 0),10)
                        cv2.line(frame,(nx+x,ny+nh/2+y),(nx+nw+x,ny+nh/2+y),(0, 0, 0),10)
                        cv2.line(frame,(mx+x,my+mh/2+y),(mx+mw+x,my+mh/2+y),(0, 0, 0),10)
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
if __name__ == '__main__':
    main()   
