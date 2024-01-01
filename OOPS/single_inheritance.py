class A:
    a = 9


class B(A):
    b = 10


obj_b = B()
print(obj_b.b)
print(obj_b.a)
