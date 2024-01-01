"""Polymorphism:
 Polymorphism - Method Overriding.
 - Overriding variables and methods
 - the properties in the child class match with the parent class.
 we can override properties."""


class A:

    a = 1

    def sample(self):
        print("Inside sample method of Class A")


class B(A):

    a = 2

    def sample(self):
        print("Inside sample method of Class B")


obj_b = B()
print(obj_b.a)  # overriden property will be printed (The latest property/assignment)
obj_b.sample()
