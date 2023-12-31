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
print(first_name[0]) # Indexing is possible
print(len(first_name)) # finding length(size)

# for each loop
for char in first_name:
    print(char)

# for loop with range
for c in range(len(first_name)):
    print(first_name[c],end="")
print("\n")

# in and not in operators
print("Sai" in first_name)

# slicing
print(first_name[1:3])

# Modifying Strings
print(first_name.upper())
print(first_name.lower())
print("  Sainadh Reddy    ".strip()) # to remove leading and trailing spaces
print(first_name.replace("d","t")) # replacing d with t

name = "Sainadh Reddy"
print(name.split()) # returns list












