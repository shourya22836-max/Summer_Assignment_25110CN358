# Write a program to Find nth Fibonacci term. 

def fiboRecur(n):
    if n == 0:
        return 0
    elif( n == 1):
        return 1
    else:
        return fiboRecur(n - 1) + fiboRecur(n -  2)
    
if __name__ == "__main__":
    num = int(input("enter any number"))
    print(f"using recursions value of fib {num} is {fiboRecur(num)}")
