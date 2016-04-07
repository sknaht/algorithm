# coding=utf-8
"""
 Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):

        i, j, t, r = 0, 0, 0, 0
        while j < len(nums):
            while t < s and j < len(nums):
                t += nums[j]
                j += 1
            while t >= s:
                t -= nums[i]
                if not r or j - i < r:
                    r = j - i
                i += 1
        return r


print Solution().minSubArrayLen(7, [2,3,2,4,3])

