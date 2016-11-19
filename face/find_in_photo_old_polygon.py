import os,time
import numpy as np
import cv2,sys
faces_num = 0
def main():
    # Get user supplied values
    imagePath = sys.argv[1] 
    scale = 1.1
    size = 10
    neighbors = 1
    done = False
    faceCascade = cv2.CascadeClassifier(str("src/haarcascade_frontalface_default.xml"))
    eye_cascade = cv2.CascadeClassifier(str("src/haarcascade_eye.xml"))
    mouthCascade = cv2.CascadeClassifier(str("src/Mouth.xml"))
    noseCascade = cv2.CascadeClassifier(str("src/haarcascade_mcs_nose.xml"))
    glassesCascade = cv2.CascadeClassifier(str("src/eye_glasses.xml"))
    # Read the image
    # Detect faces in the image
    while not done:
        image = cv2.imread(imagePath)
        frame = image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
        record = True
        if len(faces)>0:
            for (x, y, w, h) in faces:
                if record == True and done == True:
                   break
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
                            if abs(ey_1-ey) < 20 and abs(ex_1-ex) > 15 and abs(eh_1 -eh ) < 15:
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
                                #cv2.line(roi_color,(ex+ew,ey+eh/2),(ex+ew/2,ey+eh),(255, 255, 255),1)
                                #cv2.line(roi_color,(ex+ew/2,ey),(ex+ew,ey+eh/2),(255, 255, 255),1)
                                #cv2.line(roi_color,(ex+ew/2,ey),(ex,ey+eh/2),(255, 255, 255),1)
                                #cv2.line(roi_color,(ex+ew/2,ey+eh),(ex,ey+eh/2),(255, 255, 255),1)
                                if record:
                                    cv2.line(roi_color,(ex_1+ew_1/2,ey_1+eh_1/2),(ex_2+ew_2/2,ey_2+eh_2/2),(255, 255, 255),2)
                                break
                            else:
                                eye_counter = 0
                                eye_up += 1
                        elif eye_counter == eye_up:
                            #cv2.rectangle(roi_color,(ex+ew/2,ey+eh/2),(ex+ew/2,ey+eh/2),(0, 255, 255),feature_width)
                            print 'eye_1 : x = %s  y = %s  w = %s  h = %s'%(ex,ey,ew,eh)
                            ex_1 = ex
                            ey_1 = ey
                            ew_1 = ew
                            eh_1 = eh
                            #cv2.line(roi_color,(ex+ew,ey+eh/2),(ex+ew/2,ey+eh),(255, 255, 255),1)
                            #cv2.line(roi_color,(ex+ew/2,ey),(ex+ew,ey+eh/2),(255, 255, 255),1)
                            #cv2.line(roi_color,(ex+ew/2,ey),(ex,ey+eh/2),(255, 255, 255),1)
                            #cv2.line(roi_color,(ex+ew/2,ey+eh),(ex,ey+eh/2),(255, 255, 255),1)
                for (mx,my,mw,mh) in mouth:
                    #print 'mouth : x = %s  y = %s  w = %s  h = %s'%(mx,my,mw,mh)
    
                    if not eye_found or mouth_found :
                        break
                    else:
                        if my>ey+20 and h <my+mh+20:
                            print 'mouth : x = %s  y = %s  w = %s  h = %s'%(mx,my,mw,mh)
                            cv2.rectangle(roi_color,(mx+mw/2,my+mh/2),(mx+mw/2,my+mh/2),(255, 0, 255),feature_width)
                            #cv2.rectangle(roi_color,(mx+mw/2,my),(mx+mw/2,my),(255, 255, 255),5)
                            #cv2.rectangle(roi_color,(mx,my+mh/2),(mx,my+mh/2),(255, 255, 255),5)
                            #cv2.rectangle(roi_color,(mx+mw,my+mh/2),(mx+mw,my+mh/2),(255, 255, 255),5)
                            #cv2.rectangle(roi_color,(mx+mw/2,my+mh),(mx+mw/2,my+mh),(255, 255, 255),5)
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
                        if ny<my and ny >ey:
                            if (ex_1+ex_2)/2<nx+30 and (ex_1+ex_2)/2>nx-30:
                                nose_found = True
                                cv2.rectangle(roi_color,(nx+nw/2,ny+nh/2),(nx+nw/2,ny+nh/2),(255, 255, 0),feature_width)
                                done = True
                                if record:
                                    cv2.line(roi_color,(ex_1+ew_1/2,ey_1+eh_1/2),(nx+nw/2,ny+nh/2),(255, 255, 255),2)
                                    cv2.line(roi_color,(ex_2+ew_2/2,ey_2+eh_2/2),(nx+nw/2,ny+nh/2),(255, 255, 255),2)
                                    cv2.line(roi_color,(nx+nw/2,ny+nh/2),(mx+mw/2,my+mh/2),(255, 255, 255),2)
                                break
        #cv2.imwrite("./face.jpeg",frame)
        if done == True:
            print "scale = %s"%scale
            cv2.imshow("Faces found", frame)
            cv2.waitKey(0)
        else:
            size += 10
            if size > 80:
                size = 10
                scale +=0.1
                print scale
            print size
        if scale > 1.9:
            done = True
            print "Cannot detect face"
if __name__ == '__main__':
    main()   
