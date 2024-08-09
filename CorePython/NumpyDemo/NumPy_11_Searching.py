import numpy as np

one_dim = np.array([21, 34, 12, 56, 78, 100, 11])

# Searching in One-Dimensional Array
# indexing with condition
indices = np.where(one_dim == 34)
print("Indices with condition : ", indices)
print("Indices with datas : ", one_dim[indices], "\n\n")

index_greater_21 = np.where(one_dim > 21)
print("Indices with greater than condition : ", index_greater_21)
print("Indices with datas : ", one_dim[index_greater_21], "\n\n")


# check if the value exist
result = 30 in one_dim
print("Check if the value exist : ", result, "\n\n")

# np.argmax and np.argmin
# Returns the index of the maximum or minimum value in an array.
max_value_index = np.argmax(one_dim)
min_value_index = np.argmin(one_dim)
print("Maximum value of index is : ", max_value_index)
print("Minimum value of index is : ", min_value_index, "\n\n")

# Searching in Two-Dimensional Arrays
two_dim = np.array([[15, 14, 64, 23], [21, 17, 50, 20], [56, 34, 23, 15]])
print(two_dim, "\n\n")
index_no = np.argwhere(two_dim == 15)
print("Value 15 at index : ", index_no,"\n")

# Retrieve the values at the found indices
for index in index_no:
    print(f"Value at {index} is {two_dim[index[0], index[1]]}\n")

# indexing with condition
indices_two_dims = np.where(two_dim > 20)
print(indices_two_dims)

# let find the data from above index
for row, column in zip(indices_two_dims[0], indices_two_dims[1]):
    print(f"value at {row},{column} is {two_dim[row][column]}")
