mylist = [85, 98, 56, 3, 9, 88]
if max(mylist) > 50:
    print(sorted(mylist)[::-1])
elif max(mylist) < 50:
    print(sorted(mylist))
else:
    print(mylist)