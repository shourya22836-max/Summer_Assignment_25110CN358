# Write a program to Print reverse star pattern.
# *****
# ****
# ***
# **
# *

num = int(input("Enter any number: "))

for i in range(num, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

    