# writing mode - 'm'
file = open("../testdata/data.txt", "w")
file.write("Hi! My name is Sainadh Reddy.\n")
file.write("I am learning Python.")
file.close()

# reading mode - 'r'
file = open('../testdata/data.txt','r')
# all characters will be read here
data = file.read()
print(data)
file.close()

# 15 characters will be read here
file = open('../testdata/data.txt','r')
data = file.read(29)
print(data)
file.close()

# Read all lines in the list format
file = open('../testdata/data.txt','r')
data = file.readlines()
print(data)
print(data[0])
for line in data:
    print(line)
file.close()

# Read line by line but only one line
print("Reading line by line.")
file = open('../testdata/data.txt','r')
# data = file.readline()
print(file.readline())  # first line
print(file.readline())  # second line
# print(data)
file.close()

# appending - 'a'
file = open('../testdata/data.txt','a')
file.write('\n Python is an easy programming language.')
file.close()


# for each loop
print("Using for each loop.")
file = open('../testdata/data.txt','r')
for line in file:
    print(line)