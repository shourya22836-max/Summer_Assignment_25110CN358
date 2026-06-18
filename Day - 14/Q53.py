# Write a program to Linear search. 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [3, 5, 7, 9, 11]
result = linear_search(numbers, 7)

print(result)  
