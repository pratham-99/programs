A = "Geeks for Geeks".split()
B = "Learning from Geeks for Geeks".split()
uc = ''
for i in A:
    if i not in B:
        uc = uc+" "+i
for j in B:
    if j not in A:
        uc = uc+" "+j
print(uc)
