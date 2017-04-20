import sys
from time import time
import socket


ASCII_TABLE = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'


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
			return 0
	return ret_str

def decode_bin(bin_string):
	if(len(bin_string) % (7*8) == 0):
		if(ASCII(bin_string,8)==0):
			return ASCII(bin_string,7)
		else:
			return ASCII(bin_string,8)
	elif(len(bin_string) % 7 == 0):
		return ASCII(bin_string,7)
	elif(len(bin_string) % 8 == 0):
		return ASCII(bin_string,8)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("",1337))

data=""
i = 0
times = []
data = s.recv(4096)
print(data)
while (data.rstrip("\n") != "EOF"):
	t0 = time()
	data = s.recv(4096)
	t1 = time()
	times.append(t1-t0)

average = sum(times) / float(len(times))
bin_str = ""
print(average)
for i in times:
	if i < average:
		bin_str = bin_str+"0"
	else:
		bin_str = bin_str+"1"
print(bin_str)
print(decode_bin(bin_str))
s.close()

