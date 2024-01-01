"""
Private variable and Private methods:
The variables and methods which can only be accessed inside the class,
but cannot be accessed outside the class.
__variable__name or __method__name
can be accessed only within the class.
"""


class A:

    __a = 5

    def __sample(self):
        print("Inside sample method of Class A.")

    def print_details(self):
        print(self.__a)
        self.__sample()


obj_a = A()
# print(obj_a.a)
# obj_a.sample()
obj_a.print_details()