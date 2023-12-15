# data1, data2 = [], []
# for _ in range(int(input())):
#     temp = input().split()
#     data1.append(int(temp[1]))
#     data2.append(temp[0])
#     mydict = dict(zip(data1, data2))

# print(mydict[max(data1)])
# print(mydict[min(data1)])

# data1, data2 = [], []
# for _ in range(int(input())):
#     temp = input().split()
#     data1.append(temp[0])
#     data2.append(int(temp[1]))

# for i in data2:
#     if i != max(data2):
#         data1.pop(data2.index(i))

# print(data1)

data1, data2 = [], []
n = int(input())
for _ in range(n):
    temp = input().split()
    data1.append(temp[0])
    data2.append(int(temp[1]))
mydict = dict(zip(data1, data2))
mydict = dict(sorted(mydict.items(), key = lambda x: x[1], reverse=True))
req = []
for key, value in mydict.items():
    if value == max(mydict.values()):
        req.append(key)
print(req)