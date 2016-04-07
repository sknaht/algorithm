class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        import math

        curr = {n}
        step = 0
        appeared = set([])
        while curr:
            next = set([])
            step += 1
            for i in curr:
                for j in xrange(int(math.pow(n, 0.5)), 0, -1):
                    candidate = i - j * j
                    if candidate == 0:
                        return step
                    if candidate not in appeared:
                        appeared.add(candidate)
                        next.add(candidate)
            curr = next

print Solution().numSquares(9375)



