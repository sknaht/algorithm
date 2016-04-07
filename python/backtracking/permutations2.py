"""
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):

        count = {x:0 for x in nums}
        for x in nums:
            count[x] += 1
        n = len(nums)
        result = []

        def backtracking(curr, d):
            if d >= n:
                result.append([x for x in curr])
                return
            for x in count:
                if count[x] > 0:
                    count[x] -= 1
                    backtracking(curr + [x], d+1)
                    count[x] += 1

        backtracking([], 0)
        return result

print Solution().permuteUnique([1,1,1,2])

