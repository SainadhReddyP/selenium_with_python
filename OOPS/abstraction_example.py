from abc import ABC

"""
Abstract Class - which has to become child class of predefined parent Abstract class ABC.
Abstract Class-  partial implementation in it (Some are Abstract methods (doesn't have body in it)
(some are non-abstract methods -> implemented).
"""


class A(ABC):  # ABC is predefined parent abstract class

    # abstract methods - which does not have body in it.
    # Abstract method
    def method_one(self):
        pass

    # Abstract method
    def method_two(self):
        pass

    # Non-Abstract method
    def method_three(self):
        print("Inside methode three.")
