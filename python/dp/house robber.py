class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        n = len(nums)

        if n < 3:
            r = 0
            for x in nums:
                if x > r:
                    r = x
            return r


        result = [0] * n
        result[0], result[1], result[2] = nums[0], nums[1], nums[2] + nums[0]
        for i in xrange(3, n):
            result[i] = max(nums[i] + result[i - 2], nums[i] + result[i - 3])

        r = 0
        for i in xrange(n - 3, n):
            if result[i] > r: r = result[i]
        print result
        return r

print Solution().rob([2,7,9,3,1])