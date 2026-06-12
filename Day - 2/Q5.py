# Write a program to Find sum of digits of a number.

num = int(input("enter a number: "))

sum_digits = 0

num = abs(num)

while num > 0:
    digit = num % 10 
    sum_digits += digit
    num //= 10

print("sum of digits =", sum_digits)