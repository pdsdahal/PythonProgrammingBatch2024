employeeDetails = ("Ram Pandey", 12, "ram@gmail.com")
print(employeeDetails)

# Tuples are immutable which means you cannot update or change the values of tuple elements.
# employeeDetails[0] = "Shaym Pandey"
# print(employeeDetails)

employeeAddress = ("USA","St. Louis", "Nottingham Ave.")

# allows to create a new tuples from existing two tuples
fullDetails = employeeDetails + employeeAddress
print(fullDetails)
