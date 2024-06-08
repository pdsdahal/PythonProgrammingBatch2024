# Arbitrary Arguments - Varying amounts of arguments, we don't know how many arguments
# the user is going to pass in when they invoke function
# To accept varying amount of arguments developer tends to use of
# 1. *args : Arguments (allow to pass non key arguments)
# 2. **kwargs : Keyword Arguments (allow to pass multiple keyword arguments)

def college_names(*args):
    print(f"Size : {len(args)}")
    print(f"Type of data : {type(args)}")
    print(f"All data : {args}")

    # use loop to print data one by one
    for collegeName in args:
        print(str.upper(collegeName))


college_names("SLU", "UMSL", "HUSL", "Mountains")

# Example 2 : find the sum

print("\n\n\nExample 2")


def find_sum(*args):
    sum = 0
    for num in args:
        sum = sum + num
    print(f"Total Sum : {sum}")


find_sum(1, 5, 7, 2, 3, 5, 9)

print("\n\n\nKwargs Demo")


# Arbitrary Keyword Arguments (**kwargs)
# the function can accept arbitrary number of keyword arguments.
# The variable becomes a dictionary of keyword:value pairs.

def display_employee_details(**kwargs):
    # dictionary
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(f"{key.capitalize()} = {value}")


display_employee_details(name="Ram Pandey",
                         gender="Male",
                         dob="2021-01-01",
                         address="Kathmandu Nepal",
                         email="ram@gmail.com",
                         employeeCit=12345)
