# Write a program to Find x^n without pow(). 

# Find x^n without using pow()

x = int(input("Enter base (x): "))
n = int(input("Enter exponent (n): "))

result = 1

for i in range(n):
    result *= x

print("Result:", result)