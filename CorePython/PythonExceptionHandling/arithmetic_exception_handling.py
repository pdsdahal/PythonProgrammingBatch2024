# If there is no exception, then only try clause will run, except clause will not get executed.
# If any exception occurs, the try clause will be skipped and except clause will run.


num1 = 10
num2 = 0

try:
    result = num1/num2
    print(f"{num1} / {num2} = {result}")

except ArithmeticError as e:
    print(f"Error Description : {e}")
