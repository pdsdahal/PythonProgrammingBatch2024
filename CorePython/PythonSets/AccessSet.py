# set : {} unordered and immutable, but add/ remove ok. No Duplicates

studentNames = {"Ram","Shyam","Hari","Gopal","Sita"}

# using while
#  set is unordered collection and don't support indexing.

studentNamesLst = list(studentNames)
flag = 0
while flag < len(studentNamesLst):
    print(f"Element at {flag} and value is {studentNamesLst[flag]}")
    flag = flag + 1


# accessing set using for loop
for studentName in studentNames:
    print(f"Student name is {studentName}")