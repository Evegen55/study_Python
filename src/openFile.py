
#file named "romeo.txt" must be placed in a folder that you use to run python shell
fo = open("romeo.txt", "r")

count = 0
for line in fo:
    print (line.strip())
    count = count + 1

print (count, "lines")

#we must reopen file again
fh = open("romeo.txt", "r")
inp = fh.read()
print (len(inp), "symbols")
