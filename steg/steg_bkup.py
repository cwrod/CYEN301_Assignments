import sys


bitmethod = True
storedata = True
offset = 0
interval = 1
wrapper = ""
hidden = ""


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

sentinel_bytes = [chr(0x0),chr(0xFF),chr(0x0),chr(0x0),chr(0xFF),chr(0x0)]



if(storedata):
	hidden_bytes = []
	with open(hidden, "rb") as f:
		byte = f.read(1)
		while byte != "":
			hidden_bytes.append(byte)
			byte = f.read(1)
	hidden_bytes.extend(sentinel_bytes)
	hidden_bin = []
	for sbyte in hidden_bytes:
		hidden_bin.append((''.join('{0:08b}'.format(x, 'b') for x in bytearray(sbyte))))
	

	storage_bytes = []
	with open(wrapper, "rb") as f:
		byte = f.read(1)
		while byte != "":
			storage_bytes.append(byte)
			byte = f.read(1)
	storage_bin = []
	for sbyte in storage_bytes:
		storage_bin.append((''.join('{0:08b}'.format(x, 'b') for x in bytearray(sbyte))))
	
	for i,x in enumerate(hidden_bin):
		if(bitmethod):
			for biti in range(0,len(x)):
				bitloc = offset+i*8*interval+biti
				storage_bin[bitloc] = storage_bin[bitloc][0:len(storage_bin[bitloc])-1]+x[biti]
		else:
			storage_bin[offset+i*interval]=x
	
	for bito in storage_bin:
		sys.stdout.write(chr(int(bito,2)))


else:
	storage_bytes = []
	with open(wrapper, "rb") as f:
		byte = f.read(1)
		while byte != "":
			storage_bytes.append(byte)
			byte = f.read(1)
	storage_bin = []
	for sbyte in storage_bytes:
		storage_bin.append((''.join('{0:08b}'.format(x, 'b') for x in bytearray(sbyte))))
	
	sent_bin = ''.join('{0:08b}'.format(x, 'b') for x in bytearray(sentinel_bytes))
	mbin = []
	i = 0
	while sent_bin not in ''.join(mbin[-len(sent_bin):]):	
		mbin.append('')
		if(bitmethod):
			for biti in range(0,8):
				bitloc = offset+i*8*interval+biti
				mbin[i]+=storage_bin[bitloc][len(storage_bin[bitloc])-1]
			print("TEST")
		else:
			mbin[i]=storage_bin[offset+i*interval]
		i = i+1
	for bito in mbin[:-7]:
		sys.stdout.write(chr(int(bito,2)))


