"""
10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then 
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below.
"""
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
l = list()
count = 0
for line in handle:
    splt = line.split()
    if len(splt) == 0 : continue
        #find a sender
    if splt [0] != 'From' : continue
    try:
        spltHour = splt[5].split(':')
        #print splt[5]
        #print spltHour[0]
        #if you want to make a float type from string
        #hour = float(spltHour[0])
        #if not
        hour = spltHour[0]
        if (not hour in d.keys()):
            d[hour] = 1
        else:
            d[hour] = d[hour] + 1
    except:
        print 'No data element at index sub-2'
        continue
l.append(sorted(d.items()))
#print l
count = 0
for tup in l:
    for lines in tup:
        print tup[count][0], tup[count][1]
        count = count + 1
        
    
    
    
    