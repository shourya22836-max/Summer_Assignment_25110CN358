# Write a program to Second largest element. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Array elements are:")
for item in arr:
    print(item)

arr.sort()

print("Second largest element is:", arr[-2])
