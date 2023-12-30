my_set = {8, 4, 9, 7, 3}
print(my_set)

# indexing is not possible in set
# print(my_set[2]) #TypeError: 'set' object is not subscriptable

my_set = {8, 9, 3, 4, 9, 7, 3}

# duplicates are ignored
print(my_set)
print(type(my_set))  # type of data
print(len(my_set))  # finding length

print(my_set)
my_set.add(5)
print(my_set)

# add multiple elements at a time
my_set.update([1, 2])
print(my_set)

# removing the elements from the set
my_set.remove(5)
print(my_set)

# removing the values from Set without knowing where it is available in the Set
# my_set.remove(11) # Key error, becoz 11 is not there in the set
my_set.discard(11)  # it will remove if it presents, not there it will ignore

my_set.pop()  # randomly it will remove element from the set
print(my_set)

my_set.clear()  # set became empty, but empty set will present
print(my_set)

del my_set

# print(my_set) # NameError: name 'my_set' is not defined - becoz, deleted my_set in previous step

fruits = {'orange', 'apple', 'guava', 'banana'}
for fruit in fruits:
    print(fruit)

# we cannot use for loop with range function, becoz, there is no index in set

print('apple' in fruits)
print('apple' not in fruits)

print('strawberry' in fruits)
print('strawberry' not in fruits)

# set can only nest tuple
# my_set = {2,7,{4,3},8,1}
# print(my_set) #TypeError: unhashable type: 'set'

my_new_set = {1, 8, (2, 5, 4), 3}
print(my_new_set)

# converting a list to a set
my_list = [1,2,3,4,5]
my_set = set(my_list)
print(type(my_set))


# union of sets, intersection, difference & symmetric difference
a = {1,3,4,5,1,7}
b = {2,6,8,7,2,4}

print(a.union(b))
print(a | b) # union

print(a.intersection(b))
print(a & b) # intersection - common elements

print(a.difference(b)) # difference - a-b
print(a-b)

# symmetric difference
print(a.symmetric_difference(b))
print(a ^ b)

print(max(a))
print(min(a))
