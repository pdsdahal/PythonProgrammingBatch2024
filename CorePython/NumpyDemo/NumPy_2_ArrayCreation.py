import numpy as np

# Zero Dimension
zero_dim = np.array(234)
# One Dimension
one_dim = np.array([5, 3, 23, 67, 12])
# Two Dimension
two_dim = np.array([[23, 45, 12, 34], [78, 56, 34, 11], [90, 56, 87, 23]])
# Three Dimension
three_dim = np.array([
    [[1, 2], [3, 4]],
    [[45, 23], [67, 89]],
    [[34, 11], [56, 76]]
])

empty_arr = np.empty([3, 4], dtype=int)
print("Empty Array : \n", empty_arr, "\n")
print("Zero Dim : \n", zero_dim, "\n")
print("One Dim: \n", one_dim, "\n")
print("Two Dim: \n", two_dim, "\n")
print("Three Dim: \n", three_dim, "\n")
