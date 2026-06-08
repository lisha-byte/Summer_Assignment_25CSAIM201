b = input("Enter binary number: ")
decimal = 0
power = 0

for digit in reversed(b):
    decimal += int(digit) * (2 ** power)
    power += 1
    
print("Decimal:", decimal)