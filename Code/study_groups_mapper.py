#!/usr/bin/python
import sys
import csv

def cleanText(theLine):
	return theLine.strip()

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	for line in reader:
		if len(line) == 19:
			#skips header
			if str(line[0]).isdigit():
				#Prints out the NodeID, author, and node_type
				if cleanText(line[5].lower()) == "question":
					writer.writerow( [ cleanText(line[0]) ] + [ cleanText(line[3]) ] + [ cleanText(line[5].lower()) ] )
				elif cleanText(line[5].lower()) == "answer" or cleanText(line[5].lower()) == "comment":
					writer.writerow( [ cleanText(line[6]) ] + [ cleanText(line[3]) ] + [ cleanText(line[5].lower()) ] )








if __name__ == "__main__":
	mapper()
