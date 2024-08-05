import numpy as np

# ndarray.shape : This array attribute returns a tuple consisting of array dimensions.

# one dimensional array
one_dim = np.array([2, 6, 8, 9, 13, 17])
print(one_dim.shape, " One Dimensional \n", one_dim, "\n")

# two dimensional array
two_dim = np.array([[78, 23, 14, 56], [11, 56, 23, 32]])
print(two_dim.shape, " Two Dimensional\n", two_dim, "\n")

# reshape function to resize an array.
two_dim_reshape = two_dim.reshape(4, 2)
print(two_dim_reshape.shape, " Two Dimensional \n", two_dim_reshape, "\n")

print("total number of items : ", two_dim_reshape.size)

# np.arange is used to create arrays with evenly spaced values within a specified range.
# start: The starting value of the sequence (inclusive). If omitted, defaults to 0.
# stop: The end value of the sequence (exclusive).
# step: The spacing between values. Defaults to 1.
array_1 = np.arange(start=1, stop=13, step=1, dtype=int)
print(array_1)

# three_dim : Creating three dimension
# First Dimension (3): 3 blocks,
# Second Dimension (2): Each block has 2 rows
# Third Dimension (2): Each row has 2 elements.
three_dim = array_1.reshape(3, 2, 2)
print(three_dim)
