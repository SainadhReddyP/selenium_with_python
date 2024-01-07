import random

#  using random()
print(random.random())
print(random.random()*100)
print(int(random.random()*100))  # between 0-100
print(int(random.random()*1000))  # between 0-1000

# using randint() - between a range
print(random.randint(1,10))  # between 1 and 10
print(random.randint(1,100))  # between 1 and 100


# using randrange() - last item 100 won't be considered. but randint() considers it
print(random.randrange(1,10))

