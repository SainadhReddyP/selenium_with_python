class A:  # parent class

    a = 1


class B:  # parent class

    b = 2


class C(A,B):  # child class

    c = 3


obj_c = C()
print(obj_c.c)
print(obj_c.b)
print(obj_c.a)