# example of word_count program
# 3.10.2015 jsa

# import needed libraries
import sys
import os
import re

# open input output files
path = sys.argv[1]
files = os.listdir(path)
files = sorted(files)
outfile=open(sys.argv[2],"w+")
#print path, files, outfile


wordcount={}     #use dictionary

#process each file in given directory
for file in files:

	# only process .txt files (because I wanted to put large files in here too)
	if file[-3:] == "txt":   

        	print "Wordcount processing " + path + file
        	infile=open(path + file,"r+")
	
		# count words in each line
		#remove punctuation and lowercase the words here
		for word in (re.findall(r'\w+',infile.read().lower())): 
		    if word not in wordcount: wordcount[word] = 1
		    else: 		      wordcount[word] += 1
	
		#close file
		infile.close();


# write output to file
for item in sorted(wordcount.items()): 
	outfile.write(("{}\t{}\n").format(*item))
	

# close file
outfile.close();


