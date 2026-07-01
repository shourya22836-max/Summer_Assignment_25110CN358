# Write a program to Reverse array. 

n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

arr.reverse()

print("Reversed array:")
print(arr)