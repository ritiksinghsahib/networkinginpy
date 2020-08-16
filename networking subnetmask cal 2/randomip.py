#Generation of random IP addresses in the subnet
while True:
    generate = input("Generate random IP address from this subnet? (y/n)")
    
    if generate == "y":
        generated_ip = []
        
        #Obtain available IP address in range, based on the difference between octets in broadcast address and network address
        for indexb, oct_bst in enumerate(bst_ip_address):
            #print(indexb, oct_bst)
            for indexn, oct_net in enumerate(net_ip_address):
                #print(indexn, oct_net)
                if indexb == indexn:
                    if oct_bst == oct_net:
                        #Add identical octets to the generated_ip list
                        generated_ip.append(oct_bst)
                    else:
                        #Generate random number(s) from within octet intervals and append to the list
                        generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))
        
        #IP address generated from the subnet pool
        #print(generated_ip)
        y_iaddr = ".".join(generated_ip)
        #print(y_iaddr)
        
        print("Random IP address is: %s" % y_iaddr)
        print("\n")
        continue
        
    else:
        print("Ok, bye!\n")
        break