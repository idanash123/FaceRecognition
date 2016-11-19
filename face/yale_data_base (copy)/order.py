import os
for i in range (2,16):
    folder_name = "subject"+str(i)
    os.system("cd %s;ls >a"%(folder_name))
    file1 = open(folder_name+"/a","rb")
    os.system("mkdir sub%s"%(i))
    line = file1.readline()
    line = file1.readline()
    file_cnt = 1
    while not line =="":
        pos = line.find(".")
        end = line[pos:]
        end = end[:-1]
        os.system("cd %s;mv %s %s"%(folder_name,line[:-1],str(file_cnt)+str(end)))
        line = file1.readline()
        file_cnt+=1
    os.system("cd %s;rm a;mogrify -format jpg *.*"%(folder_name))
    os.system("cp %s/*.jpg sub%s/"%(folder_name,i))
    