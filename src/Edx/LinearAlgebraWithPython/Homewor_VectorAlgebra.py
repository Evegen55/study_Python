'''
Created on Nov 21, 2016

@author: Evgenii_Lartcev
@see: https://courses.edx.org/courses/course-v1:TUMx+AUTONAVx+2T2015/courseware/b25665183d4a495f879526eff50b9068/620b86a76124415698af9e8b0c6793c6/
'''
import numpy as np

def vector_addition1():
    print "vector_addition1"
    # create a column vectors
    col_vec1 = np.array([[1.5], [-1]])
    col_vec2 = np.array([[2], [3.5]])
    col_vec3 = col_vec1 + col_vec2
    print col_vec3
    
def vector_addition2():
    print "vector_addition2"
    # create a column vectors
    col_vec1 = np.array([[2], [-4], [1]])
    col_vec2 = np.array([[2], [1], [-2]])
    col_vec3 = col_vec1 - col_vec2
    print col_vec3

def length_and_normalized_vector():
    col_vec1 = np.array([[4], [8], [-4]])
    pass

vector_addition1()
vector_addition2()