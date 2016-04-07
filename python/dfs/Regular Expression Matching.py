class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):

        return self.match(s, p, 0, 0)

    def match(self, s, p, i, j):
        if i == len(s) or j == len(p):
            if i != len(s) or j != len(p):
                return False
            return True

        if s[i] == p[j] or p[j] == '.':
            if self.match(s, p, i + 1, j + 1):
                return True

        if j < len(p) - 1 and p[j + 1] == '*':
            # zero
            if self.match(s, p, i, j + 2):
                return True

            # one or more
            for k in xrange(i, len(s)):
                if s[k] != p[j]:
                    break
                if self.match(s, p, k + 1, j + 2):
                    return True

        return False

print Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")


