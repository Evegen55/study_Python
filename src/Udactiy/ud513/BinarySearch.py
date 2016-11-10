"""
Created on Nov 10, 2016
You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    def rec_find(array, value, upperBound, lowerBound):
        curIn = (lowerBound + upperBound)/2;    
        if(array[curIn]==value):
            return curIn
        elif(lowerBound == upperBound):
            return -1
        elif(array[curIn] > value):
            return rec_find(array, value, curIn+1, upperBound)            
        else:
            return rec_find(array, value, lowerBound, curIn-1)                               
        return -1
    return rec_find(input_array, value, 0, len(input_array)-1)




test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)