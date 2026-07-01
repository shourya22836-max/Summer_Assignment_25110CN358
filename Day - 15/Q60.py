# Write a program to Move zeroes to end. 

n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements: ").split()))

result = []

for num in arr:
    if num != 0:
        result.append(num)

zero_count = n - len(result)

for i in range(zero_count):
    result.append(0)

print("Array after moving zeroes to the end:")
print(result)