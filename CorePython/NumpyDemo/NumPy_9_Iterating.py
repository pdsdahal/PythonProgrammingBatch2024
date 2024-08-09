import numpy as np
# One Dim
one_dim = np.array([13, 45, 22, 76, 48, 90])

# iterate over the one dimensional array
for index, data in enumerate(one_dim):
    print(index, " ,  ", data)

# Two Dim
two_dim = np.array([[12, 45, 23, 67],
                    [78, 45, 67, 34],
                    [22, 88, 45, 21]])
# Iterate over the two dimensional array
print("\n\nIterate over the two dimensional array")
for i, row in enumerate(two_dim):
    for j, column in enumerate(row):
        print(i, " , ", j, " = ", two_dim[i, j])


# The numpy.nditer is an iterator object in NumPy that provides an
# efficient multi-dimensional iterator over an array.
print("\n\nUsing nditer")
for result in np.nditer(two_dim):
    print(result)

# Provides both the element's value and its index (position) in the array.
print("\n\nUsing ndenumerate")
for position,value in np.ndenumerate(two_dim):
    print(position, " : ",value)
