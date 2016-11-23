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
    print "length_vector"
    col_vec1 = np.array([[4], [8], [-4]])
    rise_power = np.power(col_vec1, 2)
    #print rise_power
    to_sum = np.sum(np.power(col_vec1, 2))
    #print to_sum
    exactly = np.sqrt(to_sum)
    #print exactly
    rounded = np.round(exactly, 2)
    print rounded
    
    print "normalized_vector"
    normalized_vector =  col_vec1 / rounded    
    print normalized_vector
    rouded_norm_vector = np.round(normalized_vector, 2)
    print rouded_norm_vector   

def cross_product():
    print 'cross product'
    col_vec1 = np.array([[2], [-4], [1]])
    col_vec2 = np.array([[2], [1], [-2]])    
    print np.cross(col_vec1, col_vec2, 0, 0)
    #the same result
    #cross = np.array([col_vec1[1]*col_vec2[2] - col_vec1[2]*col_vec2[1], 
    #                  col_vec1[2]*col_vec2[0] - col_vec1[0]*col_vec2[2],
    #                  col_vec1[0]*col_vec2[1] - col_vec1[1]*col_vec2[0]])
    #print cross
def scalar_product():
    print 'scalar product'
    col_vec1 = np.array([[2], [-4], [1]])
    col_vec2 = np.array([[2], [1], [-2]])
    print np.dot(col_vec2.transpose(), col_vec1)

vector_addition1()
vector_addition2()
length_and_normalized_vector()
cross_product()
scalar_product()