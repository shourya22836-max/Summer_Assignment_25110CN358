# Write a program to Write function to find factorial.

num = int(input("Enter any number: "))

def factorial(a):
    fact = 1

    for i in range(1, a + 1):
        fact *= i

    return fact

result = factorial(num)
print("Factorial:", result)
