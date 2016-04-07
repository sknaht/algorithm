class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        r = ''
        while n > 0:
            carry = False
            t = n % 26
            if t == 0:
                carry = True
                t = 26
            n = n / 26
            if carry:
                n -= 1
            r = chr(ord('A') + t - 1) + r

        return r

print Solution().convertToTitle(53)