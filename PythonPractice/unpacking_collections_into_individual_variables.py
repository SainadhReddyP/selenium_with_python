my_list = [1,3,5,7,9]

# unpacking the list
a, b, c, d, e = my_list
print(a)
# print(b)
# print(c)
# print(d)
# print(e)

my_tuple = (2,4,6,8)

f, g, h, i = my_tuple
print(f)


my_set = {11,12,13}

j, k, l = my_set
print(j)


my_dict = {'name':'Sainadh', 'age':28, 'location':'Hyderabad'}

m, n, o = my_dict  # unpack only keys
p, q, r = my_dict.values()  # unpack values
print(m)
print(p)


# unpack range() function

s, t, u, v = range(4)
print(s)