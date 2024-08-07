import numpy as np

one_dim = np.array([23, 21, 56, 78])

# Copy : Modify the copy, which will not affect the original array
copy_one_dim = one_dim.copy()
# updated
copy_one_dim[2] = 100
print("Original : ", one_dim)
print("Copied : ", copy_one_dim)

three_dim_original = np.array([
    [[11, 12],
     [21, 22]],

    [[31, 32],
     [41, 42]],

    [[51, 89],
     [90, 67]]
])

three_dim_copy = three_dim_original.copy()

three_dim_copy[1, 0, 1] = 500
print("Original Three Dim : ", three_dim_original)
print("Copy Three Dim : ", three_dim_copy)

# View : Modify the view, which will also affect the original array

view_one_dim = one_dim.view()
# updated
view_one_dim[1] = 500
print("\n\nOriginal : ", one_dim)
print("Viewed : ", view_one_dim)

three_dim_view = three_dim_original.view()

three_dim_view[1, 0, 1] = 500
print("Original Three Dim : ", three_dim_original)
print("Copy Three Dim : ", three_dim_view)
