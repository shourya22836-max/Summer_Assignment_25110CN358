# Write a program to Print reverse pyramid.
# *********
#  *******
#   *****
#    ***
#     *

num = int(input("Enter number of rows: "))

for i in range(num):
    for j in range(i):
        print(" ", end="")
    
    for k in range(2 * (num - i) - 1):
        print("*", end="")
    
    print()
