# Write a program to Recursive sum of digits.

def sum_of_digits(n):
    if n == 0:  # Base case
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

# Input from user
num = int(input("Enter a number: "))

print("Sum of digits =", sum_of_digits(abs(num)))