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

def generate_num(num):
    if num == 9:
        num = 1
    else:
        num += 1
    return num

def place_num(row, col, grid, num):
    # for element in matrix:
    #     if element != num:
    #         return True
    if num not in row and num not in col and num not in grid:
        return True
    else:
        return False


num = generate_num(1)
count = 0
row_count = 0
n = 0

max_count = 0

for j in range(3):
    # print(f"j={j}")
    for n in range(3):
        # print(f"n={n}")
        for row in range(3):
            # print(f"row={row}")
            count = 0
            while count < 3:
                
                result = place_num(matrix[row + (j*3)], matrix[:, count + (n*3)], matrix[0+(j*3):3+(j*3), (n*3):3+(n*3)], num)
                # print(result)
                if result:
                    matrix[row + (j*3), count + (n*3)] = num
                    count += 1
                    
                else: 
                    num = generate_num(num)
                    
                    # print(f"{matrix}\n")
                    # print(f"row: {matrix[row + (j*3)]}\n col: {matrix[:, count + (n*3)]}\n grid:\n {matrix[0+(j*3):3+(j*3), (n*3):3+(n*3)]}\n")
                    # print(f"generated num: {num}")
            
    
        

    

    
    

print(matrix)
