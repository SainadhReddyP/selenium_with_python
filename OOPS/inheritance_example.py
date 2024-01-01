class A:  # Parent class
    a = 9

    def method_a(self):
        print("Inside method_a")


class B(A):  # Child class - acquiring properties of Class A (Parent class)
    b = 10

    def method_b(self):
        print("Inside method_b")


obj_b = B()
print(obj_b.b)
print(obj_b.a)
obj_b.method_b()
obj_b.method_a()
