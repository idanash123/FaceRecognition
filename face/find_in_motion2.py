import time,sys,cv2,math,os
import numpy as np
import compare
data_base = {}
eps = 0.00679
num_of_values = 12
percentage = 85
num_of_rec = 4
names = []
eye_dist_x = []
eye1_nose_dist_x = []
eye2_nose_dist_x = []
eye1_mouth_dist_x = []
eye2_mouth_dist_x = []
mouth_nose_dist_x = []
eye_dist_y = []
eye1_nose_dist_y = []
eye2_nose_dist_y = []
eye1_mouth_dist_y = []
eye2_mouth_dist_y = []
mouth_nose_dist_y = []
times = []
def avg_arrays():
    global eye_dist_x,eye1_nose_dist_x,eye2_nose_dist_x,eye1_mouth_dist_x, \
    eye2_mouth_dist_x,mouth_nose_dist_x,eye_dist_y,eye1_nose_dist_y,\
    eye2_nose_dist_y,eye1_mouth_dist_y,eye2_mouth_dist_y,mouth_nose_dist_y
    temp_values = []
    try:
        '''
        temp_values.append(np.mean(eye_dist_x))
        temp_values.append(np.mean(eye1_nose_dist_x))
        temp_values.append(np.mean(eye2_nose_dist_x))
        temp_values.append(np.mean(eye1_mouth_dist_x))
        temp_values.append(np.mean(eye2_mouth_dist_x))
        temp_values.append(np.mean(mouth_nose_dist_x))
        temp_values.append(np.mean(eye_dist_y))
        temp_values.append(np.mean(eye1_nose_dist_y))
        temp_values.append(np.mean(eye2_nose_dist_y))
        temp_values.append(np.mean(eye1_mouth_dist_y))
        temp_values.append(np.mean(eye2_mouth_dist_y))
        temp_values.append(np.mean(mouth_nose_dist_y))
        '''
        temp_values.append(eye_dist_x[0])
        temp_values.append(eye1_nose_dist_x[0])
        temp_values.append(eye2_nose_dist_x[0])
        temp_values.append(eye1_mouth_dist_x[0])
        temp_values.append(eye2_mouth_dist_x[0])
        temp_values.append(mouth_nose_dist_x[0])
        temp_values.append(eye_dist_y[0])
        temp_values.append(eye1_nose_dist_y[0])
        temp_values.append(eye2_nose_dist_y[0])
        temp_values.append(eye1_mouth_dist_y[0])
        temp_values.append(eye2_mouth_dist_y[0])
        temp_values.append(mouth_nose_dist_y[0])
        return temp_values

    except:
        return -1
def init_arrays():
    global eye_dist_x,eye1_nose_dist_x,eye2_nose_dist_x,eye1_mouth_dist_x, \
    eye2_mouth_dist_x,mouth_nose_dist_x,eye_dist_y,eye1_nose_dist_y,\
    eye2_nose_dist_y,eye1_mouth_dist_y,eye2_mouth_dist_y,mouth_nose_dist_y
    
    eye_dist_x = []
    eye1_nose_dist_x = []
    eye2_nose_dist_x = []
    eye1_mouth_dist_x = []
    eye2_mouth_dist_x = []
    mouth_nose_dist_x = []
    eye_dist_y = []
    eye1_nose_dist_y = []
    eye2_nose_dist_y = []
    eye1_mouth_dist_y = []
    eye2_mouth_dist_y = []
    mouth_nose_dist_y = []
def upload_data_base():
    global data_base,names
    os.system("ls records/ >a")
    file1 = open("a","rb")
    line1 = file1.readline()
    while not line1 == "":
        line1 = line1[:len(line1)-1]
        names.append(line1)
        line1 = file1.readline()
    file1.close()
    for i in range(len(names)):
        temp_tuple = ()
        temp_dict = {}
        for j in range(1,5):
            path ="records/"+names[i]+"/"+names[i]+str(j)
            file1 = open(path,'rb')
            line1 = file1.readline()
            while not line1 == "":
                temp_tuple = temp_tuple + (line1,)
                line1 = file1.readline()
            temp_dict[j] = temp_tuple
            temp_tuple = ()
        data_base[names[i]] = temp_dict    
def normal_vectors(ex_1,ey_1,eh_1,ew_1,ex_2,ey_2,eh_2,ew_2,nx,ny,nh,nw,mx,my,mh,mw):
    global eye_dist_x,eye1_nose_dist_x,eye2_nose_dist_x,eye1_mouth_dist_x, \
    eye2_mouth_dist_x,mouth_nose_dist_x,eye_dist_y,eye1_nose_dist_y,\
    eye2_nose_dist_y,eye1_mouth_dist_y,eye2_mouth_dist_y,mouth_nose_dist_y
    
    val = normal(ex_1+ew_1/2,ey_1+eh_1/2,ex_2+ew_2/2,ey_2+eh_2/2,'x')
    if val == -1:
        return -1
    else:
        eye_dist_x.append(val)
    val = normal(ex_1+ew_1/2,ey_1+eh_1/2,nx+nw/2,ny+nh/2,'x')
    if val == -1:
        return -1
    else:
        eye1_nose_dist_x.append(val)
    val = normal(ex_2+ew_2/2,ey_2+eh_2/2,nx+nw/2,ny+nh/2,'x')
    if val == -1:
        return -1
    else:
        eye2_nose_dist_x.append(val)
    val = normal(ex_1+ew_1/2,ey_1+eh_1/2,mx+mw/2,my+mh/2,'x')
    if val == -1:
        return -1
    else:
        eye1_mouth_dist_x.append(val)
    val = normal(ex_2+ew_2/2,ey_2+eh_2/2,mx+mw/2,my+mh/2,'x')
    if val == -1:
        return -1
    else:
        eye2_mouth_dist_x.append(val)
    val = normal(mx+mw/2,my+mh/2,nx+nw/2,ny+nh/2,'x')
    if val == -1:
        return -1
    else:
        mouth_nose_dist_x.append(val)
    val = normal(ex_1+ew_1/2,ey_1+eh_1/2,ex_2+ew_2/2,ey_2+eh_2/2,'y')
    if val == -1:
        return -1
    else:
        eye_dist_y.append(val)
    val = normal(ex_1+ew_1/2,ey_1+eh_1/2,nx+nw/2,ny+nh/2,'y')
    if val == -1:
        return -1
    else:
        eye1_nose_dist_y.append(val)
    val = normal(ex_2+ew_2/2,ey_2+eh_2/2,nx+nw/2,ny+nh/2,'y')
    if val == -1:
        return -1
    else:
        eye2_nose_dist_y.append(val)
    val = normal(ex_1+ew_1/2,ey_1+eh_1/2,mx+mw/2,my+mh/2,'y')
    if val == -1:
        return -1
    else:
        eye1_mouth_dist_y.append(val)
    val = normal(ex_2+ew_2/2,ey_2+eh_2/2,mx+mw/2,my+mh/2,'y')
    if val == -1:
        return -1
    else:
        eye2_mouth_dist_y.append(val)
    val = normal(mx+mw/2,my+mh/2,nx+nw/2,ny+nh/2,'y') 
    if val == -1:
        return -1
    else:
        mouth_nose_dist_y.append(val)
    return 1
def normal(x1,y1,x2,y2,string):
    try:
        x = abs(x2-x1)
        y = abs(y2-y1)
        if x*x+y*y == 0:
            return -1
        if string == 'x':
            ret = x/(float(math.sqrt(x*x+y*y)))
            return ret
        elif string == 'y':
            ret =y/(float(math.sqrt(x*x+y*y)))
            return ret
    except:
        return -1
def main():
    '''
    this module is to detect face with 2 eyes 1 nose and 1 mouth
    the moudule is also can record a person 
    The matrix is build like this
    it is a distance vectors  between eyes mouth and nose
    mouth_width    mouth_height
    eye_1->eye_2   eye_1->nose   eye_2->nose
    eye_1->mouth   eye_2->mouth  mouth->nose
    ''' 
    try:
        record = sys.argv[2]
        name = sys.argv[1]
    except:
        record= False
        name = False
    print ("uploading data_base...")
    
    upload_data_base()
    print ("uploading data_base DONE!")


    eye_cascade = cv2.CascadeClassifier(str("src/haarcascade_eye.xml"))
    faceCascade = cv2.CascadeClassifier(str("src/haarcascade_frontalface_default.xml"))
    mouthCascade = cv2.CascadeClassifier(str("src/Mouth.xml"))
    noseCascade = cv2.CascadeClassifier(str("src/Nose.xml"))
    eye_counter = 0
    fps = 0
    tic = time.time()
    video_capture = cv2.VideoCapture(0)
     
    #video_capture = cv2.VideoCapture("rtsp://192.168.1.1/MJPG")
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if ret:
            tic1 = time.time()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            
            # Draw a rectangle around the faces
            try:
                fps+=1
                if time.time()-tic > 5:
                    tic = time.time()
                    print 'FPS = %f'%float(float(fps)/5.0)
                    fps = 0
                mouth_found = False
                nose_found = False
                eye_found = False
                face_counter = 0
                if len(faces)>0:
                    for (x, y, w, h) in faces:
                        face_counter+=1
                        #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                        roi_gray = gray[y:y+h, x:x+w]
                        roi_color = frame[y:y+h, x:x+w]
                        eyes = eye_cascade.detectMultiScale(roi_gray)
                        mouth = mouthCascade.detectMultiScale(roi_gray)
                        nose = noseCascade.detectMultiScale(roi_gray)
                        #print 'face  : x = %s  y = %s  w = %s  h = %s'%(x,y,w,h)
    
                        for (ex,ey,ew,eh) in eyes:
                            if ex < x and ey < y:
                                cv2.rectangle(roi_color,(ex+ew/2,ey+eh/2),(ex+ew/2,ey+eh/2),(255, 255, 255),5)
                                #cv2.rectangle(roi_color,(ex+ew,ey+eh/2),(ex+ew,ey+eh/2),(255, 255, 255),5)
                                #cv2.rectangle(roi_color,(ex+ew/2,ey),(ex+ew/2,ey),(255, 255, 255),5)
                                #cv2.rectangle(roi_color,(ex,ey+eh/2),(ex,ey+eh/2),(255, 255, 255),5)
                                #cv2.rectangle(roi_color,(ex+ew/2,ey+eh),(ex+ew/2,ey+eh),(255, 255, 255),5)
                                  
                                eye_counter+=1
                                #print 'eye_%s : x = %s  y = %s  w = %s  h = %s'%(eye_counter,ex,ey,ew,eh)
                                if eye_counter == 2:
                                    ex_2 = ex
                                    ey_2 = ey
                                    ew_2 = ew
                                    eh_2 = eh
                                    eye_found = True
                                    eye_counter = 0
                                    #cv2.line(roi_color,(ex+ew,ey+eh/2),(ex+ew/2,ey+eh),(255, 255, 255),1)
                                    #cv2.line(roi_color,(ex+ew/2,ey),(ex+ew,ey+eh/2),(255, 255, 255),1)
                                    #cv2.line(roi_color,(ex+ew/2,ey),(ex,ey+eh/2),(255, 255, 255),1)
                                    #cv2.line(roi_color,(ex+ew/2,ey+eh),(ex,ey+eh/2),(255, 255, 255),1)
                                    if record:
                                        cv2.line(roi_color,(ex_1+ew_1/2,ey_1+eh_1/2),(ex_2+ew_2/2,ey_2+eh_2/2),(255, 255, 255),2)
                                    break
                                else:
                                    ex_1 = ex
                                    ey_1 = ey
                                    ew_1 = ew
                                    eh_1 = eh
                                    #cv2.line(roi_color,(ex+ew,ey+eh/2),(ex+ew/2,ey+eh),(255, 255, 255),1)
                                    #cv2.line(roi_color,(ex+ew/2,ey),(ex+ew,ey+eh/2),(255, 255, 255),1)
                                    #cv2.line(roi_color,(ex+ew/2,ey),(ex,ey+eh/2),(255, 255, 255),1)
                                    #cv2.line(roi_color,(ex+ew/2,ey+eh),(ex,ey+eh/2),(255, 255, 255),1)
                        for (mx,my,mw,mh) in mouth:
                            if not eye_found :
                                break
                            else:
                                #print 'mouth : x = %s  y = %s  w = %s  h = %s'%(mx,my,mw,mh)
                                if my>ey+10:
                                    cv2.rectangle(roi_color,(mx+mw/2,my+mh/2),(mx+mw/2,my+mh/2),(255, 255, 255),5)
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
                            if not mouth_found:
                                break
                            else:
                                #print 'nose : x = %s  y = %s  w = %s  h = %s'%(nx,ny,nw,nh)
                                nose_found = True
                                if (my+ey)/2>ny-10 and (ey+my)/2<ny+10:
                                    if (ex_1+ex_2)/2>nx and (ex_1+ex_2)/2>nx:
                                        cv2.rectangle(roi_color,(nx+nw/2,ny+nh/2),(nx+nw/2,ny+nh/2),(255, 255, 255),5)
                                        if record:
                                            cv2.line(roi_color,(ex_1+ew_1/2,ey_1+eh_1/2),(nx+nw/2,ny+nh/2),(255, 255, 255),2)
                                            cv2.line(roi_color,(ex_2+ew_2/2,ey_2+eh_2/2),(nx+nw/2,ny+nh/2),(255, 255, 255),2)
                                            cv2.line(roi_color,(nx+nw/2,ny+nh/2),(mx+mw/2,my+mh/2),(255, 255, 255),2)
                                        break
                        if eye_found and mouth_found and nose_found:  
                            temp_values = normal_vectors(ex_1,ey_1,eh_1,ew_1,ex_2,ey_2,eh_2,ew_2,nx,ny,nh,nw,mx,my,mh,mw)
                            if not temp_values == -1:
                                temp_values = avg_arrays()
                                name,is_good = compare.compare(temp_values,data_base,eps,num_of_values,names,percentage,num_of_rec)
                                #print "value_is good checking"
                                if is_good:
                                    cv2.putText(frame,name,(x+w/2-20,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                                    #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                                else:
                                    pass
                                    #cv2.putText(frame,"Unknown",(x+w/2-20,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                                    #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        if not record:
                            init_arrays()
                        times.append(time.time()-tic1)
                                
            except:
                #pass
                import traceback
                traceback.print_exc(sys.stdout)
            # Display the resulting frame
            cv2.imshow('Video', frame)
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print "calc_time %f"%np.mean(times)
                if record:
                    try:
                        file1 = open(name,"w")
                    except:
                        file1 = open("no_name","w")
                    '''
                    file1.write(str(numpy.mean(eye1_height)))
                    file1.write("\n")
                    file1.write(str(numpy.mean(eye1_width)))
                    file1.write("\n")
                    file1.write(str(numpy.mean(eye2_height)))
                    file1.write("\n")
                    file1.write(str(numpy.mean(eye2_width)))
                    file1.write("\n")
                    file1.write(str(numpy.mean(nose_height)))
                    file1.write("\n")
                    file1.write(str(numpy.mean(nose_width)))
                    file1.write("\n")
                    file1.write(str(numpy.mean(mouth_height)))
                    file1.write("\n")
                    file1.write(str(numpy.mean(mouth_width)))
                    file1.write("\n")
                    '''
                    file1.write(str(np.mean(eye_dist_x)))
                    file1.write("\n")
                    file1.write(str(np.mean(eye1_nose_dist_x)))
                    file1.write("\n")
                    file1.write(str(np.mean(eye2_nose_dist_x)))
                    file1.write("\n")
                    file1.write(str(np.mean(eye1_mouth_dist_x)))
                    file1.write("\n")
                    file1.write(str(np.mean(eye2_mouth_dist_x)))
                    file1.write("\n")
                    file1.write(str(np.mean(mouth_nose_dist_x)))
                    file1.write("\n")
                    file1.write(str(np.mean(eye_dist_y)))
                    file1.write("\n")
                    file1.write(str(np.mean(eye1_nose_dist_y)))
                    file1.write("\n")
                    file1.write(str(np.mean(eye2_nose_dist_y)))
                    file1.write("\n")
                    file1.write(str(np.mean(eye1_mouth_dist_y)))
                    file1.write("\n")
                    file1.write(str(np.mean(eye2_mouth_dist_y)))
                    file1.write("\n")
                    file1.write(str(np.mean(mouth_nose_dist_y)))
                    file1.write("\n")
                cv2.imwrite("./last_frame.jpeg",frame)
                break
    
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()   
