
colors = ['orange','red','green','white','blue']

print('orange' in colors)
print('orange' not in colors)
print('violet' not in colors)
print('violet' in colors)

# for loop with range
for color in range(len(colors)):
    print(colors[color])

# for each loop
for color in colors:
    print(color)

my_message = "Python is an easy programming language."

print("Python" in my_message)
print("Java" in my_message)
print("Java" not in my_message)
