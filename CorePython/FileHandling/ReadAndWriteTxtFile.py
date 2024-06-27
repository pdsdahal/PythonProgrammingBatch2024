import os

current_file_absolute_path = os.getcwd()
base_path = os.path.dirname(current_file_absolute_path)

file_path = os.path.join(base_path, 'Resources', 'Employee.txt')
print("File Path:", file_path)

# Reading and writing to a file

# Using with : file is automatically closed when the block of code within the with statement is exited,
# even if an exception is raised.

# When you open a file in append mode, the file pointer is placed at the end of the file.
with open(file=file_path, mode="a+") as employee_file:
    employee_file.write("\nHello This is Jun 26.")

    # Move the file pointer to the beginning to read the content
    employee_file.seek(0)

    # Read the entire content of the file
    content = employee_file.read()
    print(content)

print("Outside the with block : ", employee_file.closed)


# Read the file line by line
print("\n\n Reading file line by line")
with open(file=file_path, mode="a+") as emp_file:
    emp_file.seek(0)
    line = emp_file.readline()
    while line:
        print(line, end="")
        line = emp_file.readline()

# Reading All Lines into a List

print("\n\n  Reading All Lines into a List ")
with open(file=file_path, mode="a+") as emp_files:
    emp_files.seek(0)
    lines = emp_files.readlines()
    for line_ in lines:
        print(line_, end="")