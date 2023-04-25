import random

n = int(input("colichestvo ryadov:"))
m = int(input("colichestvo mestv cazhdom ryadu:"))
array = []
for i in range(n):
    row = []
    for j in range(m):
        number = random.randint(0,1)
        row.append(number)
    array.append(row)
for row in array:
    print(*row)

zero = 0
one = 0

for row in array: 
    for seat in row:
        if seat == 0:
            zero += 1
        else:
            one += 1
print(f"zanyato mest:{one}")
print(f"ne zanyato mest:{zero}")