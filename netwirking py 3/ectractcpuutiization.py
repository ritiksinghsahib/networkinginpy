#Checking command output for IOS syntax errors
        router_output = connection.recv(65535)
        
        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} :(".format(ip))
            
        else:
            print("\nDONE for device {}. Data sent to file at {}.\n".format(ip, str(datetime.datetime.now())))
            
        #Test for reading command output
        #print(str(router_output) + "\n")
        
        #Searching for the CPU utilization value within the output of "show processes top once"
        cpu = re.search(b"%Cpu\(s\):(\s)+(.+?)(\s)* us,", router_output)
        
        #Extracting the second group, which matches the actual value of the CPU utilization and decoding to the UTF-8 format from the binary data type
        utilization = cpu.group(2).decode("utf-8")
        
        #Printing the CPU utilization value to the screen
        #print(utilization)
        
        #Opening the CPU utilization text file and appending the results
        with open("D:\\App3\\cpu.txt", "a") as f:
            #f.write("{},{}\n".format(str(datetime.datetime.now()), utilization))
            f.write(utilization + "\n")