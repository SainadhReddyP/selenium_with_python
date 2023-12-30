my_tuple = (1,2,3,4,5,6,7)

print(my_tuple)

# my_tuple[2] = 8 # TypeError: 'tuple' object does not support item assignment
# we cannot update the tuple

# access values in tuple
# Indexing - starts from 0 - forward index
print(my_tuple[3])

# backward index - starts from -1
print(len(my_tuple))
print(my_tuple[-3]) # -1+len(my_tuple)=-3+7=6

# for loop with range function
for i in range(len(my_tuple)):
    print(my_tuple[i])

# for each function
cars = ['Brio','Swift','Indica','Altroz','Nexon']
for car in cars:
    print(car)

# slicing
print(cars[1:4]) # stop index not included

# using in and not in operators
print(5 in my_tuple)
print(5 not in my_tuple)

# tuple methods
my_tuple = (1,5,2,5,6,5,7,5)
print(my_tuple.count(5))
print(sum(my_tuple))
print(max(my_tuple))
print(min(my_tuple))

print(my_tuple.index(5))

del my_tuple

my_tuple = (1,2,3,4,5)
print(type(my_tuple))


# nested tuple
nested_tuple = (1,2,(3,4,5),6,7)
print(nested_tuple[2])
print(nested_tuple[2][1])

# nesting list into a tuple

tuple_list = (1,2,3,[4,5,6,7],8,9)

print(tuple_list[3][1])
# we can modify list inside a tuple
tuple_list[3][2] = 5
print(tuple_list)


# Type Casting string into a tuple
my_string = "Sainadh"
print(type(my_string))
my_tuple = tuple(my_tuple)
print(type(my_tuple))

