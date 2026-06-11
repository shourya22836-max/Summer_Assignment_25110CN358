# Write a program to Print repeated character
# pattern.
# A
# BB
# CCC
# DDDD
# EEEEE

num = int(input("enter any number "))

for i in range(1, num + 1):
    for j in range(i):
        print(chr(64 + i), end="")
    print()
                 
