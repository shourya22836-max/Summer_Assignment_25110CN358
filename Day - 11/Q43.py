# Write a program to Write function to check prime.

# num = int(input("enter any number: "))

# def prime_num():
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "not prime number")
#             break
#         else:
#             print(num, "prime number")

# prime_num()

num = int(input("Enter any number: "))

def prime_num():
    for i in range(2, num):
        if num % i == 0:
            print(num, "not prime number")
            break
    else:
        print(num, "prime number")

prime_num()
