# Default arguments in Python are the function arguments that will be used
# if no arguments are passed to the function call.
def birthday_song(age, name="Ram Pandey"):
    print(f"Happy Birthday to you! {name}")
    print(f"Your age is {age}")


# first call to the function doesn't pass value to name argument,
# hence its default value Ram Pandey is used.
birthday_song(13)

birthday_song(12,"Shyam")
