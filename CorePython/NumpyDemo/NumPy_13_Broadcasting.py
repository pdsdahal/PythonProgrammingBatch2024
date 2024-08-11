import numpy as np

# broadcasting refers to the ability to perform element-wise operations on arrays of different shapes.
one_dim_first = np.array([1, 5, 9, 2, 5])
one_dim_second = np.array([3])

one_dim_broadcast = one_dim_first + one_dim_second
print(f"{one_dim_first} + {one_dim_second} = {one_dim_broadcast}")

one_dim_1 = np.array([1, 5, 9, 2, 5])  # 1X5
# 2 X 1
two_dim_2 = np.array([[3],
                      [1]])
broadcast_result = one_dim_1 + two_dim_2
print(broadcast_result)
