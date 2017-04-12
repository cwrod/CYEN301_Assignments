#Author Christopher Rodriguez

import ftplib
import sys


#These are the printable ASCII characters in order as they are on the table
ASCII_TABLE = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

#This method converts a binary string with either 7 or 8 bits to ASCII
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

	
#This method determines what encoding is best (7 or 8) for a binary string and then converts it to ASCII
#This turned out to be unnecessary for the class challenge (as we were told 7 character encoding)
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



#This converts a file permission to an ASCII character
#If there is anything but a dash in the first 3 characters, return with a 0
#Otherwise, return a 7 bit binary string that is converted to ASCII
#Not used for this challenge
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


#Convert a whole directory of file permissions to an ASCII line
def all_conv(full_string):
	bin_string = ''
	#Basic core of our program
	#If a file permission has a dash, change it to a 0
	#If it has anything else, change it to a 1
	for i,x in enumerate(full_string):
		if x=='-':
			bin_string += '0'
		else:
			bin_string += '1'
	#Translate the binary string
	return decode_bin(bin_string)


#Address is hardcoded in for our challenge
ftp = ftplib.FTP("192.168.1.100")
ftp.login("anonymous", "ftplib-example-1")

data = []
#Change to the incoming directory (WILL BE DIFFERENT FOR OTHER CHALLENGES)
ftp.cwd('incoming')
ftp.dir(data.append)

ftp.quit()

plaintext = ""


full_string = ''

#We need to format the result of a directory listing so that we just get a list of file permissions
for line in data:
	full_string += line.split(' ')[0]

#Make sure the listing is divisible by 7
while(len(full_string)%7!=0):
	full_string+='-'

	
plaintext += all_conv(full_string)
print(plaintext)		
