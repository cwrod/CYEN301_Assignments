#Author Christopher Rodriguez

import ftplib
import argparse
import sys

ASCII_TABLE = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'




parser = argparse.ArgumentParser(description='Discover the secret message hidden in an ftp server')
parser.add_argument('-f', action='store_true', help='Use the full ten bits of file permissions. The default is to ignore the first 3 permission flags.')
args = parser.parse_args()





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
		if(ASCII(bin_string,7)==0):
			return ASCII(bin_string,8)
		else:
			return ASCII(bin_string,7)
	elif(len(bin_string) % 7 == 0):
		return ASCII(bin_string,7)
	elif(len(bin_string) % 8 == 0):
		return ASCII(bin_string,8)



def ignore_3_conv(line):
	bin_string = ''
	for i,x in enumerate(line):
		if i<3:
			if x!='-':
				return 0
		elif x=='-':
			bin_string += '0'
		else:
			bin_string += '1'
	return decode_bin(bin_string)


def all_conv(full_string):
	bin_string = ''
	for i,x in enumerate(full_string):
		if x=='-':
			bin_string += '0'
		else:
			bin_string += '1'
	return decode_bin(bin_string)



ftp = ftplib.FTP("jeangourd.com")
ftp.login("anonymous", "ftplib-example-1")

data = []
if args.f:
	ftp.cwd('10')
else:
	ftp.cwd('7')
ftp.dir(data.append)

ftp.quit()

plaintext = ""


if args.f:
	full_string = ''
	for i,line in enumerate(data):
		full_string += line.split(' ')[0]
	while(len(full_string)%7!=0):
		full_string+='-'
	plaintext += all_conv(full_string)
else:
	for line in data:
		line = line.split(' ')[0]
		if ignore_3_conv(line) != 0:
			plaintext+=ignore_3_conv(line)


print(plaintext)		
