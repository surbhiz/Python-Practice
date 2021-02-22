class Solution(object):
    def singleNumber(self, nums):
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
            else:
                result.remove(i)
        return result.pop()


nums = [1, 2, 2, 1, 3]
print(Solution.singleNumber([], nums))
