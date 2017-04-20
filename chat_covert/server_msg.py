import socket
import time
from binascii import hexlify
import random

covert = "could this theoretically produce 1.5 and 1.9? or would it only ever produce 1.50~1 and 1.89~?" + "EOF"
covert_bin = ""
for i in covert:
	covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)
print(covert_bin)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1337
s.bind(("", port))
s.listen(0)
c, addr = s.accept()


ZERO = 0.01
ONE = 0.1
msg = "Some message..." 
n = 0
for x in range(0,len(covert_bin)):
	i = msg[x%len(msg)]
	c.send(i)
	if (covert_bin[n] == "0"):
		time.sleep(ZERO+random.uniform(0,.051))
	else:
		time.sleep(ONE+random.uniform(0,.051))
	n = (n + 1) % len(covert_bin)
c.send("EOF")
c.close()

