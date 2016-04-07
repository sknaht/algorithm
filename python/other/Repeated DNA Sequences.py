class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10 :
            return []
        t = 0
        f = { 'A': 0, 'C': 1, 'G': 2, 'T': 3}
        x = 1
        for i in xrange(10):
            t += f[s[i]] * x
            x = x * 4
        x = x / 4
        r = {t: 0}
        ans = []
        for i in xrange(10, len(s)):
            t = t / 4
            t += f[s[i]] * x
            if t in r:
                if r[t] != -1:
                    ans.append(s[r[t]:r[t]+10])
                    r[t] = -1
            else:
                r[t] = i - 9

        return ans


t = Solution()
print t.findRepeatedDnaSequences("GAGAGAGAGAGAG")