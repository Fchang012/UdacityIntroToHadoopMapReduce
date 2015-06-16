#!/usr/bin/python
import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	
	ansSum = 0
	ansCount = 0
	qPostLen = 0
	lastID = None

	print "Question Node ID | Question Length | Average Answer Length"

	for line in reader:
		#error checking incase something went wrong
		if len(line) != 3:
			continue

		curID = line[0]
		curPostLen = float(line[1])
		curPostType = line[2]

		if lastID and lastID != curID:
			if ansCount == 0:
				ansAvg = 0
			else:
				ansAvg = ansSum/ansCount
			writer.writerow( [lastID] + [qPostLen] + [ansAvg])
			ansSum = 0
			ansCount = 0
			
		#this keeps track of the question length or the total sum and count of answers
		#to help calculate the average answer length
		if curPostType == "question":
			qPostLen = int(curPostLen)
		elif curPostType == "answer":
			ansSum = ansSum + curPostLen			
			ansCount = ansCount + 1
			
		lastID = curID

	#deals with the last output
	if ansCount == 0:
		ansAvg = 0
	else:
		ansAvg = ansSum/ansCount
	writer.writerow( [lastID] + [qPostLen] + [ansAvg])







if __name__ == "__main__":
	reducer()
