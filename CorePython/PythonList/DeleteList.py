apartmentInfo = ["2Bhk","Baltimore",1012, 405, 4,"2 Bathrooms"]
print(apartmentInfo)

# del statement to remove items at a specific index.
del apartmentInfo[0]
print("After deleting index 0 : ",apartmentInfo)
# Using remove method

apartmentInfo.remove("2 Bathrooms")
print("After deleting the item (2 Bathrooms) : ",apartmentInfo)

# Remove List Item Using pop()
apartmentInfo.pop(1)
print("After deleting the item from index 1 : ",apartmentInfo)

# Remove all List Item Using clear() Method
apartmentInfo.clear()
print("After clear method : ",apartmentInfo)