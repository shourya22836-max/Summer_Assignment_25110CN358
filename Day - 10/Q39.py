# Write a program to Print number pyramid.
#     1
#    121
#   12321
#  1234321
# 123454321

num = int(input("Enter any number: "))

for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()