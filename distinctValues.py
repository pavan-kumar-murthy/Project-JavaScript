a = [int(input()) for _ in range(int(input()))]
x = list()
for num in a:
    if num not in x:
        x.append(num)
print(x)
