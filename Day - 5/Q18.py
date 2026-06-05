# Write a program to Check strong number. 

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))

original_num = num
sum_factorials = 0

while num > 0:
    digit = num % 10
    sum_factorials += factorial(digit)
    num //= 10

if sum_factorials == original_num:
    print(original_num, "is a Strong Number")
else:
    print(original_num, "is not a Strong Number")
