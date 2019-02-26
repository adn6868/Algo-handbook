def bubbleSort(alist):
    length = len(alist)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if alist[j] > alist[j+1]:
                swapped = True
                alist[j] , alist[j+1] = alist[j+1], alist[j]
        if not swapped: break
    return alist


print(bubbleSort([1,2,3,4,5]))
print(bubbleSort([5,2,3,4,5]))
print(bubbleSort([2,1,4,5,5]))
print(bubbleSort([3,2,1,4,5]))
print(bubbleSort([5,4,3,2,1]))