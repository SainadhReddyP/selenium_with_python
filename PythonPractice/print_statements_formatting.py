name = "Sainadh Reddy"
location = "Hyderabad"

print("I am "+name+". I am from "+location+".")
print("I am",name+". I am from",location+".")
print("I am {}. I am from {}.".format(name,location))
print("I am {1}. I am from {0}.".format(location,name)) # with index
print("I am %s. I am from %s."%(name,location)) # %s - string, %d - integer, %f - float, %g - correct float

age = 29.5
print("I am %s. I am %d old."%(name,age))
print("I am %s. I am %f old."%(name,age))
print("I am %s. I am %g old."%(name,age))



