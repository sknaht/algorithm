"""
ind the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):

        neg, pos, r = 1, 1, float('-inf')
        for i in nums:
            neg, pos = min(neg * i, pos * i, i), max(pos * i, neg * i, i)
            r = max(r, pos)

        return r

t = Solution()
print t.maxProduct([2,3,-2,4])