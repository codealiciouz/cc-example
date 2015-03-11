# example of running median program
# 3.10.2015 jsa

# import needed libraries
import sys #for arg handling
import re  #regex
import os  #for file handling

# used median function to avoid possible issues with numpy,statistics,etc
def median(values):
    values = sorted(values)
    if len(values) < 1:
            return None
    if len(values) %2 == 1:
            return values[((len(values)+1)/2)-1]
    if len(values) %2 == 0:
            return float(sum(values[(len(values)/2)-1:(len(values)/2)+1]))/2.0

# open input output files
path = sys.argv[1]
files = os.listdir(path)
files = sorted(files)
outfile=open(sys.argv[2],"w+")
#print path, files, outfile

wordcount=[]
median_value=[]

#process each file in given directory
for file in files:

    	# only process .txt files (because I wanted to put large files in here too)
        if file[-3:] == "txt":

		print "Median processing " + path + file
		infile=open(path + file,"r+")

		# count number of words in each line
		for i,line in enumerate(infile):
			count = len(re.findall(r'\w+',line.lower()))
			wordcount.insert(0,count)
			mwc = median(wordcount) 
			median_value.append(mwc)
	
			#write value each time
			#tradeoff - can write all values at end, but there would be 
			#no way of checking status (via tail -f) for large files
			outfile.write("%0.1f\n" %mwc)  
	
			#debugging
			#print count, wordcount[i], i,line
			#print wordcount, median_value

		# close file
		infile.close();


# close file
outfile.close();



