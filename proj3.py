#proj3 Chesleah Kribs 
 


def sender(time, sACK, sFrame, transmitStat, ACKStat):

	if int(transmitStat):
		#means there was a good transmision
		messagestat = 'good transmission '
	else:
		#means there was a bad transmission
		messagestat = 'bad transmission'

	#print messagestat

	if int(ACKStat):
		print('time ' + str(time) + '00000: sender got ACK' + str(sACK) + ', transmitting new frame: ' + messagestat)
		sACK = sACK + 1
	else: 
		print('time ' + str(time) + '00000: sender time out on frame ' + str(sFrame) + ', retransmitting it: ' + messagestat)

	if int(transmitStat): 
		time = time + 2.0 
	else:
		time = time + 3.5

	return time, sACK, sFrame

def receiver(time, sACK, sFrame, transmitStat):
	if int(transmitStat):
		messagestat = 'good transmission '
	else: 
		messagestat = 'bad transmission ' 

	print('time ' + str(time) + '00000: receiver got frame ' + str(sFrame) + ', transmitting ACK' + str(sACK) + ': ' + messagestat)


def StopAndWait(ACK, frames):
	#starting values
	time = 0.0
	sACK = 0
	sFrame = 0
	ACKStat = 1
	transmitStat = 1

	while frames:
		transmitStat = frames.pop(0)
		time, sACK, sFrame = sender(time, sACK, sFrame, transmitStat, ACKStat)

		ACKStat = 0

		#sender
		#for a good transmission! 
		if(int(transmitStat)): 
			transmitStat = ACK.pop(0)
			receiver(time, sACK, sFrame, transmitStat)

			#receiver
			#good transmission
			if(int(transmitStat)):
				sFrame = sFrame + 1
				ACKStat = 1
				time = time + 1.0
			else: 
				time = time + 1.5





#check for blank lines 
ACK = []

f = open("Pj3_ACK_GOOD")
for elem in f:
	fileACK = elem.strip("\n ")

	if fileACK:
		ACK.append(fileACK)
	else:
		continue

#print ACK


# check for blank lines 
frames = []
f = open("Pj3_DATA_GOOD")
for elem in f:
	dataframes = elem.strip("\n ")

	if dataframes:
		frames.append(dataframes)
	else:
		continue

#print "This is now the frames\n"
#print frames

StopAndWait(ACK, frames)



