"""
super()
- Accessing or Calling the parent class properties (variables and methods) from child class,
which are having the same name as child class properties.
- if the child class doesn't have any constructor and the parent class has a constructor,
it will be automatically invoked on creating an object for child class.
- but if the child class has its own constructor, then the parent class constructor
won't be invoked, and we have to call it explicitly from child class constructor using super().
"""

class A:

    a = 1

    def sample(self):
        print("Inside sample method of Class A.")


class B(A):
    a = 2

    def sample(self):
        print("Inside sample method of Class B.")

    def print_properties(self):
        # print(self.a)  # it will fetch same class variable
        # self.sample()  # # it will fetch same class method
        print(super().a)
        super().sample()


# Here, it will print the child class variable values and methods - when we use it with self.
# But, when we use super() while calling variables and methods - it will fetch parent properties.

obj_b = B()
obj_b.print_properties()


