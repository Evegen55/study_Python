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
       
    def quicksort(array, start=0, end=None):
        if end is None:
            end = len(array) - 1
        if end - start < 1:
            return
        idx_pivot = end
        i = partitionIt(array, start, end, idx_pivot)
        #print array, i, idx_pivot
        quicksort(array, start, i - 1)
        quicksort(array, i + 1, end)
        
    quicksort(array, 0, len(array)-1)
        
    return array

     
       
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)