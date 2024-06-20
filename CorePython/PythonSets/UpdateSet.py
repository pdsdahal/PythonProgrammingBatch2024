addresses = {"Nottingham Ave.", "Lockwood Ave", "Garden Ave"}
print("Before : ",addresses)

# first remove the element you want to update
# Add the new element

for address in addresses:
    if address == "Nottingham Ave.":
        addresses.remove(address)
        addresses.add("Nottingham Ave..")
        break

print("After Update : ", addresses)