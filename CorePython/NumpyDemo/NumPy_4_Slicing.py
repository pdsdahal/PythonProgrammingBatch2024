import numpy as np

one_dim = np.array([45, 23, 12, 56, 33, 78, 90, 89])

# Slice items starting from index 3 to the end
print("From index 3 to last : ", one_dim[3:])

# Slice items between indexes 2 and 6 (inclusive of start, exclusive of end)
print("From index 2 to index 5 : ", one_dim[2:6])

# Slice items from the beginning up to index 4 (exclusive)
print("index 0 to 3 : ", one_dim[:4])

# Slice items between indexes 1 and 7 with a step of 2
print("indexes 1 and 7 with a step of 2 : ", one_dim[1:7:2])

two_dim = np.array([[12, 45, 33, 23],
                    [67, 56, 43, 54],
                    [67, 89, 90, 91]])

print("\n\n", two_dim)

print("\nFirst row : First column to Last column : ", two_dim[0, :])
print("Second column : First row to Last row : ", two_dim[:, 1])

# Slice items between indexes 1 and 3 in the second row
print("Slice items between indexes 1 and 3 in the second row : ", two_dim[1, 1:3])

# Slice the third column (index 2) from the first two rows (indexes 0 and 1)
print("Slice the third column (index 2) from the first two rows (indexes 0 and 1) : ", two_dim[0:2, 2])

# Slice the subarray from rows 0 to 1 and columns 1 to 2
print(two_dim[0:2, 1:3])
