class Solution:
    def containDuplicates(self, nums):
        result = []
        for i in nums:
            if i not in result:
                print(i)
                result.append(i)
        print((result))


nums = [1, 2, 3, 1, 4, 5]
print(Solution.containDuplicates([], nums))
