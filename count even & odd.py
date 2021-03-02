lst = [6, 8, 4, 2, 1, 454, 87, 45, 312, 754, 654]

even_count, odd_count = 0, 0

for x in lst:
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count)
print(odd_count)
