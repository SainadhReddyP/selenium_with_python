# hybrid = hierarchical + multiple

class A:

    a = 1


class B(A):  # child of A

    b = 2


class C(A):  # child of A

    c = 3


class D(B,C):  # child of B and C

    d = 4


obj_d = D()
print(obj_d.d)
print(obj_d.c)
print(obj_d.b)
print(obj_d.a)

