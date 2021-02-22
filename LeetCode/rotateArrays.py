class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        result = []
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
        return nums


nums = [1, 2, 3, 4]
k = 1
print(Solution.rotate([], nums, k))
