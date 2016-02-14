"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent 
the greatest number of mail messages. The program looks for 'From ' lines and takes 
the second word of those lines as the person who sent the mail. The program creates
a Python dictionary that maps the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads through
the dictionary using a maximum loop to find the most prolific committer.
"""
#for python ver 2.7
name = raw_input("Enter file:")
if len(name) < 1 : name = "../data/mbox-short.txt"
handle = open(name)
d = dict()
count = 0
for line in handle:
    splt = line.split()
    if len(splt) == 0 : continue
        #find a sender
    if splt [0] != 'From' : continue
    try:
        fr = splt[1]
        #test code
        #print fr
        if (not fr in d.keys()):
            #test code
            #print 'a'
            d[fr] = 1
        else:
            d[fr] = d[fr] + 1
    except:
        print 'No data element at index sub-2'
        continue
#test code
#print d
for k,v in d.items():
    if v>count:
        count = v
for k,v in d.items():
    if v == count:
        print k,v
