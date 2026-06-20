# Function to check Armstrong
def is_armstrong(n):
    num = n
    digits = len(str(n))
    sum = 0
    
    while n > 0:
        digit = n % 10
        sum = sum + digit ** digits
        n = n // 10
    
    if num == sum:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is Armstrong Number")
else:
    print(num, "is Not Armstrong Number")