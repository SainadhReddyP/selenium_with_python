
car = {"Brand":"Honda", "Model":"Brio","Price":800000,"Mileage":19.5}

print(car)
print(type(car))

print(car.get('Model')) # retrieve the value of the given key
print(car['Model'])

# printing all the keys
print(car.keys())

# printing all the values
print(car.values())

# updating the values
print(car)
car['Price'] = 900000
print(car)

# add a new element
car['Color'] = 'White'
print(car)

# for loop with dictionary (for each loop)
for key in car:
    print(key) # keys will print

for key in car.keys(): # in-buit method
    print(key)

# print the values
for value in car.values():
    print(value)

# both keys and values
for key in car.keys():
    print(key,":",car[key])

# for key, values - items
for k,v in car.items():
    print(k,v)


#





















