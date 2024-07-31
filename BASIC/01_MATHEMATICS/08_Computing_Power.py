# x = int(input("Enter the number : "))
# y = int(input("Enter the number : "))

# iterative sol, time complexity = O(logn)
def powerCompute(x,y):
    # base cases
    if y==0:
        return 1
    elif x==0:
        return 0
    
    negative = y<0
    y = abs(y)
    result = 1
    
    # main code
    while(y):
        if y%2==0:
            x*=x
            y//=2
        else:
            result = result*x
            y-=1

    # for negative power
    result = (1/result) if negative else result
    return result


