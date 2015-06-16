#!/usr/bin/python
import sys
import csv
import string

def getTags(theLine):
	return theLine.strip().split()


def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	for line in reader:
		if len(line) == 19:
			#skips header
			if str(line[0]).isdigit():
				#This will find all the post types that are either question, answer, or comment.
				#It then strips and splits out each tag and posts them along with their node ID.
				if line[5].lower().strip() == "question":
					for word in range(len(getTags(line[2]))):
						writer.writerow( [getTags(line[2])[word]] + [line[0]])
				elif line[5].lower().strip() == "answer" or line[5].lower().strip() == "comment":
					for word in range(len(getTags(line[2]))):
						writer.writerow( [getTags(line[2])[word]] + [line[6]])





if __name__ == "__main__":
	mapper()
