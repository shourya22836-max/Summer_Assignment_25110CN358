# Write a program to Write function for perfect number.

def is_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    return total == num

number = int(input("Enter a number: "))

if is_perfect(number):
    print("Perfect Number")
else:
    print("Not a Perfect Number")