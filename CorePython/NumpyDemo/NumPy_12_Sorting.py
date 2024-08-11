import numpy as np

one_dim = np.array([21, 45, 12, 9, 56, 5, 3, 40])
sorted_one_dim = np.sort(one_dim)
print("Before Sorting : ", one_dim)
print("After Sorting : ", sorted_one_dim)

two_dim = np.array([[21, 45, 67, 12, 3],
                    [45, 32, 14, 23, 56],
                    [90, 13, 25, 31, 67]])
sorted_array_column = np.sort(two_dim, axis=0)
print(sorted_array_column, "\n")

sorted_array_row = np.sort(two_dim, axis=1)
print(sorted_array_row, "\n")


personal_data = np.array([
    ('Shyam', 'Shrestha', 56, 1000),
    ('Ram', 'Dahal', 13, 1200),
    ('Hari', 'Pandey', 70, 1110.56)],
    dtype=[("FirstName", "U50"), ("LastName", "U50"), ("Age", "i4"), ("Salary", "float32")])

personal_sorted_data = np.sort(personal_data, order=["Age", "FirstName"])
print("Personal sorted data : \n",personal_sorted_data)