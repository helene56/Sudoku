import numpy as np

# Create a sample NumPy matrix
matrix = np.array([[10, 20, 30],
                   [10, 50, 60],
                   [70, 80, 90]])

# Specify the number to find and the row index
num = 50
row_index = 1

# Select the specific row
row = matrix[row_index, :]

# Use numpy.where to find the column index of the number
column_index = np.where(row == num)[0]
column_index = column_index[0]
# print(column_index)

matrix_not_complete = np.isin(0, matrix)

if matrix_not_complete:
    print("hello")
else:
    print("hej")