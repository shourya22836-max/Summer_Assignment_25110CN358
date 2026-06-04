# Write a program to Print Armstrong numbers in a range.

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Armstrong numbers in the range are:")

for num in range(start, end + 1):
    n = len(str(num))
    total = sum(int(digit) ** n for digit in str(num))

    if total == num:
        print(num, end=" ")