#  Numerical methods for describing data

import math
def mean(nums):
    return sum(nums)/len(nums)

def median(nums):
    midpoint = len(nums) // 2
    if len(nums) % 2 :
        return nums[midpoint]
    else:
        return (nums[midpoint] + nums[midpoint +1])/2

def standardDeviation(nums):
    m = mean(nums)
    denum = 0
    for i in nums:
        denum += ( i - m ) **2  
    return math.sqrt( denum / (len(nums)-1) )

def IQR(nums):
    if len(nums) % 2:
        Q1 = median(nums[:len(nums)//2])
        Q2 = median(nums[len(nums)//2 + 1:])
    else:
        Q1 = median(nums[:(len(nums))//2])
        Q2 = median(nums[(len(nums))//2:])     
    return (nums[0],Q1,median(nums),Q2,nums[-1])


if __name__ == "__main__":
    # nums = [727.7,1086.5,1091.0,1361.3,1490.5,1956.1]
    nums = [3, 5, 7, 8, 9, 11, 15, 16, 20, 21]
    # nums = [1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27]
    
    print(mean(nums))
    print(median(nums))
    print(standardDeviation(nums))
    print(IQR(nums))