car_dict = {
    "type1": {
        "make": "Honda",
        "model": "Acura",
        "vin": "19UUA9F50DA000071"
    },
    "type2": {
        "make": "Audi",
        "model": "Audi",
        "vin": "WA1FFCFS6FR097108"
    },
    "type3": {
        "make": "Ford",
        "model": "F 150",
        "vin": "2FTRX08L82CA59097"
    }
}

print("Before Delete : ",car_dict)
# Way 1 : using del keyword
del car_dict["type2"]
print("After Deleted using del  : ",car_dict)

# Way 2: Using pop method
car_dict.pop("type3")
print("After Deleted using pop method : ",car_dict)


# Way 3 : Use clear to remove all items
car_dict.clear()
print("After clear all items : ",car_dict)