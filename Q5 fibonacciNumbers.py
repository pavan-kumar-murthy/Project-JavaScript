# Write a Program to enter the number of terms and to print the Fibonacci Series.

# Recursion Method
def fibonacci(n):
    if n == 0:
       return 0
    elif n == 1:
       return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2)
    
num = int(input("num: "))
for i in range(num):
    print(fibonacci(i), end=' ')