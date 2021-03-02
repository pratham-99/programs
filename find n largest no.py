lst = [6, 8, 5, 4, 7, 22, 65, 34, 84, 74]
n = 3
final_list = []
for i in range(0, n):
    max1 = 0
    for j in range(len(lst)):
        if lst[j] > max1:
            max1 = lst[j]
    lst.remove(max1)
    final_list.append(max1)
print(final_list)

# second largest element
print(final_list[1])
