#Type Casting is a process in which we convert a literal of one data type to another data type.
#Python supports two types of casting − implicit and explicit.

#implicit : When any language compiler/interpreter automatically converts object of one type into other

num1 = 10
print(f"original number : {num1}, Type : {type(num1)}")

num1 = num1 * 100.56
print(f"final number : {num1}, type : {type(num1)}")

#Python's built-in functions int(), float() and str() to perform the explicit conversions such as string to integer.

# double to int
salary = 234.678
salaryInt = int(salary)
print(f"Salary in Double Original : {salary}")
print(f"Salary in Int Final : {salaryInt}")

# int to double
averageSalary = 12
averageSalaryDouble = float(averageSalary)
print(f"Original Int : {averageSalary}")
print(f"Final Float : {averageSalaryDouble}")

# boolean to String
gender = True
print(f"Initial {gender} and type is {type(gender)}")
gender = str(gender)
print(f"Final {gender} and type is {type(gender)}")

#String to boolean
collegeName = "Saint Louis University"
collegeName = bool(collegeName)
print(f"Final Result : {collegeName}")