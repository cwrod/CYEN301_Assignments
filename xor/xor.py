#Author: Christopher Rodriguez

import sys


#Read bytes from stdin as their integer representation
in_bits = []
for line in sys.stdin:
	for byte in line:
		in_bits.append(ord(byte))


#Read bytes from key file as their integer representation
key_bits = []
with open('key', "rb") as f:
	byte = f.read(1)
	while byte != "":
		key_bits.append(ord(byte))
		byte = f.read(1)

#XOR the in byte with the key byte
#Then print out the corresponding ASCII character
for i in range(0,len(in_bits)):
	sys.stdout.write(chr(in_bits[i]^key_bits[i]))

