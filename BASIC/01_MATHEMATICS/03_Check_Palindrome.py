x = input("enter the string : ")

# for strings & numbers -> using slicing
def isPalindrome(x):
    rev = x[::-1]
    return x==rev

# for numbers only
def isPal(x) : 
    num = int(x)
    rev = 0
    while num : 
        digit = num%10
        rev = (rev*10) + digit
        num//=10
    return rev==int(x)

print(isPal(x))