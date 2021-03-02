def swapList(newList):
    size=len(newList)
    temp = newList[0]
    newList[0]= newList[size-1]
    newList[size-1]=temp
    return newList
newList= [23,45,66,879]
print(swapList(newList))