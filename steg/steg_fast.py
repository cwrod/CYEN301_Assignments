#Author: Christopher Rodriguez


import sys


#Default values
bitmethod = True
storedata = True
offset = 0
interval = 1
wrapper = ""
hidden = ""


#Read the flags
for x in range(1,len(sys.argv)):
	lin = sys.argv[x][2:]
	flag = sys.argv[x][:2]
	if('-b' in flag):
		bitmethod = True
	elif('-B' in flag):
		bitmethod = False
	elif('-s' in flag):
		storedata = True
	elif('-r' in flag):
		storedata = False
	elif('-o' in flag):
		offset = int(lin)
	elif('-i' in flag):
		interval = int(lin)
	elif('-w' in flag):
		wrapper = lin
	elif('-h' in flag):
		hidden = lin

#Default for sentinel bytes
#Note that I am storing integers, not bytes
sentinel_bytes = [0x0,0xFF,0x0,0x0,0xFF,0x0]



#Hiding messages
if(storedata):

	#Read the file you intend to hide and save the bytes as binary numbers
	hidden_bin = []
	with open(hidden, "rb") as f:
		byte = f.read(1)
		while byte != "":
			hidden_bin.append(''.join('{0:08b}'.format(x, 'b') for x in bytearray(byte)))
			byte = f.read(1)

	#Make sure you include the sentinel bytes at the end
	for sbyt in sentinel_bytes:
		hidden_bin.append((''.join('{0:08b}'.format(x, 'b') for x in bytearray(chr(sbyt)))))


	

	#Read the bytes you want to wrap your message in
	storage_bin = []
	with open(wrapper, "rb") as f:
		byte = f.read(1)
		while byte != "":
			storage_bin.append(''.join('{0:08b}'.format(x, 'b') for x in bytearray(byte)))
			byte = f.read(1)

	
	#Make changes to the wrapper that reflect the hidden message
	for i,x in enumerate(hidden_bin):
		if(bitmethod):
			#Loop through each bit of the current hidden message byte
			for biti in range(0,len(x)):
				#Location of the wrapper byte we want to hide the message byte in
				bitloc = offset+i*8*interval+biti*interval

				#Just edit the last bit
				storage_bin[bitloc] = storage_bin[bitloc][0:len(storage_bin[bitloc])-1]+x[biti]
		else:
			#Change the whole byte to the hidden messsage byte
			storage_bin[offset+i*interval]=x
	
	#Print out our hidden message
	for bito in storage_bin:
		sys.stdout.write(chr(int(bito,2)))



#Retrieving data
#Probably where we need to be editing in cyber storm
else: 
	storage_bin = [] #Last 8 bytes that we read
	byte_count = 0 #How many bytes of the wrapper we have gone through
	i = 0 #How many bytes we have got of the hidden message


	with open(wrapper, "rb") as f:
		byte = f.read(1)
		if(bitmethod):
			cur_byte = ''
			while byte != "" and sentinel_bytes != storage_bin:
				#Did the byte we just read contain a hidden bit in its Least Significant Bit?
				if byte_count == offset + i*8*interval + len(cur_byte)*interval:
					
					#Add the last bit of the wrapper byte to the current message byte
					cur_byte += ''.join('{0:08b}'.format(x, 'b') for x in bytearray(byte))[7]
					
					#If our current message byte is 8 characters, we are done with that message byte
					if len(cur_byte) == 8:
						
						#Make sure that our storage bin shows the sentinel bits when we get to them
						if(len(storage_bin)==len(sentinel_bytes)):
							storage_bin.pop(0)
						storage_bin.append(int(cur_byte,2))

						#Write out the message byte we got and start over
						sys.stdout.write(chr(int(cur_byte,2)))
						cur_byte = ''
						i += 1
				#Increment byte count every time we read a byte no matter what
				byte_count += 1
				byte = f.read(1)
		else:
			while byte != "" and sentinel_bytes != storage_bin:
				#Is this byte a secret message byte?
				if byte_count == offset + i*interval:

					#Make sure our storage bin is storing the potential sentinel bytes
					if(len(storage_bin)==len(sentinel_bytes)):
						storage_bin.pop(0)
					storage_bin.append(ord(byte))

					#Write out the hidden message byte
					sys.stdout.write(byte)
					i += 1
				#Increment byte count every time we read a byte no matter what
				byte_count += 1
				byte = f.read(1)
