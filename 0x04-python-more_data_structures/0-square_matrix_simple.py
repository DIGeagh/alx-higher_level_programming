#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = [[0 for _ in row] for row in matrix]
    
    # Compute the square value for each element in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2
    
    return result

