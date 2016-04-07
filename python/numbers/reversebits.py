class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0
        c = 0
        while n>0:
            t = n%2
            n = n/2
            r = r*2 + t
            c += 1
            for i in xrange(32-c):
                r*=2
                return r
