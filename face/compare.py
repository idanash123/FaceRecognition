import time,sys,cv2,numpy,math

def main():
    eps = 0.001
    num_of_values = 12
    prc = 0.0
    file1 = open (sys.argv[1],'rb')
    file2 = open (sys.argv[2],'rb')
    line1 = file1.readline()
    line2 = file2.readline()
    while not line1 == "":
        ret = abs(float(line1) - float(line2))
        if ret< eps:
           prc += 100/float(num_of_values)
        else:
            if (100/float(num_of_values)*(int(ret/eps)/10)) >(100/float(num_of_values)):
                pass
            else:
                prc += (100/float(num_of_values))-(100/float(num_of_values)*(int(ret/eps)/10))
        line1 = file1.readline()
        line2 = file2.readline()
    print prc
'''
def compare(comparing_values,data_base,eps,num_of_values,names,percentage,num_of_rec):
    prc = 0.0
    for i in range(len(names)):
        for j in range (1,num_of_rec+1):
            for t in range (num_of_values):
                if (float(data_base[names[i]][j][t]) > float(comparing_values[t])):
                    prc+= (float(comparing_values[t]) / float(data_base[names[i]][j][t]))*(100/float(num_of_values))
            print names[i]
            print prc
            if prc >=percentage :
                return names[i],True
            prc = 0.0
    return "",False
'''
def compare(comparing_values,data_base,eps,num_of_values,names,percentage,num_of_rec):
    prc = 0.0
    for i in range(len(names)):
        for j in range (1,num_of_rec+1):
            for t in range (num_of_values):
                ret = abs(float(data_base[names[i]][j][t]) - float(comparing_values[t]))
                if ret< eps:
                   prc += 100/float(num_of_values)
                else:
                    if (100/float(num_of_values)*(int(ret/eps)/10)) >(100/float(num_of_values)):
                        pass
                    else:
                        prc += (100/float(num_of_values))-(100/float(num_of_values)*(int(ret/eps)/10))
            print names[i]
            print prc
            if prc >=percentage :

                return names[i],True
            prc = 0.0
    return "",False
if __name__ == '__main__':
    main()   
