num = int(input("enter the number : "))
def isPrime(num) :
    if num <= 1 : 
        return False
    i = 2
    while i*i <= num : 
        if num%i == 0:
            return False
        i+=1
    return True