def factorial (a):
    ans = 1
    for i in range(1,a+1):
        ans *= i
    return ans

def permutation(n,k):
    return factorial(n) / factorial(n - k)

def betterPermutation(n,k):
    assert k <= n , "k cannot be > n"
    ans = 1
    for i in range(n-k+1,n+1):
        ans *= i
    return ans 

def combination(n,k):
    return factorial(n) /  ( factorial(k) * factorial(n-k) )

def betterCombination(n,k):
    denum = 1
    for i in range(n-k+1,n+1):
        denum *= i
    return denum / factorial(k)
    

if __name__ == "__main__":
    print(factorial(4))
    print(permutation(7,5))
    print(betterPermutation(7,5))
    print(combination(9,2))
    print(betterCombination(9,2))