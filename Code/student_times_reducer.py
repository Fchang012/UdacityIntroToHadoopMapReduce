#!/usr/bin/python
import sys
import csv


def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')

	#hourList creates a list with 24 Zeros to represent the count of each hour for each poster.
	hourList = [0] * 24
	lastPoster = None	
	
	print "Poster:", "\t", "Hour Most Active:"
	
	for line in reader:
		#error checking incase something went wrong
		if len(line) != 2:
			continue		

		#sets the current poster and the current hour
		curPoster = int(line[0])
		curHour = int(line[1])

		if lastPoster and lastPoster != curPoster:
			#This part of the code will go through the current hourList and find the max value in it.
			#It then goes and finds the indexes of where the max values occur.
			maxVal = max(hourList)
			hours = [index for index, val in enumerate(hourList) if val == maxVal]
			for i in range(len(hours[:])):
				sys.stdout.write(str(lastPoster) + "\t" + str(hours[i]) + "\n")
			hourList = [0] * 24
		
		lastPoster = curPoster	
		hourList[curHour] = hourList[curHour] + 1	

	#deals with last record
	if lastPoster != None:
		maxVal = max(hourList)
		hours = [index for index, val in enumerate(hourList) if val == maxVal]		
		sys.stdout.write(str(lastPoster) + "\t" + str(hours[i]) + "\n")





if __name__ == "__main__":
	reducer()

