def insertionSort (alist):
    for i in range(1,len(alist)):
        while i > 0 and alist[i - 1] > alist[i]: #swap > to < for decending sort
            alist[i], alist[i-1] = alist[i-1], alist[i]
            i -= 1
    return alist
 

print(insertionSort([1,2,3,4,5]))
print(insertionSort([5,2,3,4,5]))
print(insertionSort([2,1,4,5,5]))
print(insertionSort([3,2,1,4,5]))
print(insertionSort([5,4,3,2,1]))