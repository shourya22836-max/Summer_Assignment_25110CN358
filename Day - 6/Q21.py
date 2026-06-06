# Write a program to Convert decimal to binary.

decimal = int(input("Enter a decimal number: "))

binary = ""

if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

print("Binary equivalent:", binary)
