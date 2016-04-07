class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """


        d = [0]

        x = n
        g = 0
        while x > 0:
            g += 1
            x /= 10

        c = 1
        for i in xrange(1, g + 1):
            d.append(d[-1] * 10 + c)
            c *= 10


        result = 0
        i = 0
        p = 1
        while n > 0:
            x = n % 10
            n /= 10
            result += (x - 1) * d[i] + p
            p *= 10
            i += 1

        print d
        print result

Solution().countDigitOne(13)


