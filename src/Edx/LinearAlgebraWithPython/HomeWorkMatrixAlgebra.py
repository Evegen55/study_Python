'''
@author: Evegen
'''
import numpy as np
def transpose():
    mat = np.array([[1, -2], [2, -1]])
    print mat.transpose()

def matrix_addition():
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 4], [3, 2]])
    print mat1 + mat2

def matrix_addition1():
    mat1 = np.array([[-1, 0], [0, 1]])
    mat2 = np.array([[-2, 1], [-1, 2]])
    print mat1 - mat2

def scalar_matrix_multiplication():
    mat1 = np.array([[1, -2], [2, -1]])
    print 2.5 * mat1

def matrix_vector_multiplication():
    mat1 = np.array([[1, 0], [0, 1]])
    col_vec1 = np.array([[1], [2]])
    print mat1.dot(col_vec1)

def matrix_vector_multiplication1():
    mat1 = np.array([[1, -1], [-1, 1]])
    col_vec1 = np.array([[5], [6]])
    print mat1.dot(col_vec1)

def matrix_multiplication():
    mat1 = np.array([[1, 0], [0, -1]])
    mat2 = np.array([[1, -2], [2, -1]])
    print mat1.dot(mat2)

def matrix_multiplication1():
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[4, 3], [2, 1]])
    print mat1.dot(mat2)

transpose()
matrix_addition()
matrix_addition1()
scalar_matrix_multiplication()
matrix_vector_multiplication()    
matrix_vector_multiplication1()
matrix_multiplication()
matrix_multiplication1()