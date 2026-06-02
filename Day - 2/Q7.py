# Write a program to Find product of digits. 

num = int(input("enter a number: "))

sum_digits = 1

num = abs(num)

while num > 0:
    digit = num % 10 
    sum_digits *= digit
    num //= 10 

print("sum of digits =", sum_digits)