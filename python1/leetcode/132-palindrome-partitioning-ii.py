class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        cut = [len(s) - 1 for i in xrange(len(s))]
        pal = [[False for i in xrange(len(s))] for j in xrange(len(s))]
        for i in xrange(len(s)):
            pal[i][i] = True
            j, k = i - 1, i + 1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    pal[j][k] = True
                    j, k = j - 1, k + 1
                else:
                    break
            j, k = i - 1, i
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    pal[j][k] = True
                    j, k = j - 1, k + 1
                else:
                    break
        for i in xrange(len(s)):
            if pal[0][i]:
                cut[i] = 0

        for i in xrange(1, len(s)):
            if cut[i] > 0:
                for j in xrange(1, i + 1):
                    if pal[j][i] and cut[j - 1] < cut[i]:
                        cut[i] = cut[j - 1] + 1

        return cut[len(s) - 1]

print Solution().minCut('aa')
