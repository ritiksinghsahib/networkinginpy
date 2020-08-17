#Printing an informational message to the screen
print("\n* Starting the capture...)
 
 
#Running the sniffing process (with or without a filter)
if proto_sniff == "0":
    sniff(iface = net_iface, count = int(pkt_to_sniff), timeout = int(time_to_sniff), prn = packet_log)
 
elif (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp"):
    sniff(iface = net_iface, filter = proto_sniff, count = int(pkt_to_sniff), timeout = int(time_to_sniff), prn = packet_log)
    
else:
    print("\nCould not identify the protocol.\n")
 
#Printing the closing message
print("\n* Please check the %s file to see the captured packets.\n