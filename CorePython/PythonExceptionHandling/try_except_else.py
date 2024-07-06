university_name = None

try:
    u_length = len(university_name)
    print("Length is : ", u_length)
except Exception as e:
    print("Error : ", e)

# Else: If there is no exception then this block will be executed

else:
    print("Inside the else block.")
