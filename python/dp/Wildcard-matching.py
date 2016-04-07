# coding=utf-8
"""
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""

class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):


        i, j = 0, 0
        lasti, lastj = 0, -1

        while i < len(s):

            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and (p[j] == '*'):
                lasti = i
                lastj = j
                j += 1
            elif lastj >= 0:
                i = lasti + 1
                lasti = i
                j = lastj + 1
            else:
                return False

        if i < len(s):
            return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)


if __name__ == "__main__":
    t = Solution()
    print t.isMatch('aaaaa', 'a*')


