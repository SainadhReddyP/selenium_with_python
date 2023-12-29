def my_function():
    print("Function is a block of code.")


def print_name(name):
    print("Your name is: "+name)


def default_argument_function(name='Sainadh'):
    """
    Description: When you are not passing any argument,
    it will execute with the default argument.
    :param name:
    :return:
    """
    print("My name is: "+name)


# function calling statements
my_function()
print_name("Sainadh")
default_argument_function()
default_argument_function("Reddy")