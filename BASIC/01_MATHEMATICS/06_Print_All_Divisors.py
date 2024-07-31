num = int(input("enter the number : "))

# naive approach
def allDivisors(num) : 
    for i in range(1,num+1) : 
        if num%i == 0 : 
            print(i, end=" ")

# optimized approach
def allDivs(num) : 
    result = []
    i = 1
    while i*i <= num : 
        if num%i == 0 :
            result.append(i)
            if num/i != i : 
                result.append(num//i)
        i+=1
    return result

print(allDivs(num))
