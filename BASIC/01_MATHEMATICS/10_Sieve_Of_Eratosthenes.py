import math
n = int(input("Enter the number : "))
def simpleSieve(n):
    # primeList = [1 for _ in range(n+1)]
    primeList = [True]* (n+1)
    
    i = 2
    # time complexity -> O(n(loglog(n)))
    while i*i <= n:
        if primeList[i]==True:
            for j in range(i*i,n+1,i):
                primeList[j]=False
        i+=1
    
    result = [i for i in range(2,n+1) if primeList[i]==True]
    return result

print(simpleSieve(n))