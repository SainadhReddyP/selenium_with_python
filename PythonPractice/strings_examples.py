# creating strings
first_name = "Sainadh"
last_name = 'Reddy'
location = str("Hyderabad")

print(first_name)
print(last_name)
print(location)

print(type(first_name))
print(type(last_name))
print(type(location))

# strings work like collections
print(first_name[0])  # Indexing is possible
print(len(first_name))  # finding length(size)

# for each loop
for char in first_name:
    print(char)

# for loop with range
for c in range(len(first_name)):
    print(first_name[c], end="")
print("\n")

# in and not in operators
print("Sai" in first_name)

# slicing
print(first_name[1:3])

# Modifying Strings
print(first_name.upper())
print(first_name.lower())
print("  Sainadh Reddy    ".strip())  # to remove leading and trailing spaces
print(first_name.replace("d", "t"))  # replacing d with t

name = "Sainadh Reddy"
print(name.split())  # returns list

# Strings are immutable - not updatable or modifiable
name = "Sainadh"  # stored in one memory space
print(id(name))

name = "Reddy"  # another memory space is getting allocated
print(id(name))

# we are not updating the old name, but creating a new
# so strings are not updatable and not modifiable - are immutable

# in-built functions
# capitalize - first letter will be capital
name = "my name is sainadh"
print(name.capitalize())  # only first letter

print(name.title())  # first letter of each word in the statement gets capitalized

# returns the number of times the given word is available in the string
print(name.count("a"))

my_text = "My name is Sainadh. I am learning Python. Python is an easy language."

print(my_text.count("Python"))

# returns index if found, otherwise returns -1
print(my_text.find("Sainadh"))  # index will return
print(my_text.find("Python"))  # first occurence will return
print(my_text.find("Java"))

# comparing strings
# using ==
name1 = "Sainadh"
name2 = "Sainadh"
name3 = "Reddy"

print(name1 == name2)
print(name1 == name3)
print(name1 == name2)

print(".__eq__() function")
# using .__eq__() function
print(name1.__eq__(name2))
print(name1.__eq__(name3))

print("casefold function")
# casefold() - name1.casefold() == name2 (without case comparison)
name1 = "Sainadh"
name2 = "sainadh"
name3 = "Reddy"
print(name1 == name2)
print(name1.casefold() == name2)