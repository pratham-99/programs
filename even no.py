lst = [61, 4, 5, 48, 33, 47, 95, 75, 12, 45, 78]
even = []
odd = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)

print(even)
print(odd)
