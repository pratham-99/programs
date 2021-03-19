lst= [23,45,657,78,90,76,10,34,23,56,75,4]
mid = int(len(lst)/2)

if len(lst)%2==0:
    print(lst[mid], lst[mid-1])
else:
    print(lst[mid])