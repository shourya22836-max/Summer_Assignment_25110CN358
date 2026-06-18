# Write a program to Find sum and average of array.

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    element = input("Enter element: ")
    arr.append(element)

print("Array elements are:")
for item in arr:
    print(item)

total = sum(arr)

average = total / n

print("Sum of array elements =", total)
print("Average of array elements =", average)
