# Stop-N-Wait
Implementation of the Stop and Wait Protocol 


Project 3

This project is to be completed individually.

In this project, you are asked to implement a simulator of the Stop-n-Wait protocol we discussed in the class, in a simplified case.

The assumptions are:

There is a sender A with unlimited data to send to the receiver B.
Each data frame is 1 ms long.
The delay between A and B is 1 ms.
The time to send the ACK is negligible, that is, 0.
The timeout used by A is 2.5 ms, where, as we discussed in the class, the timeout timer starts after the last bit of the data frame is sent.
There are loss in the link, both for the data frame and ACK. Two files are given under files, namely Pj3_DATA_GOOD and Pj3_ACK_GOOD, where, in both files, each line is either ‘1’ or ‘0’, representing if the data frame or ACK is received correctly or lost, respectively.
For example, if the 10th line in DATA_GOOD is ‘1’, the 10th data frame transmitted by A is received correctly; otherwise it is lost.
Please note that it is the 10th data frame transmitted by A, and may or may not be data frame with sequence number 10, because, for example, the 10th data frame transmitted by A may be a retransmission of data frame with sequence number 9.
You can use any language you like in this project. The output of your program should be in the same format as in file pj3_sampleoutput.
