fruites = ["Apple", "Banana", "Strawburry", "Pineapple", "Orange", "Apple"]

# size
print(f"Size is : {len(fruites)}")

falful = fruites.copy()
print("By using copy : ",falful)

# Returns count of how many times obj occurs in list
print(fruites.count("Apple"))

# Reverses objects of list in place
fruites.reverse()
print("After Reverse : ",fruites)

#sorting
fruites.sort(reverse=True)
print("sorted in descending order : ",fruites)

fruites.sort(reverse=False)
print("sorted in ascending order : ",fruites)

# Join Lists

vitamins = ["A","B","C","D"]

for vitamin in vitamins:
    fruites.append(vitamin)

print("After Joined ",fruites)

# Using extend()
fruites.extend(vitamins)
print("After Extend : ", fruites)