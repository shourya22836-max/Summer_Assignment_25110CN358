# Write a program to Check Armstrong number. 

def armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(d) ** power for d in digits)
num = int(input("enter a number: "))
if armstrong(num):
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")

