# Write a program to Recursive reverse number. 

def reverse(n):
    if n < 10:  # Base case
        return str(n)
    return str(n % 10) + reverse(n // 10)

# Input from user
num = int(input("Enter a number: "))

print("Reversed number =", reverse(num))