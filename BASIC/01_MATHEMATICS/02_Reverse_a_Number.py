num = int(input("Enter The Number : "))
rev = 0
while num : 
    digit = num%10
    rev = (rev*10) + digit
    num//=10

print(rev)
