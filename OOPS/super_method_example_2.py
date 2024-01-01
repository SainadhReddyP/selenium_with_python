

class A:

    def __init__(self):
        print("Inside __init__ method of Class A.")


class B(A):

    def __init__(self):
        super().__init__()
        print("Inside __init__ method of Class B.")

"""
it will invoke the constructor in Class A - when no constructor in Class B
But, when Class B (child class) has constructor - it will invoke constructor of Class B
By adding super().__init__() to child class - it will invoke parent class constructor first,
then invoke the child class constructor."""
obj_b = B()



