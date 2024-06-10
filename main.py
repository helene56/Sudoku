#TODO: create 9x9 matrix random num from 1-9 times 9.
#TODO: every row, column and grid must only contain one number once

import numpy as np

matrix = np.random.randint(1, 9, size=(9 , 9))
print(matrix)

# for index, element in np.ndenumerate(matrix):
#     print(f'Index: {index}, Element: {element}')
# for _ in range(9):
#         print(_)

# for element in np.nditer(matrix):
#     for n in range(9):
#         print(n)
#         if element == matrix[0, n]:
#             print(f"element: {element}")
#             print(f"n: {n}")

def search_number(matrix):
    number = 1
    
    if number in matrix:


# selects all elements in column 0 from row 1
for element in matrix[1:, 0]:
    if element == matrix[0,0]:
        # print(element)
        not_in = search_number(matrix[1:, 0])
        print(not_in)

# for element in matrix[0, 1:]:
#     if element == matrix[0,0]:
#         print(element)
#         not_in = search_number(matrix[1:, 0])
#         print(not_in)