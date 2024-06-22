apartment_dict = {
    "apartment1": {"No.": 1778, "Street Name": "Brentwood 1", "City": "St. Louis"},
    "apartment2": {"No.": 1779, "Street Name": "Brentwood 2", "City": "St. Louis"},
    "apartment3": {"No.": 1780, "Street Name": "Brentwood 2", "City": "St. Louis"}

}


# Way 1 : Using []
print("Using [] : ",apartment_dict["apartment2"])

# Way 2 : Using get
print("Using get Method : ",apartment_dict.get("apartment3"))

#Way 3 : Access all the keys
print("All Keys : ",apartment_dict.keys())

#Way 4 : Access all the values
print("All Values : ",apartment_dict.values())

#Way 5: Iterating Over key in the Dictionary
for key in apartment_dict:
    print(f" key : {key} and value : {apartment_dict[key]}")

#Way 6: Iterating Over key and value in the Dictionary
print("\n\nIterating Over key and value in the Dictionary")
for key, value in apartment_dict.items():
    print(f"{key} = {value}")

# Way 7:  nested loops to fetch all the items from  nested Dictionary
print("\n\nNested loops to fetch all the items from  nested Dictionary")
for key, value in apartment_dict.items():
    if isinstance(value, dict):
        for key1, value1 in value.items():
            print(f"key : {key1} and value {value1}")
    else:
        print(f"Key : {key} and value : {value}")

# Way 8 : using recursive way
def fetch_all_data_from_dic(dicData):
    for key,value in dicData.items():
        if isinstance(value, dict):
            fetch_all_data_from_dic(value)
        else:
            print(f"key : {key} value : {value}")

print("\n\nUsing recursive approach : ")
fetch_all_data_from_dic(apartment_dict)