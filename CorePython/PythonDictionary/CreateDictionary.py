# A dictionary in Python is a collection of key-value pairs.
# Each key is unique and maps to a value.
# Dictionaries are mutable, meaning they can be changed after their creation.
# They are defined using curly braces {} or the dict() function.

# Way 1 using curly braces
studentProfiles = {"name": "Ram Pandey",
                   "id": 2,
                   "age": 15,
                   "address": "Brentwood St.Louis",
                   "email": "ram@gmail.com"}

# Way 2 using dict function

employeeDict = dict(EmployeeId=1,
                    EmployeeName="Sita Dahal",
                    EmployeeAddress="Kathmandu Nepal")


# Dynamic adding element in dict
university_dict = {}
flag = 0
while flag < 5:
    universityName = input("Enter a university info ony by one (Name, Address, Estd. Date, CountryName : ")
    keyName = input("Enter a key : ")
    university_dict[keyName] = universityName
    flag = flag + 1
print(university_dict)
