# Voting eligibility system
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    print("Wait for", 18 - age, "more years")