"""
Created on Nov 11, 2016
Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):    
    
    def partitionIt(array, start, end, idx_pivot):
        #'returns the position where the pivot winds up'
        if not (start <= idx_pivot <= end):
            raise ValueError('idx pivot must be between start and end')
        array[start], array[idx_pivot] = array[idx_pivot], array[start]
        pivot = array[start]
        i = start + 1
        j = start + 1        
        while j <= end:
            if array[j] <= pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
            j += 1
        array[start], array[i - 1] = array[i - 1], array[start]
        return i - 1     
       
    def quicksort(array, start, end):
        if end - start < 1:
            return
        idx_pivot = end
        print "before partitioning", array, "index pivot: ",  idx_pivot,"index end: ", end,"index start: ", start        
        i = partitionIt(array, start, end, idx_pivot)
        print "after partitioning", array,"i: ", i, "index pivot: ",  idx_pivot,"index end: ", end,"index start: ", start
        print
        quicksort(array, start, i - 1)
        quicksort(array, i + 1, end)
        
    quicksort(array, 0, len(array)-1)
        
    return array

     
       
test = [21, 4, 1, 3, 8, 20, 25, 6, 21, 14]
print quicksort(test)

#RESULT OF WORK
#before partitioning [21, 4, 1, 3, 8, 20, 25, 6, 21, 14] index pivot:  9 index end:  9 index start:  0
#after partitioning [6, 4, 1, 3, 8, 14, 25, 20, 21, 21] i:  5 index pivot:  9 index end:  9 index start:  0

#before partitioning [6, 4, 1, 3, 8, 14, 25, 20, 21, 21] index pivot:  4 index end:  4 index start:  0
#after partitioning [6, 4, 1, 3, 8, 14, 25, 20, 21, 21] i:  4 index pivot:  4 index end:  4 index start:  0

#before partitioning [6, 4, 1, 3, 8, 14, 25, 20, 21, 21] index pivot:  3 index end:  3 index start:  0
#after partitioning [1, 3, 4, 6, 8, 14, 25, 20, 21, 21] i:  1 index pivot:  3 index end:  3 index start:  0

#before partitioning [1, 3, 4, 6, 8, 14, 25, 20, 21, 21] index pivot:  3 index end:  3 index start:  2
#after partitioning [1, 3, 4, 6, 8, 14, 25, 20, 21, 21] i:  3 index pivot:  3 index end:  3 index start:  2

#before partitioning [1, 3, 4, 6, 8, 14, 25, 20, 21, 21] index pivot:  9 index end:  9 index start:  6
#after partitioning [1, 3, 4, 6, 8, 14, 21, 20, 21, 25] i:  8 index pivot:  9 index end:  9 index start:  6

#before partitioning [1, 3, 4, 6, 8, 14, 21, 20, 21, 25] index pivot:  7 index end:  7 index start:  6
#after partitioning [1, 3, 4, 6, 8, 14, 20, 21, 21, 25] i:  6 index pivot:  7 index end:  7 index start:  6

#[1, 3, 4, 6, 8, 14, 20, 21, 21, 25]