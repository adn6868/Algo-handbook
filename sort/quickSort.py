def quickSort(unsorted):
    length = len(unsorted)
    if (length <= 1):
        return unsorted

    pivot = unsorted[0]
    greater = []
    lesser = []
    for i in unsorted[1:]:
        if i > pivot:
            greater.append(i)
        else:
            lesser.append(i)
    return quickSort(lesser) +[pivot] + quickSort(greater)



print(quickSort([1,2,3,4,5]))
print(quickSort([5,2,3,4,5]))
print(quickSort([2,1,4,5,5]))
print(quickSort([3,2,1,4,5]))
print(quickSort([5,4,3,2,1]))