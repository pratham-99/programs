list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
rep = []

for i in range(len(list)):
    k = i + 1
    for j in range(k, len(list)):
        if list[i] == list[j] and list[i] not in rep:
            rep.append(list[i])

print(rep)
