import numpy as np

one_dim_first = np.array([10, 20, 30, 40, 50])
one_dim_second = np.array([60, 70, 80, 90, 100])

one_dim_result = np.concatenate((one_dim_first, one_dim_second))
print("Joined : ", one_dim_result)

# Two dimensional joining
two_dim_first = np.array([[2, 5, 6, 8],
                          [10, 45, 23, 11],
                          [34, 56, 78, 33]])

two_dim_second = np.array([[12, 15, 16, 18],
                           [20, 25, 23, 21],
                           [34, 36, 38, 33]])

# row wise joined
joined_two_dim_row = np.concatenate((two_dim_first, two_dim_second), axis=1)
print(joined_two_dim_row, "\n\n")

# column wise joined
joined_two_dim_col = np.concatenate((two_dim_first, two_dim_second), axis=0)
print(joined_two_dim_col)

# SPLITTING
one_dim_data = np.array([2, 5, 6, 12, 34, 56, 23])
# split the array into three parts (unequal splits)
# it will return l % n sub-arrays of size l // n + 1 and the rest of size l // n.
# l = 7, n = 3
# l//n + 1 = 7//3 + 1 = 2+1 = 3
# l//n = 7//3 = 2
result = np.array_split(one_dim_data, 3)
print(result)
