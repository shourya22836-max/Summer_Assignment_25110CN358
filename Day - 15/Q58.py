# Write a program to Rotate array left. 

n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements: ").split()))

first = arr[0]
for i in range(n - 1):
    arr[i] = arr[i + 1]
arr[n - 1] = first

print("Array after left rotation:")
print(arr)