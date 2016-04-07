"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):

        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i, n in enumerate(nums):
            if n - 1 != i:
                return i + 1
        return len(nums) + 1


if __name__ == "__main__":
    print Solution().firstMissingPositive([4,7,4,4, 1, 9])
    print Solution().firstMissingPositive([3,4,-1,1])
