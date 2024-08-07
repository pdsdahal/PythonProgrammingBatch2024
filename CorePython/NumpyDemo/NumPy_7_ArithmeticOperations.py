import numpy as np

# First Dimension
one_dim_first = np.array([2, 3, 2, 10], dtype=float)
one_dim_second = np.array([12, 10, 13, 9], dtype=float)

one_dim_sum = np.add(one_dim_first, one_dim_second)
one_dim_mul = np.multiply(one_dim_first, one_dim_second)
one_dim_div = np.divide(one_dim_first, one_dim_second)
one_dim_subtract = np.subtract(one_dim_first, one_dim_second)

# ------------------------power() function in NumPy is used to raise elements of an array to the
# power of the corresponding elements of another array or a scalar.
one_dim_power = np.power(one_dim_first,
                         3)  # first parameter is base array, second parameter is exponent array or scalar.

# ------------------------ The reciprocal of a number
# x is
# 1 / 𝑥
one_dim_reciprocal = np.reciprocal(one_dim_first)

print(f"{one_dim_first} + {one_dim_second} = {one_dim_sum}")
print(f"{one_dim_first} * {one_dim_second} = {one_dim_mul}")
print(f"{one_dim_first} / {one_dim_second} = {one_dim_div}")
print(f"{one_dim_first} - {one_dim_second} = {one_dim_subtract}")
print(f"{one_dim_first} ^ 3 (power) = {one_dim_power}")
print(f"1 / {one_dim_first}  = {one_dim_reciprocal}")

# Second Dimension
two_dim_first = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])

two_dim_second = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

two_dim_sum = np.add(two_dim_first, two_dim_second)
two_dim_mul = np.multiply(two_dim_first, two_dim_second)

print(f"\n\n{two_dim_first} \n+ \n{two_dim_second} \n = \n {two_dim_sum}")
print(f"\n\n{two_dim_first} \n* \n{two_dim_second} \n = \n {two_dim_mul}")
