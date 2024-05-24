import math

#absolute
negaNum = int(input("Enter a negative number "))
print(f"Absoulute value of {negaNum}  = ", abs(negaNum))

#round
decNum = float(input("Enter a decimal number "))
roundNum = int(input("Enter a number of decimal places to round "))
print(f"round({decNum}, {roundNum})  = ", round(decNum, roundNum))

#power
base = 3
exp = 2
print(f"{base} to power of {exp}", pow(base, exp))

#min and max
print(f"Max from 1,4,6,3,43,23,12,90,100,34,23  = ", max(1,4,6,3,43,23,12,90,100,34,23))
print(f"Min from 1,4,6,3,43,23,12,90,100,34,23  = ", min(1,4,6,3,43,23,-12,90,100,34,23))

#sum : returns the sum of the elements in an iterable, with an optional start value (default is 0).
totalStudent = [5,6,4,2,6,2]
print("sum of 5 numbers  = ",sum(totalStudent,0))

#square root
print(f"Square root of 4  = ", math.sqrt(4))

#ceil : returns the smallest integer greater than or equal to x
print(f"ceil function of 2.4 is  = ",math.ceil(2.4))

#floor: This function returns the largest integer less than or equal to x
print(f"ceil function of 2.5 is  = ",math.floor(2.6))

#area of circle
r = int(input("enter the radius of circle "))
area = math.pi * pow(r,r)
print(f"Are of circle is : {area}")