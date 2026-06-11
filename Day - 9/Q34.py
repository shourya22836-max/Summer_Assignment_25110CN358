# Write a program to Print reverse number
# triangle.
# 12345
# 1234
# 123
# 12
# 1

num = int(input("Enter any number: "))

for i in range(num, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    