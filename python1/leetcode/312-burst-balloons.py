class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        n = len(nums)

        a = {i: nums[i] for i in xrange(n)}
        a[-1] = 1
        a[n] = 1

        F = [
            [0 for i in xrange(n + 1)]
            for j in xrange(n + 1)
        ]

        for i in xrange(n):
            F[i][i] = a[i - 1] * a[i] * a[i + 1]

        for k in xrange(2, n + 1):
            for i in xrange(n - k + 1):
                j = i + k - 1
                x = a[i - 1] * a[j + 1]

                for t in xrange(i, j + 1):
                    y = a[t] * x + F[i][t - 1] + F[t + 1][j]
                    F[i][j] = max(F[i][j], y)

        return F[0][n - 1]





print Solution().maxCoins([9,76,64,21,97])