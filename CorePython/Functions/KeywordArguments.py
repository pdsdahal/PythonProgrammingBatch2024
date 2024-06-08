# When using keyword arguments,
# it is not necessary to follow the order of formal arguments in function definition.
# Using keyword arguments is optional.
def student_details_info(name, age, gender):
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Gender : {gender}")


student_details_info(age=14, name="Ram Pandey", gender="Male")

student_details_info("Sita Dahal", gender="Female", age=13)