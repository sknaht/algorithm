"""
 Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):

        if sorted(s1 + s2) != sorted(s3):
            return False

        l1, l2, l3 = len(s1), len(s2), len(s3)

        result = [[False for i in xrange(l2 + 1)] for j in xrange(l1 + 1)]

        result[0][0] = True
        for i in xrange(1, l1 + 1):
            if result[i-1][0] and s1[i-1] == s3[i-1]:
                result[i][0] = True
            else:
                break
        for j in xrange(1, l2 + 1):
            if result[0][j-1] and s2[j-1] == s3[j-1]:
                result[0][j] = True
            else:
                break
        for i in xrange(1, l1 + 1):
            for j in xrange(1, l2 + 1):
                if result[i][j-1] and s2[j-1]==s3[i+j-1] or result[i-1][j] and s1[i-1]== s3[i+j-1]:
                    result[i][j] = True
        return result[l1][l2]



print Solution().isInterleave("baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab", "aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb", "babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab")
