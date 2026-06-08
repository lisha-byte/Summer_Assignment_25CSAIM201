n = int(input("Enter number: "))
count = 0

while n > 0:
    count += n % 2  # add 1 if last bit is 1
    n = n // 2
    
print("Number of set bits:", count)
