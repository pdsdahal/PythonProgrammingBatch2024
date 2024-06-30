class VariablesDemo:
    # class variables are define outside the constructor and shared
    # among all objects
    dob_year = 2021

    def __init__(self, name, age):
        # instance variables : define inside the constructor

        self.name = name
        self.age = age


varidemo = VariablesDemo("Ram Pandey", 13)
print(f"Student Details :\nName : {varidemo.name} \nAge : {varidemo.age}")
print(f"DoB : {VariablesDemo.dob_year}")
