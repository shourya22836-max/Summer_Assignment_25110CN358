# Write a program to Write function for Armstrong.

def is_armstrong(num):
    digits = str(num)
    power = len(digits)

    total = 0
    for digit in digits:
        total += int(digit) ** power

    return total == num

number = int(input("Enter a number: "))

if is_armstrong(number):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")