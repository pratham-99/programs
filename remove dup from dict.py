test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
temp = []
res = {}
for key, val in test_dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)
