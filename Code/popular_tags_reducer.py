#!/usr/bin/python
import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	#top 10 array creation
	topTenA = ['None']*10
	topTenB = [0]*10
	topTen = [topTenA, topTenB]
	tempA = None
	tempB = 0

	lastTag = None
	count = 0

	print "Tag | FrequencyCount"
	for line in reader:
		curTag = line[0]
		curID = line[1]
			

		if lastTag and lastTag != curTag:
			#At the time the tag changes, it takes the previous tag and count
			#and compares it to the current top 10 list. If its greater than or 
			#equal, it replaces it at that current spot and then shifts the rest down a spot. 
			for i in range(10):
				if count >= topTen[1][i]:
					tempA = topTen[0][i]
					tempB = topTen[1][i]
					topTen[0][i] = lastTag
					topTen[1][i] = count
					lastTag = tempA
					count = tempB

			count = 0					
			
		lastTag = curTag
		count = count + 1

	#deals with last entries
	if curID != None:
		for i in range(10):
			if count >= topTen[1][i]:
				tempA = topTen[0][i]
				tempB = topTen[1][i]
				topTen[0][i] = lastTag
				topTen[1][i] = count
				lastTag = tempA
				count = tempB

	for j in range(10):
		writer.writerow( [str(topTen[0][j])] + [str(topTen[1][j])] )



if __name__ == "__main__":
	reducer()
