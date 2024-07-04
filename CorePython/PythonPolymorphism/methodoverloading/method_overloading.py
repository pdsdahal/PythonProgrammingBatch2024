# Method overloading : Define multiple methods in a class with the same name but different parameters.

# Python does not support method overloading in the traditional sense as seen in languages like Java or C++.
# Instead, Python achieves a similar effect through default arguments,
# variable-length arguments, and type-checking within a single method definition.

class University:
    # way 1: using default arguments
    def university_info(self, name, address=""):
        print(f"University Name is {name}.")
        print(f"University Address is {address}.")
        print()

    # way 2 : using variable-length arguments
    def univeristy_details(self, *args):
        for arg in args:
            print(arg)
        print()

    # way 3: using conditional logic:

    def show_university_info(self, university_name=None, university_address=None, university_city=None):
        if university_name is not None and university_address is not None and university_city is not None:
            print(f"University Name = {university_name}")
            print(f"University Address = {university_address}")
            print(f"University City = {university_city}")
            print()


        elif university_name is not None and university_address is not None:
            print(f"University Name = {university_name}")
            print(f"University Address = {university_address}")
            print()

        else:
            print(f"University Name = {university_name}")
            print()


university = University()

# call way 1
university.university_info("Khwopa", "St.Louis")
university.university_info("Webster")

# call way 2
university.univeristy_details("St. Louis", "USA")
university.univeristy_details("St. Louis", "USA", "Saint Louis City")

# call way 3
university.show_university_info("Texas State University", "Texas", "Texas")
university.show_university_info("Illinois State University", "Illinois")
university.show_university_info("New York State University")
