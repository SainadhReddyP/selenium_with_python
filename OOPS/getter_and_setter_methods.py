"""
Using Getter and Setter methods with private variables
- Getter and Setter non-private methods can be used for accessing the private variables.
"""

class A:

    __age = 0  # private variable - can only be accessible inside the class

    def set_age(self,age):
        A.__age = age

    def get_age(self):
        return A.__age

obj = A()
# print(obj.__age)  # cannot access private variable

obj.set_age(28)
print(obj.get_age())


