def search(x, nums):
    for index in range(len(nums)):
        if nums[index] == x:
            return index
    return -1

print(search(4 ,[1, 5, 7, 13, 10, 4, 10, 11]))
