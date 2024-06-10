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
    not_found = True
    while(not_found):
        if number not in matrix:
            not_found = False
            return number
        else:
            number += 1




# selects all elements in column 0 from row 1
for element_col in matrix[1:, 0]:
    if element_col == matrix[0,0]:
        print(f"element: {element_col}")
        not_in = search_number(matrix[1:, 0])
        print(f"num not in column: {not_in}")


for element in matrix[0, 1:]:
    if element == matrix[0,0]:
        print(f"element: {element}")
        not_in = search_number(matrix[0, 1:])
        print(f"num not in row: {not_in}")