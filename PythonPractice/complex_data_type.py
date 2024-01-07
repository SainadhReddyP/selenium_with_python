"""
Complex data type is used while developing scientific applications
where complex mathematical operations are required.
- syntax:
real + imaginary j

j - means -> square root of -1
example:
3+5j


-> Real value of complex data type is optional

c = 10j
"""
c = 3+5j
d = 1+4j
e = 10j
print(type(c))  # <class 'complex'>
print(c)

print(c.real)
print(c.imag)

# we can perform operations
print(c+d)

print(type(e))
print(e)
print(e.real)
