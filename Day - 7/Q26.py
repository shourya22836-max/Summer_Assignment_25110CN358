# Write a program to Recursive Fibonacci. 

def fibonacci(n):
    if n <= 1:  # Base cases
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input from user
terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")