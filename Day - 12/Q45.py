# Write a program to Write function for palindrome.

def is_palindrome(s):
    return s == s[::-1]

text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")