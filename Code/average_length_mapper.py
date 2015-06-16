#!/usr/bin/python
import sys
import csv
import string


def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')

	for line in reader:
		if len(line) == 19:
			#skips header
			if str(line[0]).isdigit():
				#Prints out the correct ID for either the question or answer, then length of body, and then the type of post it is.
				if line[5].lower() == "question":
					print line[0].strip(), "\t", len(line[4]), "\t", line[5].lower().strip() 
				elif line[5].lower() == "answer":
					print line[6].strip(), "\t", len(line[4]), "\t", line[5].lower().strip()










if __name__ == "__main__":
	mapper()
