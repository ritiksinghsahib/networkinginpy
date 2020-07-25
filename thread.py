import threading
import time

def myfun():
    print("started!")
    time.sleep(3)
    print("ended the thread")

threads=[]
for i in range(5):
    myfun()
#for i in range():
#    th=threading.Thread(target=myfun)
###
##    th.join()
