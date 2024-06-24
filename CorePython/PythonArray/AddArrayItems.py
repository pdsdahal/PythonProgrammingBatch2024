import array as arr

total_students_count = arr.array('i',[10,30,50,60,80,100,110])

# Using append() method
print(f"Before : {total_students_count}")
total_students_count.append(160)
print(f"After : {total_students_count}")

# Using insert() method
# i − The index at which new value is to be inserted.
# v − The value to be inserted. Must be of the arraytype.
total_students_count.insert(2,200)
print(f"After : {total_students_count}")
