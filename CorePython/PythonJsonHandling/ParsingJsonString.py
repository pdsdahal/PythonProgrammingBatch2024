import json

response = """{
  "name": "John",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York"
  },
  "phone_numbers": [
    {
      "type": "home",
      "number": "212-555-1234"
    },
    {
      "type": "work",
      "number": "646-555-4567"
    }
  ]
}"""

# Parse string to dictionary
json_response = json.loads(response)

name = json_response['name']
age = json_response["age"]
street = json_response["address"]["street"]
city = json_response["address"]["city"]

phone_numbers = json_response["phone_numbers"]
for phone_number in phone_numbers:
    type = phone_number["type"]
    number = phone_number["number"]

    print("Type : ",type)
    print("Number : ", number)

print("Name : ",name)
print("Age : ",age)
print("Street : ",street)
print("city : ",city)