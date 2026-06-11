# Function to print Fibonacci
def fibonacci(n):
    a = 0
    b = 1
    print("Fibonacci series:")
    
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

terms = int(input("Enter number of terms: "))
fibonacci(terms)