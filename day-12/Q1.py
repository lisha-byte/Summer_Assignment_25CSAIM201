# Function to check palindrome
def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

num = input("Enter number or word: ")

if is_palindrome(num):
    print(num, "is Palindrome")
else:
    print(num, "is Not Palindrome")