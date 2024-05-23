collegeNameNpl = ["ABC", "XYZ", "KTM"]
collegeNameWorld = ["ABC", "XYZ", "KTM"]
collegeNameNepal = collegeNameNpl

isOp = collegeNameNepal is collegeNameNpl
isNotOp = collegeNameNpl is not collegeNameWorld

print(f"{collegeNameNepal} is {collegeNameNpl} = {isOp}")
print(f"{collegeNameNpl} is not  {collegeNameWorld} = {isNotOp}")