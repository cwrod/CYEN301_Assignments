import sys
import pxssh
import os
from os import write
import subprocess
import time
import pipes

user = "vortex1"
host = "vortex.labs.overthewire.org"
password = "Gq#qu3bF3"
remote_commands = """scp afile.file user@serverip: path of server directory
pwd
"""
sshCommand = " ssh -t -t %s@%s" % (user, host)
process1 = subprocess.Popen(sshCommand, shell=True, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
time.sleep(5)
print(process1.pid)
write(process1.pid, password + b'\n')
stdout_data = process1.stdin.write(password+b'\n')
#out, err = process1.communicate(input=password)
print("este")
process1.stdin.close()
time.sleep(10)
