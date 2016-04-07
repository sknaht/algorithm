"""
 Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):

        result = [[]]
        nums.sort()
        p1, p2, n = 0, 0, len(nums)
        while p2 < n:
            while p2 < n and nums[p2] == nums[p1]:
                p2 += 1
            t = p2 - p1
            curr = []
            for i in xrange(t + 1):
                for s in result:
                    curr.append(s + [nums[p1]] * i)
            result = curr
            p1 = p2
        return result

Solution().subsetsWithDup([1,2,2])

