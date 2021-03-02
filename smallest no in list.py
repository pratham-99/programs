'''lst= [34,56,78,34,45,2,67]
minimum=lst[0]
for x in lst:
    if x<minimum:
        minimum=x

print(minimum)
print(min(lst))'''

lst=[]
num=10
for i in range(1, num+1):
    ele = int(input("Enter no: "))
    lst.append(ele)

print(lst)