from abc import ABC, abstractmethod

"""
Abstract Class - which has to become child class of predefined parent Abstract class ABC.
Abstract Class-  partial implementation in it (Some are Abstract methods (doesn't have body in it)
(some are non-abstract methods -> implemented).
"""


class A(ABC):  # ABC is predefined parent abstract class

    def __init__(self, a):
        self.a = a

    # abstract methods - which does not have body in it.
    # Abstract method
    @abstractmethod
    def method_one(self):
        pass

    # Abstract method
    @abstractmethod
    def method_two(self):
        pass

    # Non-Abstract method
    def method_three(self):
        print("Inside methode three.",self.a)


class B(A):  # Child Class of Parent Abstract Class

    # Implement all the abstract methods of parent abstract class
    def method_one(self):
        print("Inside method_one.")

    def method_two(self):
        print("Inside method_two.")


# TypeError:
# Can't instantiate abstract class A with abstract methods method_one, method_two

# obj = A()
# we can create child class and can create object for it

obj_b = B(5)
obj_b.method_one()
obj_b.method_two()
obj_b.method_three()

