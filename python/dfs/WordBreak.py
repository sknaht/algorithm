class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):

        f = [False]*len(s)

        for i in range(len(s)):
            if s[:i+1] in dict:
                f[i] = True
                continue
            for j in range(i):
                if f[j] and (s[j+1:i+1] in dict):
                    f[i] = True
                    break
        return f[len(s)-1]
