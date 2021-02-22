class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    result.append(i)
        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 1]
print(Solution.intersect([], nums1, nums2))
