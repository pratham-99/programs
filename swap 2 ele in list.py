newList = [23,435,57,78,45]
po1= 0
po2 = 4

def swapList(newList):
    newList[po1], newList[po2]= newList[po2], newList[po1]
    return newList
print(swapList(newList))