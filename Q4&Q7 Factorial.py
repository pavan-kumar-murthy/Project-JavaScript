# Write a Program to find factorial of the entered number.

# Traditional Method
# num = int(input("num: "))
# product = 1
# i = 1
# while i <= num:
#     product *= i
#     i += 1

# print("Factorial:", product)

# Recursion Method
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("num: "))
print("factorial:", factorial(n))