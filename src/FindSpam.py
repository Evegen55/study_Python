"""
Task:
7.2 Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
when you are testing below enter mbox-short.txt from /data folder as the file name.

"""
#for python ver 2.7
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
flo = 0
avg = 0
for line in fh:
    if (not line.startswith("X-DSPAM-Confidence:")):
        continue
    else:
        pos = line.find('.')
        numStr = line[pos-1:pos+5]
        flt = float(numStr)
        flo = flo + flt
        count = count + 1
print "Average spam confidence:", flo/count

"""
#for python ver 3.4.4

fname = input("Enter file name: ")
fh = open(fname)
count = 0
flo = 0
avg = 0
for line in fh:
    if (not line.startswith("X-DSPAM-Confidence:")):
        continue
    else:
        pos = line.find('.')
        numStr = line[pos-1:pos+5]
        flt = float(numStr)
        flo = flo + flt
        count = count + 1
print ("Average spam confidence:", flo/count)
"""
