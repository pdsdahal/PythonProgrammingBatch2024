import numpy as np

input_data = np.arange(start=1, stop=13, step=1)
two_dim = input_data.reshape(3, 4)
print("\nTwo Dim : \n",two_dim)

three_dim = input_data.reshape(3, 2, 2)
print("\nThree Dim : \n",three_dim)
