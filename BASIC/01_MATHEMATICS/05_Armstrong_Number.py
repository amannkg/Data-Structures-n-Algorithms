# armstrong number -> number that is equal to the sum of its own digits each raised to the power of the number of digits

num = int(input("enter the number : "))
temp = num
count = 0
while temp :
    temp = temp//10
    count+=1

def isArmstrong(num) : 
    n = num
    sum = 0
    while n : 
        digit = n%10
        sum = sum + digit**count
        n//=10
    return sum == num

print(isArmstrong(num))
