familyDetails = ("Hindu","Asian",5,"Nepal")
print(type(familyDetails))
print(familyDetails)

# removing individual tuple elements is not possible.
# To explicitly remove an entire tuple, just use the del statement.
del familyDetails

# The code will result in an error because once the tuple familyDetails is deleted,
# trying to print it again will raise a NameError as the variable no longer exists.
print("After Deleted all : ",familyDetails)