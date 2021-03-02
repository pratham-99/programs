lst = [10, -9, 3, 6, -4, 8, -7]

posi_count, neg_count = 0, 0

for x in lst:
    if x >= 0:
        posi_count += 1
    elif x < 0:
        neg_count += 1
print(posi_count)
print(neg_count)
