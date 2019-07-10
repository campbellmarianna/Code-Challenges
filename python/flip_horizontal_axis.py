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
def flip_horizontal_axis(matrix):
    # base case 1 pixel -> 1 pixel
    if len(matrix) == 1:
        return matrix
    # if the length of the matrix is 2
    elif len(matrix) == 2:
        flip_count = 1
        while flip_count == 1:
            temp_var = matrix.pop(0)
            matrix.append(temp_var)
            flip_count -= 1
    # if the length of the matric is 3
    else:
        # store value of the first one
        temp_var = matrix[0]
        # pop and store the last one
        last_item = matrix.pop()
        # append the first one to the end
        matrix.append(temp_var)
        # put the former last item in the front
        matrix[0] = last_item
# -- Another way of doing it
# def flip_horizontal_axis(matrix):
#     r = len(matrix) - 1 # 2 row
#     c = len(matrix[0]) - 1 # 2 column
#     temp = 0
#     i = 0 # index
#     while i <= r/2: # = 1
#         j = 0 # other index
#         while j <= c:
#             temp = matrix[i][j] # matrix[0][0] = 1
#             matrix[i][j] = matrix[r-i][j] # matrix[2-0][0] = 7
#             matrix[r-i][j] = temp # switching them
#             j = j+1
#         i = i + 1
# ---
# def flip_horizontal_axis(matrix):
#     # base case 1 pixel -> 1 pixel
#     if len(matrix) == 1:
#         return matrix
#     i = 0
#     goal = len(matrix)
#     while i is not goal:
#         current_item = matrix.pop(goal - 1)
#         matrix.append(current_item)
#         i += 1
# ---
# def flip_horizontal_axis(matrix):
    # for outer_list in matrix:
    #     for i in range(0, len(matrix) - 1):
    #         # swap
    #         temp_var = matrix.pop(i)
    #         matrix.append(temp_var)

if __name__ == '__main__':
    matrix = [[1,0,0],[0,0,1]]
    matrix2 = [[1,0,0], [0,0, 1]]
    matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
    print(flip_horizontal_axis(matrix3))
