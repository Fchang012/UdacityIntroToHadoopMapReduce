#!/usr/bin/python
import sys
import csv
from datetime import datetime

def getTimeStamp(theLine):
	return theLine[8:9]

def cutTimeZ(TZStamp):
	return TZStamp[2:21]

def returnTime(TS):
	return datetime.strptime(cutTimeZ(TS), "%Y-%m-%d %H:%M:%S")

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	
	for line in reader:
		if len(line) == 19:
			#skips header
			if str(line[0]).isdigit():
				#Parsing out "author_id": and "added_at" and then getting out the hour from the time stamp from "added_at"
				tempTS = str(getTimeStamp(line))
				TShour = returnTime(tempTS).hour
				print int(line[3]), "\t", TShour






if __name__ == "__main__":
	mapper()

