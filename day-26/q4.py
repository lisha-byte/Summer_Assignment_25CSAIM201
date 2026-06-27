# Simple quiz application
score = 0

print("Welcome to Python Quiz")
print("Q1. Which keyword is used to define a function in Python?")
print("a) func  b) def  c) function")
ans1 = input("Your answer: ")
if ans1 == 'b' or ans1 == 'B':
    print("Correct")
    score = score + 1
else:
    print("Wrong. Correct answer is b")

print("\nQ2. What is the output of 3 ** 2?")
print("a) 6  b) 9  c) 8")
ans2 = input("Your answer: ")
if ans2 == 'b' or ans2 == 'B':
    print("Correct")
    score = score + 1
else:
    print("Wrong. Correct answer is b")

print("\nQ3. Which data type is mutable?")
print("a) tuple  b) string  c) list")
ans3 = input("Your answer: ")
if ans3 == 'c' or ans3 == 'C':
    print("Correct")
    score = score + 1
else:
    print("Wrong. Correct answer is c")

print("\nQuiz Over!")
print("Your total score:", score, "/ 3")