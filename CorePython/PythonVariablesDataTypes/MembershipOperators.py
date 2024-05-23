#Membership operators are used to test if a value or variable is present in a
#sequence such as strings, lists, tuples, sets, and dictionaries.

#String
collegeName = "ABC International College"
resultCheckInString = "B" in collegeName
print(f"Membership Operator check in result : {resultCheckInString}")

#list
studentNames = ["Ram", "Shyam","Hari", "Gita","Sita"]
resultCheckInList = "Hari" in studentNames
print(f"Hari is present in {studentNames} : {resultCheckInList}")

#tuple
rollNo = (1,5,7,3,2,6)
resultTupleCheck = 2 in rollNo
print(f"2 in {rollNo} : {resultTupleCheck}")

#sets
setA = {1,2,5,7,4}
resultSetCheck = 5 in setA
print(f"5 in {setA} : {resultSetCheck}")

#Dictionaries
studentId = {"Ram":1, "Shyam":20, "Gita": 10}
resultDictionariesKeycheck = "Shyam" in studentId
print(f"Shyam in {studentId} : {resultDictionariesKeycheck}")