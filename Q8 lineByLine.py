# Read a file line by line and print it.

# with open("InputData.txt", 'r') as fin:
#     for i in fin.readlines():
#         print(i)

a = open("InputData.txt", 'r')
c = a.readlines()
for i in c:
    print(i)