def isFascinating(num):
    freq = [0] * 10
    val = (str(num) + str(num * 2) +
           str(num * 3))
    for i in range(len(val)):
        digit = int(val[i])
        if freq[digit] and digit != 0 > 0:
            return False
        else:
            freq[digit] += 1
    for i in range(1, 10):
        if freq[i] == 0:
            return False
    return True
num = 192
if num < 100:
    print("No")
else:
    ans = isFascinating(num)
    if ans:
        print("Yes")
    else:
        print("No")