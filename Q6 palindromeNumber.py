# Write a Program to enter the string and to check if it’s palindrome or not using loop.

string = input("string: ")
if string == string[::-1]:
    print("is a Palindrome")
else:
    print("not a Palindrome")