personal_details = dict(
    personal1={
        "name": "Ram Pandey",
        "id": 11,
        "address": "St. Louis"
    },
    personal2={
        "name": "Sita Pandey",
        "id": 12,
        "address": "Texas"
    })

print("Before Item added : ",personal_details)

# Way 1: Using [] bracket
personal_details["personal3"] = {
    "name": "Hari Dahal",
    "id": 13,
    "address": "Brentwood"
}

print("After Item added : ",personal_details)

# Way 2: Using update Method
personal_details.update(perosnal4={
    "name": "Shyam Dahal",
    "id": 14,
    "address": "Crickwood"
})

print("After Item added using update: ",personal_details)