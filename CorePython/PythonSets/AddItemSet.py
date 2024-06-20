universityNames = {"Texas State University", "Saint Louis University", "University of Missouri", "University of Missouri St. Louis"}

# Add items to a set using add() method
universityNames.add("Illinois State University")
print(universityNames)

# using update method
universityNames.update(["Ohio State University"])
print("Using update method : ",universityNames)

# using union
universityRanks = {5,2,6,7,8,10}

universitiesInfo = universityNames.union(universityRanks)
print(universitiesInfo)