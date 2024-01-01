class A:

    a = 1


class B(A):  # class b and c are children - and having the properties of class A

    b = 2


class C(A):

    c = 3


obj_c = C()
print(obj_c.c)
print(obj_c.a)

# we can access parent properties from both child classes B and C
obj_b = B()
print(obj_b.b)
print(obj_b.a)

