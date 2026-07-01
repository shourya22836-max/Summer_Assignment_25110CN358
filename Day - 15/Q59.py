# Write a program to Rotate array right. 

n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements: ").split()))

last = arr[n - 1]
for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]
arr[0] = last

print("Array after right rotation:")
print(arr)