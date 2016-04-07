class Solution:
    # @param s, a string
    # @return a string
    def longestPalindrome(self, s):

        if not s:
            return ''

        r = [[False] * len(s) for i in xrange(len(s) + 1)]

        for j in xrange(len(s)):
            r[0][j] = True
            r[1][j] = True

        c = 0
        ans = r[0]
        for i in xrange(2, len(s) + 1):
            for j in xrange(len(s) - i + 1):
                if s[j] == s[j + i - 1] and r[i - 2][j + 1]:
                    r[i][j] = True
                    ans = s[j: j + i]
                    c += 1

        return ans, c


print Solution().longestPalindrome('aaaaaaaaaaaaaaaaa')

