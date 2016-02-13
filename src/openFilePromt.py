
fname = input("Enter the file name: ")

try:
    fo = open(fname)
except:
    print ("File cannot be opened", fname)
    exit()

count = 0
for line in fo:
    print (line.strip())
    #in uppercase
    #print (line.strip().upper())
    count = count + 1

print (count, "lines")
