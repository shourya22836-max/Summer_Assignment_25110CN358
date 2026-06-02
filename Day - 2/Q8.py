# Write a program to Check whether a number is palindrome.

num = input("Enter a number: ")
reversed_num =  num[::-1]

if(num == reversed_num):
    print("palindrome number")

else:
    print("not a palindrome number")
