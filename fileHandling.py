# f = open("InputData.txt","r")
# print(list(f))
# f.close()

# f = open("InputData.txt", "r")
# for line in f:
#     print(line)
# f.close()

# f = open("InputData.txt", "r")
# for line in f:
#     print(line, end='')
# f.close()

f = open("InputData.txt", "r")
for line in f:
    print(line[::-1], end='')
f.close()