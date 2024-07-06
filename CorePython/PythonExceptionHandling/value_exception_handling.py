name = input("Enter your name ")
age = ""
try:
    age = int(input("Enter your age (enter string) "))
except ValueError as e:
    print("Error : ", e)

print("Name : ", name)
print("Age : ", age)