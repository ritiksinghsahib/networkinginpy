import time
 
#the rest of the code in NetworkApp.py
 
#Calling threads creation function for one or multiple SSH connections
while True:
    create_threads(ip_list, ssh_connection)
    time.sleep(10)