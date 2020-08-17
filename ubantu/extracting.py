#This is the function that will be called for each captured packet
#The function will extract parameters from the packet and then log each packet to the log file
def packet_log(packet):
    
    #Getting the current timestamp
    now = datetime.now()
    
    #Writing the packet information to the log file, also considering the protocol or 0 for all protocols
    if proto_sniff == "0":
        #Writing the data to the log file
        print("Time: " + str(now) + " Protocol: ALL" + " SMAC: " + packet[0].src + " DMAC: " + packet[0].dst, file = sniffer_log)
        
    elif (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp"):
        #Writing the data to the log file
        print("Time: " + str(now) + " Protocol: " + proto_sniff.upper() + " SMAC: " + packet[0].src + " DMAC: " + packet[0].dst, file = sniffer_log)