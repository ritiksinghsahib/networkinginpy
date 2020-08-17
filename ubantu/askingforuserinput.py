#Asking the user for some parameters: interface on which to sniff, the number of packets to sniff, the time interval to sniff, the protocol
 
#Asking the user for input - the interface on which to run the sniffer
net_iface = input("* Enter the interface on which to run the sniffer (e.g. 'enp0s8'): ")
 
#Setting network interface in promiscuous mode
'''
Wikipedia: In computer networking, promiscuous mode or "promisc mode"[1] is a mode for a wired network interface controller (NIC) or wireless network interface controller (WNIC) that causes the controller to pass all traffic it receives to the central processing unit (CPU) rather than passing only the frames that the controller is intended to receive.
This mode is normally used for packet sniffing that takes place on a router or on a computer connected to a hub.
'''
try:
    subprocess.call(["ifconfig", net_iface, "promisc"], stdout = None, stderr = None, shell = False)
 
except:
    print("\nFailed to configure interface as promiscuous.\n")
 
else:
    #Executed if the try clause does not raise an exception
    print("\nInterface %s was set to PROMISC mode.\n" % net_iface)
 
 
#Asking the user for the number of packets to sniff (the "count" parameter)
pkt_to_sniff = input("* Enter the number of packets to capture (0 is infinity): ")
 
#Considering the case when the user enters 0 (infinity)
if int(pkt_to_sniff) != 0:
    print("\nThe program will capture %d packets.\n" % int(pkt_to_sniff))
    
elif int(pkt_to_sniff) == 0:
    print("\nThe program will capture packets until the timeout expires.\n")
 
 
#Asking the user for the time interval to sniff (the "timeout" parameter)
time_to_sniff = input("* Enter the number of seconds to run the capture: ")
 
#Handling the value entered by the user
if int(time_to_sniff) != 0:
    print("\nThe program will capture packets for %d seconds.\n" % int(time_to_sniff))
    
    
#Asking the user for any protocol filter he might want to apply to the sniffing process
#For this example I chose three protocols: ARP, BOOTP, ICMP
#You can customize this to add your own desired protocols
proto_sniff = input("* Enter the protocol to filter by (arp|bootp|icmp|0 is all): ")
 
#Considering the case when the user enters 0 (meaning all protocols)
if (proto_sniff == "arp") or (proto_sniff == "bootp") or (proto_sniff == "icmp"):
    print("\nThe program will capture only %s packets.\n" % proto_sniff.upper())
    
elif (proto_sniff) == "0":
    print("\nThe program will capture all protocols.\n")
 
 
#Asking the user to enter the name and path of the log file to be created
file_name = input("* Please give a name to the log file: ")
 
#Creating the text file (if it doesn't exist) for packet logging and/or opening it for appending
sniffer_log = open(file_name, "a")