# coding=utf-8
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        ans = []
        nums.sort()

        def find(x, begin, end):
            while begin < end:
                m = (begin + end) / 2
                if nums[m] == x:
                    return m
                if nums[m] > x:
                    end = m - 1
                else:
                    begin = m + 1
            if x == nums[begin]:
                return begin
            return -1

        lasta, lastb = None, None
        for i in xrange(len(nums) - 2):
            if lasta != None and lasta == nums[i]:
                continue
            else:
                lasta = nums[i]
            for j in xrange(i + 2, len(nums)):
                if lastb != None and lastb == nums[j]:
                    continue
                else:
                    lastb = nums[j]
                t = find(0 - nums[i] - nums[j], i + 1, j - 1)
                if t > 0:
                    ans.append([nums[i], nums[t], nums[j]])
        return ans

print Solution().threeSum([0, 0, 0, 0])


