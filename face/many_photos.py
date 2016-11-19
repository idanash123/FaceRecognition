import os,time
from thread import start_new_thread
os.system("cd photos;ls >a")
file1 = open("photos/a","rb")
line = file1.readline()
line = file1.readline()
cnt = 0
while not line == "":
    start_new_thread(os.system , ("python find_in_photo.py photos/%s %s"%(line[:-1],line[:-1]),))
    #os.system("python find_in_photo.py photos/%s %s"%(line[:-1],line[:-1]))
    line = file1.readline()
    cnt += 1
    if cnt == 3:
        time.sleep(5)
        cnt = 0

