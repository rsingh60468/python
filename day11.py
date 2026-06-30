nums = [2, 2, 4, 3, 4, 8, 16, 2]
dupe = {}
for el in nums:
    dupe[el] = nums.count(el)
print(dupe)