def mergeSort(alist):
    length = len(alist)
    if length > 1:
        mid = length // 2
        left = mergeSort(alist[:mid])
        right = mergeSort(alist[mid:])
        i = 0
        j = 0 
        k = 0
        left_len = len(left)
        right_len = len(right)
        while i < left_len and j < right_len:
            if left[i] < right[j]:
                alist[k] = left[i]
                i+=1
            else:
                alist[k] = right[j]
                j+=1
            k+=1
        while i < left_len:
            alist[k] = left[i]
            i+=1
            k+=1
        
        while j < right_len:
            alist[k] = right[j]
            j+=1
            k+=1
    return alist



print(mergeSort([1,2,3,4,5]))
print(mergeSort([5,2,3,4,5]))
print(mergeSort([2,1,4,5,5]))
print(mergeSort([3,2,1,4,5]))
print(mergeSort([5,4,3,2,1]))