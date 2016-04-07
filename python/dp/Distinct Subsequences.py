"""
 Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):

        if len(t) > len(s):
            return 0

        result = [[0] * len(s) for _ in xrange(len(t))]
        for i in xrange(len(s)):
            if s[i] == t[0]:
                result[0][i] = 1

        for i in xrange(1, len(t)):
            tmp = 0
            for j in xrange(len(s)):
                if tmp > 0 and s[j] == t[i]:
                    result[i][j] = tmp
                tmp += result[i-1][j]
        r = 0
        for i in xrange(len(s)):
            r += result[len(t) - 1][i]
        return r

print Solution().numDistinct('rabbbit', 'rabbit')

