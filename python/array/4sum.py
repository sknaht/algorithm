# coding=utf-8
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
    The solution set must not contain duplicate quadruplets.

    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):

        if not nums or target > 4 * max(nums) or target < 4 * min(nums):
            return []

        m = {x: 0 for x in set(nums)}
        for x in nums:
            m[x] += 1
        nums = sorted(m.keys())
        result = []

        def find(curr, d, remain, p):
            if d >= 2:
                i, j = p, len(nums) - 1
                while i <= j:
                    if m[nums[i]] == 0:
                        i += 1
                        continue
                    if m[nums[j]] == 0:
                        j -= 1
                        continue
                    if nums[i] + nums[j] == remain:
                        if i == j and m[nums[i]] < 2:
                            break
                        result.append([_ for _ in curr] + [nums[i], nums[j]])
                        i += 1
                    elif nums[i] + nums[j] < remain:
                        i += 1
                    else:
                        j -= 1
                return
            for i in xrange(p, len(nums)):
                x = nums[i]
                if m[x] > 0:
                    m[x] -= 1
                    find(curr + [x], d + 1, remain - x, i)
                    m[x] += 1

        find([], 0, target, 0)
        return result

print Solution().fourSum([0,0,0,0],0)

