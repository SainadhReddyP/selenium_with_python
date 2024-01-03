from PythonPractice import modules_in_python
from PythonPractice.modules_in_python import addition, subtraction, multiplication, divison
from PythonPractice.modules_in_python import *

print(dir(modules_in_python))  # This will return set of functions in the module

# Approach 1
r1 = modules_in_python.addition(4, 5)
print(r1)

r2 = modules_in_python.subtraction(5, 4)
print(r2)

r3 = modules_in_python.multiplication(4, 5)
print(r3)

r4 = modules_in_python.divison(5, 4)
print(r4)

# Approach 2
r1 = addition(4, 5)
print(r1)

r2 = subtraction(5, 4)
print(r2)

r3 = multiplication(4, 5)
print(r3)

r4 = divison(5, 4)
print(r4)


