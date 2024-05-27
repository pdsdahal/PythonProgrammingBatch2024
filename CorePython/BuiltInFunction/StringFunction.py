collegeName = "ABC international College"
print(f"College Name : {collegeName}")

length = len(collegeName)
print(f"Length of {collegeName} : ", length)

print("Upper Case : ",collegeName.upper())
print("Lower Case : ",collegeName.lower())
print("Capitalize Case : ", collegeName.capitalize())
print("Title Case : ", collegeName.title())

print("Returns True if all characters in the string are digits : ",collegeName.isdigit())
print("Returns True if all characters in the string are in the alphabet : ",collegeName.isalpha())
print("Returns True if all characters in the string are alphanumeric : ",collegeName.isalnum())
print("Returns True if all characters in the string are lower case : ",collegeName.islower())
print("Returns True if all characters in the string are upper case : ",collegeName.isupper())


print("Returns true if the string starts with the specified value : ",collegeName.startswith("AB"))
print("Returns true if the string end with the specified value : ",collegeName.endswith("ege"))

#Split : The split() method splits a string into a list.
collegeNameList = collegeName.split(" ")
print(collegeNameList)

collegeNameList2 = collegeName.split(" ", 1)
print(collegeNameList2)

#Splits the string at line breaks and returns a list
address = "St. Louis City\nMissouri United States"
addressList = address.splitlines()
print(addressList)

#The count() method returns the number of times a specified value appears in the string.
message = "I love my girlfriend, girlfriend is beautiful."
count = message.count("girlfriend")
print("Return the number of times the value girlfriend appears in the string: ", count)

#replace : Returns a string where a specified value is replaced with a specified value
xyzCollegeName = collegeName.replace("ABC", "XYZ")
print(xyzCollegeName)

#Slicing: From index 4 to index 17 (exclusive)
sliceCollegeName = xyzCollegeName[4:17]
print("From index 4 to index 17 (exclusive) : ",sliceCollegeName)