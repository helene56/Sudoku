#TODO: create 9x9 matrix random num from 1-9 times 9.
#TODO: every row, column and grid must only contain one number once

import numpy as np
import random as r

# matrix = np.random.randint(1, 9, size=(9 , 9))
# print(matrix)
# print("\n")
def search_number(matrix):
    number = 1
    not_found = True
    while(not_found):
        if number not in matrix:
            not_found = False
            return number
        else:
            number += 1

# # selects all elements in column 0 from row 1
# for j in range(0,9):
#     for n in range(1,10):
#         for element_col in matrix[n:, j]:
#             if element_col == matrix[n-1,j]:
#                 # print(f"element: {element_col}")
#                 num_not_in = search_number(matrix[:, j])
#                 # print(f"num not in column: {num_not_in}")
#                 # change the element to the number that is not yet in the column
#                 matrix[n-1,j] = num_not_in

# print(matrix)

# print("\n")


# for element_row in matrix[0, 1:]:
#     if element_row == matrix[0,0]:
#         print(f"element: {element_row}")
#         not_in = search_number(matrix[0, 1:])
#         print(f"num not in row: {not_in}")

# for n in range(0,9):
#     for j in range(1,10):
#         for element_row in matrix[j:, n]:
#             if element_row == matrix[j-1,n]:
#                 # print(f"element: {element_col}")
#                 num_not_in = search_number(matrix[:, n])
#                 # print(f"num not in column: {num_not_in}")
#                 # change the element to the number that is not yet in the column
#                 matrix[j-1,n] = num_not_in

# print(matrix)

# new approach: should fill the matrix with random num one by one, but if already present in the row, new one is generated
# 3 check: row check, column check and subgrid check before placing a number


matrix = np.zeros((9,9))

def generate_num():
    num = r.randint(1,9)
    return num

def place_num(row, col, grid, num):
    # for element in matrix:
    #     if element != num:
    #         return True
    if num not in row and num not in col and num not in grid:
        return True


# place first number
matrix[0,0] = 1
# test nums
# matrix[1,1] = 2
# matrix[2,0] = 2

# lists containing rows
# rows = [matrix[n+0] for n in range(9)]
# cols = [matrix[:, n+0] for n in range(9)]
# print(rows[0])
# print(cols)
# first row test
# row = matrix[0]
# # first col test
# col = matrix[:, 0]
# #  first grid test
# grid = matrix[:3, :3]
# num = generate_num()

# if place_num(row, col, grid, num):
#     matrix[0,1] = num

# print(matrix)

num = generate_num()
count = 0
col_count = 0
while count < 8:
    
    if place_num(matrix[count], matrix[:, count], matrix[:3, :3], num):
        matrix[col_count,count + 1] = num
        count += 1
    if place_num(matrix[count], matrix[:, count], matrix[:3, :3], num):
        matrix[col_count+1,count + 1] = num
        count += 1
    
    # if count == 8:
    #     if col_count < 8:
    #         col_count += 1
    #         count = 0
        

    num = generate_num()
    

print(matrix)
