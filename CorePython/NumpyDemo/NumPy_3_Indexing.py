import numpy as np

# one dimension
one_dim = np.array([10, 32, 90, 9, 23])
print("Value at index 0 : ", one_dim[0])
print("Value at index 1 : ", one_dim[1])

# iteration
for index, data in enumerate(one_dim):
    print(index, " : ", data)

# Two dimension
two_dim = np.array([[10, 23, 12, 56],
                    [55, 43, 32, 12],
                    [67, 45, 89, 42]])

print("At 0 index row : ", two_dim[0])
print("At 1 index row : ", two_dim[1])
print("At 2 index row : ", two_dim[2])

print("At 0 index column : ", two_dim[:, 0])
print("At 1 index column : ", two_dim[:, 1])
print("At 2 index column : ", two_dim[:, 2])

print("Value at 0, 0 : ", two_dim[0, 3])

# Three dimension
three_dim = np.array([
    [[1, 3],
     [4, 6]],

    [[7, 5],
     [3, 1]],

    [[9, 4],
     [23, 12]]
])

print("Block 0 : ", three_dim[0])
print("Block 1 : ", three_dim[1])
print("Block 2 : ", three_dim[2])
print("Block 0 : first row : ", three_dim[0, 0, :])
print("Block 2 : second row : ", three_dim[2, 1, :])
print("Block 1 : second column : ", three_dim[1, :, 1])
print("Value at block 1, row 1 and column 0 : ", three_dim[1, 1, 0])
