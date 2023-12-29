
for i in range(1,7):
    if i == 3:
        break # it will cancel the iteration after this
    print(i)

print("While-break")
j = 1
while j <= 7:
    if j == 5:
        break
    print(j)
    j = j+1
