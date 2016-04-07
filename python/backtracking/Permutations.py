"""
 Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].


"""


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):

        n = len(nums)
        result = []
        used = [False] * n

        def backtracking(curr, d):
            if d == n:
                result.append([_ for _ in curr])
                return
            for i in xrange(n):
                if not used[i]:
                    used[i] = True
                    backtracking(curr + [nums[i]], d + 1)
                    used[i] = False

        backtracking([], 0)
        return result


print Solution().permute([1,2,3])


