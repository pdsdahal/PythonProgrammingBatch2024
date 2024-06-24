# importing
import array as arr

# creating array
# type codes
# 'i' for signed integers
# 'f' for floating point numbers
# 'd' for double-precision floating point numbers

# array of integer
int_elements = arr.array('i',[1,2,3,5,6])
print(int_elements)

# array of double
float_elements = arr.array('d',[1.6,3.3,4.55,4.9,4.5,6.0,4])
print(float_elements)

# The array module in Python does not support arrays of strings directly.
# The array module is designed for creating arrays of numeric values or
# other fixed-size primitive data types.
# The type codes provided by the array module are meant for integers,
# floats, and other basic types, but not for strings.


# Handle arrays of strings, you can use a list of strings,

student_names = ["Ram Pandey","Sita Shrestha","Hari Moktan", "Lee Chi"]
print(student_names)