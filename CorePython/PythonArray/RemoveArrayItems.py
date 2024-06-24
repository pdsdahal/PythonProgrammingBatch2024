import array as arr

total_income = arr.array('i',[100,300,200,500,400])


# Way 1:  remove the first occurrence of a given value from the array, use remove() method.
print("Before Remove method : ",total_income)
total_income.remove(300)
print("After Remove method : ",total_income)

# Way 2: Remove Items from Specific Indices using the pop() method
total_income.pop(-1)
print("After Removing last element : ",total_income)
