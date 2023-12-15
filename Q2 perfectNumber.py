# Write a program to find whether an inputted number is perfect or not.

num = int(input("num: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("not a Perfect Number")