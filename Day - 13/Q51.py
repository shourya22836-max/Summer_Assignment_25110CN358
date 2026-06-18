# Write a program to Find largest and smallest element.

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    element = input("Enter element: ")
    arr.append(element)

print("Array elements are:")
for item in arr:
    print(item)

print(arr)

maximum = max(arr)
minimum = min(arr)

print("min of array elements =", minimum)
print("max of array elements =", maximum)
