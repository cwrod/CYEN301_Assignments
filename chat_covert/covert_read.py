#This program is designed to decode a secret message based on timing delays in a chat server using a socket connection.

#Usage: python chat_covert [IPADDRESS] [PORT] [f/b]
#Example: python chat_covert 138.47.102.193 31337 f

#Author:Chris Rodriguez of Team Chamaeleon
import sys
from time import time
import socket


ASCII_TABLE = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

#Simple function to decode a binary string given whether its 7 bit or 8 bit
def ASCII(bin_string,encode):
	ret_str = ""
	for i in range(0,len(bin_string)/encode):
		n_byte = int(bin_string[i*encode:(i+1)*encode],2)
		if(n_byte==8):
			ret_str = ret_str[:-1]
		elif(n_byte==9):
			ret_str = ret_str+"\t"	
		elif(n_byte==10):
			ret_str = ret_str+"\n"	
		elif(n_byte==13):
			ret_str = ret_str+"\r"
		elif(n_byte==0):
			ret_str = ret_str
		elif(n_byte>31 and n_byte<127):
			ret_str = ret_str+ASCII_TABLE[n_byte-32]
		else:
			ret_str = ret_str
	return ret_str




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the IP and port as given in the command line
s.connect((sys.argv[1],int(sys.argv[2])))

data=""
i = 0
times = []
data = s.recv(4096)
print(data)

#Read the data as it's coming in
while (data.rstrip("\n") != "EOF"):
	t0 = time()
	data = s.recv(4096)
	#Make sure we only have one character in our data string 
	if(len(data) == 1):
		t1 = time()
		#Append the time it took to get the data to the times list
		times.append(t1-t0)
	else:
		#If we don't have just one character, just feed in 0 for all the bits
		for d in range(1,len(data)):
			times.append(0)
	print(data)

#Calculate the average time of our method
average = sum(times) / float(len(times))
bin_str = ""

#Should we read long times as 1 or 0?
bit_order = sys.argv[3]=='f'

#If the time delay is less than the average, use a 0 (or a 1 if the f flag isn't set)
#Otherwise, use the other digit
for i in times:
	if((i < average) and (bit_order)):
		bin_str = bin_str+"0"
	else:
		bin_str = bin_str+"1"

#Throw the kitchen sink at it. Let's check both 7 bit and 8 bit
print(ASCII(bin_str,7))
print(ASCII(bin_str,8))

#Close our socket connection
s.close()

