"""
5.2 Write a program that repeatedly prompts a user for integer numbers until
the user enters 'done'. Once 'done' is entered, print out the largest and
smallest of the numbers. If the user enters anything other than a valid number
catch it with a try/except and put out an appropriate message and ignore the number.
Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
"""
#for python ver 2.7
largest = None
smallest = None
lst = list()
while True:
    num = raw_input("Enter a number: ")
    try:
        apd = int(num)
        lst.append(apd)
        if num == "done" : break
        largest = max(lst)
        smallest = min(lst)
    except:
        print 'Invalid input'
        if num == "done" : break
print "Maximum is", largest
print "Minimum is", smallest
