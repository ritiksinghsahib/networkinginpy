#Convert IP to binary string
ip_octets_binary = []
 
for octet in ip_octets:
    binary_octet = bin(int(octet)).lstrip('0b')
    #print(binary_octet)
    
    ip_octets_binary.append(binary_octet.zfill(8))
        
#print(ip_octets_binary)
#Example: for 192.168.10.1 => 
 
binary_ip = "".join(ip_octets_binary)
 
#print(binary_ip)   
#Example: for 192.168.2.100 => 11000000101010000000101000000001
 
#Getting the network address and broadcast address from the binary strings obtained above
 
network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
#print(network_address_binary)
 
broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
#print(broadcast_address_binary)
 
#Converting everything back to decimal (readable format)
net_ip_octets = []
 
#range(0, 32, 8) means 0, 8, 16, 24
for bit in range(0, 32, 8):
    net_ip_octet = network_address_binary[bit: bit + 8]
    net_ip_octets.append(net_ip_octet)
 
#We will end up with 4 slices of the binary IP address: [0: 8], [8: 16], [16: 24] and [24:31]; remember that each slice goes up to, but not including, the index on the right side of the colon!
 
#print(net_ip_octets)
 
net_ip_address = []
 
for each_octet in net_ip_octets:
    net_ip_address.append(str(int(each_octet, 2)))
    
#print(net_ip_address)
 
network_address = ".".join(net_ip_address)
#print(network_address)
 
bst_ip_octets = []
 
#range(0, 32, 8) means 0, 8, 16, 24
for bit in range(0, 32, 8):
    bst_ip_octet = broadcast_address_binary[bit: bit + 8]
    bst_ip_octets.append(bst_ip_octet)
 
#print(bst_ip_octets)
 
bst_ip_address = []
 
for each_octet in bst_ip_octets:
    bst_ip_address.append(str(int(each_octet, 2)))
    
#print(bst_ip_address)
 
broadcast_address = ".".join(bst_ip_address)
#print(broadcast_address)
 
#Results for selected IP/mask
print("\n")
print("Network address is: %s" % network_address)
print("Broadcast address is: %s" % broadcast_address)
print("Number of valid hosts per subnet: %s" % no_of_hosts)
print("Wildcard mask: %s" % wildcard_mask)
print("Mask bits: %s" % no_of_ones)
print("\n")