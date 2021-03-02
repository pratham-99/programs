str = "geek of geek in your world".split()
di = {}

for x in str:
    if x in di:
        di[x] += 1
    else:
        di[x] = 1

print(di)
