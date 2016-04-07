class Solution:
    # @param s, a string
    # @return a string
    def longestPalindrome(self, s):

        r, n = '', len(s)

        for i in xrange(n):
            t = 0
            for j in xrange(1, min(i+1, n-i)):
                if s[i-j] == s[i+j]:
                    t += 1
                else:
                    break
            if len(r) < 2*t+1:
                r = s[i-t:i+t+1]

            t = 0
            for j in xrange(1, min(i+1, n-i+1)):
                if s[i-j] == s[i+j-1]:
                    t += 1
                else:
                    break
            if len(r) < 2*t:
                r = s[i-t:i+t]

        return r



t = Solution()
print t.longestPalindrome("ooooooabchhcba")
