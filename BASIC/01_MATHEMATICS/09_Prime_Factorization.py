n = int(input("Enter the number : "))

def isPrime(n):
    if n<=1:
        return False
    i = 2
    while i*i<=n:
        if n%i == 0:
            return False
        i+=1
    return True

# naive approach, time complexity -> O(sqrt(n)*sqrt(n)) = O(n)
def primeFactors1(n):
    result = []
    i = 2
    while i*i<=n:
        if n%i == 0:
            if isPrime(i):
                result.append(i)
            if n//i != i :
                if isPrime(n//i) : 
                    result.append(n//i)
        i+=1
    return result



# optimized sol,time complexity = O(sqrt(n)log(n))
def primeFactors2(n):
    result = []
    for i in range (2, int(n**0.5)) : 
        if n%i == 0 : 
            result.append(i)
        while n%i == 0 :
            n = n//i
    if n!=1 : 
        result.append(n)
    return result

print(primeFactors2(n))
