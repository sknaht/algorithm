"""
 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):

        if not nums:
            return 0
        p1, p2, n = 0, 0, len(nums)
        while p2 < n:
            p3 = p2
            p2 += 1
            while p2 < n and nums[p2] == nums[p3]:
                p2 += 1
            for i in xrange(min(2, p2 - p3)):
                nums[p1] = nums[p3]
                p1 += 1
        return p1


print Solution().removeDuplicates([1,1,1, 1, 2,2, 3, 4, 4,4])

