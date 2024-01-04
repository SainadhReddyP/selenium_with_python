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
else:
    print("Inside else block.")
finally:
    print("Inside finally block.")

print("End of the program.")


# Raise custom exception messages
try:
    raise ZeroDivisionError("Dividing a number by zero")
except ZeroDivisionError as ex:
    print("Exception got handled:",ex)