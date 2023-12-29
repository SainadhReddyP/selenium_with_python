my_list = [1,3,5,7,9]
print(my_list)

# indexing
print(my_list[2])
print(my_list[0])

# length of list
print(len(my_list))

# for each loop
for i in my_list:
    print(i)

# for loop with range function
for i in range(len(my_list)):
    print(my_list[i])

# appending - at last
my_list.append(11)
print(my_list)

# Insert a value at specific index
my_list.insert(2,4)
print(my_list)

# remove
my_list.remove(4)
print(my_list)

# pop- remove last element in the list
my_list.pop()
print(my_list)

# pop(index)
my_list.pop(1)
print(my_list)

# clear() - all elements in the list - but list will present - empty list
# my_list.clear()
# print(my_list)

# reverse()
my_list.reverse()
print(my_list)

# sorting
new_list = [2,5,6,7,8,1,3,9,4]
new_list.sort()
print(new_list)

# sorting - alphabetical order - default ascending order
colors = ["orange","green","white","blue","yellow","red"]
colors.sort()
print(colors)

# index with list - returns index of a number 1 in that list
print(new_list.index(1))


# nested list - list inside a list
nested_list = [1,2,[3,4,5],6,7]
print(nested_list[2]) # child list will print

print(nested_list[2][1]) # get specific element in a child list

# we can store multiple data types in a list
cars = ['Honda','Brio',19.5,'Petrol',True,800000]
print(cars[1])

# forward index - my_list[1]
# backward index - my_list[-1]
# backward index can be calculated by -index_len(list)
my_list = [1,2,3,4,5]
print(my_list[-2]) # (-2+5)= 3 - returns 4


# slicing
print(my_list[1:4]) # index:position or stop index-1

print(my_list[1:]) # starts from 1 index and go till end


new_list=[1,5,1,3,4,5,6,7,8,9,4,5,6,7,3,4,5,3,4,5,6,5]
print(new_list.count(5)) # count of the element
print(max(new_list)) # highest value in the list
print(min(new_list)) # lowest value in the list
print(sum(new_list)) # sum of the elements in the list

print(type(new_list)) # type

del new_list # deleting the list


# using in and not in operators

new_list = [1,2,3,4,5,6,7,8,9]
print(5 in new_list) # true
print(10 in new_list) # false

# concatenate two list using + operator
a = [1,2,3,4,5]
b = [4,5,6,7,8,9]
c = a+b
print(c)

# extend the list
a = [1,2,3,4,5]
b = [4,5,6,7,8,9]

a.extend(b)
print(a)
