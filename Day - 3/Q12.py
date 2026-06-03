# Write a program to Find LCM of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a,b = num1, num2

while b:
    a,b = b, a%b

gcd = a 
lcm = (num1 * num2) // gcd 

print(lcm)



# git add "Day - 3"
# git commit -m "Add Day 1 files"
# git push origin main
