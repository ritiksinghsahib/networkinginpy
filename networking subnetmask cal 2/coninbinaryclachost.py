#Algorithm for subnet identification, based on IP and Subnet Mask
 
#Convert mask to binary string
mask_octets_binary = []
 
for octet in mask_octets:
    binary_octet = bin(int(octet)).lstrip('0b')
    #print(binary_octet)
    
    mask_octets_binary.append(binary_octet.zfill(8))
        
#print(mask_octets_binary)
 
binary_mask = "".join(mask_octets_binary)
#print(binary_mask)   
#Example: for 255.255.255.0 => 11111111111111111111111100000000
 
#Counting host bits in the mask and calculating number of hosts/subnet
no_of_zeros = binary_mask.count("0")
no_of_ones = 32 - no_of_zeros
no_of_hosts = abs(2 ** no_of_zeros - 2) #return a positive value for the /32 mask (all 255s)
 
#print(no_of_zeros)
#print(no_of_ones)
#print(no_of_hosts)
 
#Obtaining wildcard mask
wildcard_octets = []
 
for octet in mask_octets:
    wild_octet = 255 - int(octet)
    wildcard_octets.append(str(wild_octet))
    
#print(wildcard_octets)
 
wildcard_mask = ".".join(wildcard_octets)
#print(wildcard_mask)