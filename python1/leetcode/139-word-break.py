class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        a = [True] + [False for i in xrange(len(s))]
        m = max([len(w) for w in wordDict] + [0])
        for i in xrange(len(s)):
            if a[i]:
                for j in xrange(1, m + 1):
                    if s[i: i + j] in wordDict and i + j <= len(s):
                        a[i + j] = True
        return a[len(s)]

print Solution().wordBreak('ab', ['a', 'b'])