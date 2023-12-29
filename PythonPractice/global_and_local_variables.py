def my_method():
    name = "Sainadh Reddy"
    print(name)


my_name = "Sainadh Reddy"  # outside the function - global variable


def my_language():
    global language # declare global variable inside function with global keyword
    language = "Python"
    print(language)


# print(name) # NameError: name 'name' is not defined
"""we cannot the access name outside the function.
Because name is local variable present inside the function."""

print(my_name)
my_language()