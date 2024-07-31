x = int(input("Enter the number x : "))
y = int(input("Enter the number y : "))

# naive approach
def lcm1(x,y):
    result = max(x,y)
    temp = result
    i = 2
    while True:
        if temp%x == 0 and temp%y == 0:
            return temp
        temp = result*i
        i+=1


# optimized sol using gcd relationship
# lcm(x,y) = (x*y) / gcd(x,y)

def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def lcm2(x,y):
    return int((x*y)/gcd(x,y))

print(lcm2(x,y))