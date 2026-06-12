# Write a program to Print character pyramid. 
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

num = int(input("Enter any number: "))

for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(chr(64 + j), end="")

    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")

    print()