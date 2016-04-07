class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        p = {0: 1}
        p[1] = x

        i = 2
        while i <= abs(n):
            p[i] = p[i / 2] * p[i/2]
            i *= 2

        def pow(n):
            if n in p:
                return p[n]
            else:
                t = pow(n/2) * pow(n/2) * p[n % 2]
                p[n] = t
                return t

        if n < 0:
            return 1 / pow(-n)
        else:
            return pow(n)

print Solution().myPow(8.66731, 3)