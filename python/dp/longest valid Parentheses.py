class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):

        p = [-1] * len(s)

        for i in xrange(1, len(s)):
            if s[i] == ')':
                if s[i -1] == '(':
                    if i > 1 and p[i - 2] != -1:
                        p[i] = p[i - 2]
                    else:
                        p[i] = i - 1
                else:
                    if p[i - 1] > 0 and s[p[i - 1] - 1] == "(":
                        p[i] = p[i - 1] - 1
                        if p[i - 1] > 1 and p[p[i - 1] - 2] != -1:
                            p[i] = p[p[i - 1] - 2]

        r = 0
        for i in xrange(1, len(s)):
            if p[i] > -1 and i - p[i] + 1 > r:
                r = i - p[i] + 1
        return r

print Solution().longestValidParentheses('(()))())(')

