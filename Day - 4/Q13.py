# Write a program to Generate Fibonacci series. 

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = 10

for i in range(terms):
    print(fibonacci(i), end=" ") 
    