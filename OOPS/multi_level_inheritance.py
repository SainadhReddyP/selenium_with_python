class A:  # Grand Parent
    a = 2


class B(A):  # Parent
    b = 3


class C(B):  # Child
    c = 4


obj_c = C()
print(obj_c.c)
print(obj_c.b)
print(obj_c.a)
