try:
    num1 = 10
    num2 = 2
    num3 = int('12')
    data_list = [1,5,9,10]
    result1 = num1/num2
    result2 = num3
    result3 = data_list[0]

    print(f"{result1}")
    print(f"{result2}")
    print(f"{result3}")
except (ValueError, ZeroDivisionError, IndexError) as e:
    print(f"Error Description : {e}")