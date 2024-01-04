"""
Exception are the errors which occur while running the code.
-
"""

# a = 10/0
#
# print(a)  # ZeroDivisionError: division by zero

number = int(input("Enter any number: "))

try:
    a = 10/number
    print(a)
except ZeroDivisionError as ex:
    print("Exception occurred:",ex)

print("End of the program.")

