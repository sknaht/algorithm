# coding=utf-8
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):

        match = [[False for i in xrange(len(s) + 1)] for j in xrange(len(p) + 1)]
        match[0][0] = True

        for i in xrange(1, len(p) + 1):

            cp = p[i - 1]

            if cp == '.':
                for j in xrange(1, len(s) + 1):
                    match[i][j] = match[i - 1][j - 1]

            elif i > 1 and cp == '*':
                if p[i - 2] == '.':
                    for j in xrange(0, len(s) + 1):
                        if match[i - 2][j]:
                            k = j
                            while k <= len(s):
                                match[i][k] = True
                                k += 1
                            break
                else:
                    for j in xrange(0, len(s) + 1):
                        if match[i - 2][j]:
                            match[i][j] = True
                            for k in xrange(j + 1, len(s) + 1):
                                if s[k - 1] != p[i - 2]:
                                    break
                                match[i][k] = True
                                k += 1

            else:
                for j in xrange(1, len(s) + 1):
                    if cp == s[j - 1] and match[i - 1][j - 1]:
                        match[i][j] = True

        return match[len(p)][len(s)]


print Solution().isMatch("", ".*")

