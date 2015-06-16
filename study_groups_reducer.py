#!/usr/bin/python
import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	lastID = None
	authorList = []

	print "Question Node ID |Student IDs"
	#Logic of this is it creates a empty list of authors and adds to it until a new node is detected.
	#It then writes out the list along with the ID name and then resets it back to a empty list.
	for line in reader:
		
		curID, curAuthor, curPostType = line
		
		if lastID and lastID != curID:
			writer.writerow( [lastID] + [authorList] )
			authorList = []
			

		authorList.append(curAuthor)
		lastID = curID

	if lastID != None:
		writer.writerow( [lastID] + [authorList] )



if __name__ == "__main__":
	reducer()
