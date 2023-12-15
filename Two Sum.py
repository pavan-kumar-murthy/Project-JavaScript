nums = list(map(int, input("nums = ").lstrip('[').rstrip(']').split(',')))
target = int(input("target = "))
required = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            if nums[i] + nums[j] == target:
                required.append(i)
                required.append(j)
                break

print(sorted(list(set(required))))