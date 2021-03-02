'''
lst= [23,44,56,78,54]
sum = 0
for x in lst:
    sum += x
print(sum)
'''

#Recuecive way
lst= [23,45,56,67,78,44]
def sumoflist(list, size):
    if size==0:
        return 1
    else:
        return list[size-1]+sum(list, len(list))
total =sumoflist(lst, len(lst))
print(total)