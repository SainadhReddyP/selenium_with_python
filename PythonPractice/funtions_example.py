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


def multiple_parameters_function(a,b,c):
    """
    Description: function can contains any number of parameters
    :return:
    """
    result_sum = a + b + c
    print("The sum of "+str(a)+", "+str(b)+", "+str(c)+" is: "+str(result_sum))


def sum_of_three_numbers(num1,num2,num3):
    return num1+num2+num3

# function calling statements
my_function()
print_name("Sainadh")
default_argument_function()
default_argument_function("Reddy")
multiple_parameters_function(1,2,3)
result = sum_of_three_numbers(5,4,3)
print(result)

