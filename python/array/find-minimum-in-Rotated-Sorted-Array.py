"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if not nums:
            return 0

        left, right = 0, len(nums) - 1

        while left < right:
            m = (left + right) / 2
            if m == left or m == right:
                return min(nums[left], nums[right])
            if nums[left] < nums[m] < nums[right]:
                right = m
            elif nums[left] < nums[m] > nums[right]:
                left = m
            elif nums[left] > nums[m] < nums[right]:
                right = m
        return nums[left]

print Solution().findMin([3, 1,2])