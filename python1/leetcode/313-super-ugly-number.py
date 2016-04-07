class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        result = []
        k = len(primes)
        f = [1] * k
        count = [0] * k

        for i in xrange(n):
            next = min(f)
            result.append(next)
            for j in xrange(k):
                if f[j] == next:
                    f[j] = primes[j] * result[count[j]]
                    count[j] += 1
        return result[-1]

print Solution().nthSuperUglyNumber(12,
[2, 7, 13, 19])
