import numpy as np
import random as r
import time

def search_number(matrix):
    number = 1
    not_found = True
    while(not_found):
        if number not in matrix:
            not_found = False
            return number
        else:
            number += 1

# generate main grid
matrix = np.zeros((9,9))

def generate_num():
    num = r.randint(1,9)
    return num

def place_num(row, col, grid, num):
    if num not in row and num not in col and num not in grid:
        return True
    else:
        return False


num = generate_num()
count = 0

num_used = []

# new loop construct where steps will be use instead of range loops to be able to backtrack
def fill_grid(matrix, start_row, end_row, start_col, num, max_iteration):
    increment = False
    num_used = []
    countrow = start_row
    countcol = start_col
    
    while countrow < end_row:
        
        if max_iteration > 0:
            # print(matrix)
            # print(f"num_used = {num_used}")
            # print(f"num={num}")
            # print(f"countrow: {countrow}")
            # print(f"countcol: {countcol}")
            result = place_num(matrix[countrow], matrix[:, countcol], matrix[start_row:end_row, 0 + start_col:3 + start_col], num)
            # print(f"countrow: {countrow}, countcol: {countcol} ")
            if result:
                matrix[countrow, countcol] = num
                
                countcol += 1
                num_used = []
                num = generate_num()
            
            else:
                if num not in num_used:
                    num_used.append(num)
                else:
                    if len(num_used) > 8:
                        matrix[start_row:end_row, 0 + start_col:3 + start_col] = 0
            
                        # reset previos to start
                        max_iteration -= 1 # to control how many iterations area allowed
                        countrow = start_row
                        countcol = start_col
                        num_used = []
                        num = generate_num()
                    
                        # need to add backtrack here..
                    else:
                        if num == 1:
                            increment = True
                        elif num == 9:
                            increment = False
                        if increment:
                            num += 1
                        else:
                            num -= 1
                        
                        

            if countcol > start_col + 3 - 1:
                countrow += 1
                countcol = start_col
        else:
            
            # print(max_iteration)
            break

    
    
     
max_iteration = 10
number = generate_num()

start_time = time.time()
while 0 in matrix:
    fill_grid(matrix, 0, 3, 0, number, max_iteration)
    fill_grid(matrix, 0, 3, 3, number, max_iteration)
    fill_grid(matrix, 0, 3, 6, number, max_iteration)
    fill_grid(matrix, 3, 6, 0, number, max_iteration)
    fill_grid(matrix, 3, 6, 3, number, max_iteration)
    fill_grid(matrix, 3, 6, 6, number, max_iteration)
    fill_grid(matrix, 6, 9, 0, number, max_iteration)
    fill_grid(matrix, 6, 9, 3, number, max_iteration)
    fill_grid(matrix, 6, 9, 6, number, max_iteration)
    # print(matrix)
end_time = time.time()

completion_time = end_time - start_time
# note: by limiting the iterations makes it easier to judge if a succesful sudoku game is created. does not guarante a correct puzzle but by running the program multiple times,
# it is possible to get a correct iteration. 
# next step: make a algorithm that keeps iterating above steps till a success is had

# start = 0
# step = 3
# stop = 7
# # fills all grids in the 9x9 grid
# for i in range(start, stop, step):
#     for n in range(start, stop, step):
#         fill_grid(matrix, i, i+3, n, number)

print(matrix)
print(f"time to complete {round(completion_time, 2)} seconds")
