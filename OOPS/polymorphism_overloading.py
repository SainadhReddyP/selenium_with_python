"""
Polymorphism:
Method overloading in python is not possible.
- but we can achieve by alternative ways
"""


class A:

    def sample(self, a=None, b=None):
        if a != None and b != None:
            print(a * b)
        elif a != None:
            print(a)
        else:
            print("Nothing.")


obj_a = A()
obj_a.sample()
