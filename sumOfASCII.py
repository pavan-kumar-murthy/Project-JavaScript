a = input()
ls = [ord(i) for i in a]
if sum(ls) % 2 == 0:
    print("Even")
else:
    print("Odd")