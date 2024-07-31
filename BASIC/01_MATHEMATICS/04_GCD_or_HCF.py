x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

# naive approach, time complexity -> O(min(x,y))
def findGCD(x,y) : 
    div = min(x,y)
    for i in range(div,0,-1) : 
        if x%i == 0 and y%i == 0 :
            return i
        
# using Eucledean method, gcd(x,y) = gcd (x-y,y) if x>y
def gcd(x,y) : 
    if x==0 : 
        return y
    if x<y : 
        x,y = y,x
    return gcd(x-y,y)

# improved eucledean
# more efficiently -> gcd(x,y) = gcd(x%y,y)
# time complexity -> O(log(min(x,y)))
def improvedGCD(x,y)  :
    if x==0 : 
        return y
    if x<y : 
        x,y = y,x
    return improvedGCD(x%y,y)

# using loops
def gcd2(x,y):
    while x>0 and y>0:
        if x>y :
            x = x%y
        else :
            y = y%x

    return y if x==0 else x

# more concised solution applying same concept
def gcd3(x,y):
    while y:
        x,y = y,x%y
    return x