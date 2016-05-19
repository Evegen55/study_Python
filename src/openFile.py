
#if you run this program via python shell
#file named "romeo.txt" must be placed in a folder that you use to run python shell
#
#if you run this program via PyDev
#Choose "Python Run" and your run configuration from the left and then in the "Arguments"
#tab in the right side, set your "working directory" as "other" with giving
#"the path" on which you want to run your code.

#for python ver 3.4.4
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
