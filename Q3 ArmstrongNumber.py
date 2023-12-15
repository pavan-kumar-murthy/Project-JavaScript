# Write a Program to check if the entered number is Armstrong or not.

num = input("num: ")
sum = 0
for i in num:
    sum += int(i)**(len(num))

if sum == int(num):
    print("armstrong number")
else:
    print("not a armstrong number")