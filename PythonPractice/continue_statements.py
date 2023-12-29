
for i in range(1,7):
    if i == 3:
        continue # it will cancel current iteration
    print(i)

print("While-continue")

j = 1

while j <= 7:
    if j == 3:
        j = j+1 # without this the j won't be incremented.
        continue
    print(j)
    j = j+1


