lst = [45, 98, 47, 35, 14, 22, 48, 66]

for i in lst:
    if i % 2 == 0:
        lst.remove(i)
print(lst)
