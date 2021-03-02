x = int(input("Enter a no: "))
y = "4"
sum = ""
for i in range(1, x + 1):
    sum += y * i
    if i != x:
        sum += "+"
print(sum)
