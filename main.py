#TODO: create 9x9 matrix random num from 1-9 times 9.
#TODO: every row, column and grid must only contain one number once
# might be better to backtrack after it tries to fill it out once first
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
    else:
        return False


def backtrack():
    pass

def check_number(num_list, num):
    # temp code
    global count
    if len(num_list) > 8:
        # this means that every number has been added to the list, and therefore exhausted all possibilities, and thus should backtrack..
        num_list = []
        # temp code
        count += 1
        # backtrack

    if num not in num_list:
        # number has not been used before, it may continue with the rest of the code
        # num_list.append(num)
        return True
    else:
        # this number is already in the list, it should generate a new number now
        return False
    
    
    
    

num = generate_num()
count = 0

num_used = []
# for j in range(3):
#     # print(f"j={j}")
#     for n in range(3):
#         # print(f"n={n}")
#         for row in range(3):
#             # print(f"row={row}")
#             count = 0
#             while count < 3:
                
#                 result = place_num(matrix[row + (j*3)], matrix[:, count + (n*3)], matrix[0+(j*3):3+(j*3), (n*3):3+(n*3)], num)
#                 # print(result)
#                 if result:
#                     matrix[row + (j*3), count + (n*3)] = num
#                     count += 1
#                     num_used = []
                    
#                 else:
#                     if check_number(num_used, num):
#                         num_used.append(num)
#                     else:
#                         num = generate_num()



# new loop construct where steps will be use instead of range loops to be able to backtrack
def fill_grid(matrix, start, end, num):
    num_used = []
    countrow = start
    countcol = 0
    while countrow < end:
        result = place_num(matrix[countrow], matrix[:, countcol], matrix[start:end, 0:3], num)
        # print(f"countrow: {countrow}, countcol: {countcol} ")
        if result:
            # print(f"\n {matrix}")
            # print(f"col check: {matrix[:, countrow]}")
            
            matrix[countrow, countcol] = num
            
            countcol += 1
            num_used = []
        if countcol > 2:
            countrow += 1
            countcol = 0
        else:
            if check_number(num_used, num):
                num_used.append(num)
            else:
                num = generate_num()
        

# countrow = 0
# countcol = 0
# while countrow < 3:
#     result = place_num(matrix[countrow], matrix[:, countrow], matrix[0:3, 0:3], num)
#     if result:
#         matrix[countrow, countcol] = num
#         countcol += 1
#         num_used = []
#     if countcol > 2:
#         countrow += 1
#         countcol = 0
          
#     else:
#         if check_number(num_used, num):
#             num_used.append(num)
#         else:
#             num = generate_num()

number = generate_num()      
# fill_grid(matrix, 0, 3, number)
# fill_grid(matrix, 3, 6, number)
# fill_grid(matrix, 6, 9, number)

start = 0
step = 3
stop = 7
for n in range(start, stop, step):
    # print(n)
    fill_grid(matrix, n, n+3, number)

print(matrix)
