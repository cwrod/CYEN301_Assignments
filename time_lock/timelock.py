#Author: Christopher Rodriguez

import hashlib
import datetime
import sys



#This function computes the code given a difference in seconds.
#Worst comes to absolute worst, copy paste this into terminal and manually guess time difference
def timediff_code(sdiff):

	#Hash twice
	firsthash = hashlib.md5(str(sdiff)).hexdigest()
	sechash = hashlib.md5(str(firsthash)).hexdigest()

	#It's nice to know the hash in case the form of the code changes
	print("\n" + sechash)
	
	letters = ""
	numbers = ""

	#Loop through the hash
	for i in range(0,len(sechash)):

		#Are we looking at a letter and do we still need letters?
		if(sechash[i].isalpha() and len(letters)<2): 
			#Better add it then.
			letters+=sechash[i]

		#Are we looking at a number and do we still need numbers?
		#Note that this is looking from the back 
		#i.e. When i is 0, we look at the very last character
		if(not sechash[-(i+1)].isalpha() and len(numbers)<2):
			numbers+=sechash[-(i+1)]

		#If we got everything we need, end the loop early
		#Thank god I'm saving those 5 nanoseconds, right?
		if(len(numbers)==2 and len(letters)==2):
			break
	return letters+numbers


#Read in the file for epoch time
timein = []
for line in sys.stdin:
	timein.append(line.strip())

#Epoch time parsing
etl = timein[0].split(" ")
etl = [int(x) for x in etl]

#If we get more than one line of data in, we take the second line as the current system time
#Really useful for debugging/testing
if(len(timein)==2):
	stl = timein[1].split(" ")
	stl = [int(x) for x in stl]

#a is our epoch time as a date
a = datetime.datetime(etl[0],etl[1],etl[2],etl[3],etl[4],etl[5])

#b is our current system time as a date
if(len(timein)==2):
	b = datetime.datetime(stl[0],stl[1],stl[2],stl[3],stl[4],stl[5])
else:
	b = datetime.datetime.now()


#Compute the difference in seconds
sdiff = (b-a).total_seconds()

#Integer division of 60 times 60 should give us the beginning of the valid interval
#Add and subtract hours because we never know what zone timing the server is on
sdiff_less = int(((sdiff//60)*60)-3600)
sdiff_norm = sdiff_less+3600
sdiff_more = sdiff_norm+3600
sdiff_utc = sdiff_less+3600+3600*5


#Throw the kitchen sink at it and see what hits we get
#This might involve manually entering in 4 codes wildly before our 60 seconds is up
print(timediff_code(sdiff_less) + " :3600 behind local")
print(timediff_code(sdiff_norm) + " :local")
print(timediff_code(sdiff_more) + " :3600 ahead local")
print(timediff_code(sdiff_utc)  + " :UTC")
