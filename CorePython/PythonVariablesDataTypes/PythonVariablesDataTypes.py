#Variables are containers for storing data values
from turtledemo.chaos import f

year = 2020

print(year)
#Getting data type
print(type(year))

#print variables with some text

#Way 1 : type casting : int to str
print("year is "+str(year) + ".")
#Way 2 : , to separate variables and text
print("year is",year,".")
# Way 3 : f-string
print(f"year is {year}.")

#many Values to Multiple Variables
name, num1, num2 = "Ram", 20, 30
print(f"Name = {name} \nNum1 = {num1} \nNum2 = {num2}")

#one Value to Multiple Variables
cityName = capitalCity = "Kathmandu"
print(f"City : {cityName} \nCapital City : {capitalCity}")

#Data Types
#Integer
players = 10
tickets = 10
print(f"Total Players {players} and total ticket is {tickets}")
#Float
perDaysalary = 145.6
hourly = 14.56
print(f"Your per day salary is {perDaysalary} and Hourly salary is : {hourly}")

#String
collegeName = "Abc international College"
address = "St.Louis USA"
print(f"{collegeName} is located in {address}")

#Boolean
active = True
offline = False
print(f"Is Ram active? {active}")
print(f"Ram is offline. {offline}")