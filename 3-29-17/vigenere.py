import argparse
import sys

lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


key = ""


def decrypt(line):
	output_line = ""
	key_ind = 0
	for x in line:
		if(lower_alpha.find(x)>-1):
			output_line += lower_alpha[((lower_alpha.index(x) - upper_alpha.index(key[key_ind])) + 26) % 26]
			key_ind += 1
			key_ind %= len(key)
		elif(upper_alpha.find(x)>-1):
			output_line += upper_alpha[((upper_alpha.index(x) - upper_alpha.index(key[key_ind])) + 26) % 26]
			key_ind += 1
			key_ind %= len(key)
		else:
			output_line += x
	return output_line



def encrypt(line):
	output_line = ""
	key_ind = 0
	for x in line:
		if(lower_alpha.find(x)>-1):
			output_line += lower_alpha[(lower_alpha.index(x) + upper_alpha.index(key[key_ind])) % 26]
			key_ind += 1
			key_ind %= len(key)
		elif(upper_alpha.find(x)>-1):
			output_line += upper_alpha[(upper_alpha.index(x) + upper_alpha.index(key[key_ind])) % 26]
			key_ind += 1
			key_ind %= len(key)
		else:
			output_line += x
	return output_line
			

def remove_spaces(m_string):
	new_string = ""
	for x in m_string:
		if(x != ' '):
			new_string += x
	return new_string



parser = argparse.ArgumentParser(description='A program to encrypt and decrypt messages using the classic vigenere technique')
parser.add_argument('-e', action='store_true', help='Encrypt message (this is set by default)')
parser.add_argument('-d', action='store_true', help='Decrypyt messages')
parser.add_argument('keyarg', help='Decrypyt messages')
args = parser.parse_args()

temp_key = args.keyarg
key = remove_spaces(temp_key.upper())


line = sys.stdin.readline()
while line:
	if(args.d):
		print(decrypt(line))
	else:
		print(encrypt(line))
	line = sys.stdin.readline()

