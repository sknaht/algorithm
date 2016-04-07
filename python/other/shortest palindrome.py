class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):

        l = s + '#' + s[::-1]
        p = [0] * len(l)

        for i in xrange(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            if l[i] == l[j]:
                p[i] = j + 1
            else:
                p[i] = j
        return s[::-1][:len(s) - p[-1]] + s

print Solution().shortestPalindrome("abababc" )