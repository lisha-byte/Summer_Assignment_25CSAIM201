# Function to check perfect number
def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    
    if sum == n:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_perfect(num):
    print(num, "is Perfect Number")
else:
    print(num, "is Not Perfect Number")