# Write a program to Find largest prime factor.

num = int(input("enter any number "))

def prime_fact(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print("factors are ",i)

prime_fact(num)
    