#Author Christopher Rodriguez

import sys
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


bin_string = ""
for line in sys.stdin:
	bin_string = bin_string + line.strip()

print(decode_bin(bin_string))
