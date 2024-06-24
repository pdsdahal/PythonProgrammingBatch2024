import array as arr

rollNos = arr.array("i",[6,4,3,2,7,9,1])

# Way 1: Using index
print("Value at 0 index : ",rollNos[0])
print("Value at 1 index : ",rollNos[1])
print("Value at 2 index : ",rollNos[2])
print("Value at 3 index : ",rollNos[3])
print("Value at last index : ",rollNos[-1])

# Way 2 : Using iteration
print("\n\nUsing Iteration")
for rollNo in rollNos:
    print(rollNo)


# Way 3: Using enumerate() function
print("\n\nUsing Enumerate")
for index, value in enumerate(rollNos):
    print(f"{index} at {value}")


# Example Array Sorting using bubble sort
room_nos = arr.array("i",[10,7,4,1,9,2,45,2])

for i in range(0,len(room_nos)):
    for j in range(i+1,len(room_nos)):
        if room_nos[i] > room_nos[j]:
            temp = room_nos[i]
            room_nos[i] = room_nos[j]
            room_nos[j] = temp

print("After Sorting : ",room_nos)
