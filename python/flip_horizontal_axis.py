''' Firecode.io Problem
You are given an m x n 2D image matrix (List of Lists) where each integer
represents a pixel. Flip it in-place along its horizontal axis.

Example:
Input image :
              1 1
              0 0
Modified to :
              0 0
              1 1
'''
import copy
def flip_horizontal_axis(matrix):
    # base case 1 pixel -> pixel
    if len(matrix) == 1:
        return matrix
    matrix_copy = copy.deepcopy(matrix)
    for i in range(0, len(matrix)-1):
        current_item = matrix_copy.pop(i)
        matrix_copy.append(current_item)
    return matrix_copy
    # return " {} \n {}".format(matrix_copy[0], matrix_copy[1])
    # print(f"{matrix_copy[0]} /n {matrix_copy[1]}")

if __name__ == '__main__':
    matrix = [[1,0,0],[0,0,1]]
    matrix2 = [[1,0,0], [0,0, 1]]
    matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
    print(flip_horizontal_axis(matrix))
