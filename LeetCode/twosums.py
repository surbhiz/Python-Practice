nums = [2, 11, 7, 15]


def twoSum(nums, target):
    for i in range(len(nums)):
        a = target-nums[i]
        print(a)
        print(nums.index(a))
        if a in nums and i != nums.index(a):
            return print([i, nums.index(a)])


twoSum(nums, 17)
