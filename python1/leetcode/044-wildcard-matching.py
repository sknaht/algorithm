class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        indexp = 0
        indexs = 0
        lastp = -1
        lasts = -1
        while indexs < len(s):
            if indexp < len(p) and (p[indexp] == s[indexs] or p[indexp] == '?'):
                indexp += 1
                indexs += 1
            elif indexp < len(p) and p[indexp] == '*':
                while indexp < len(p) and p[indexp] == '*':
                    indexp += 1
                if indexp == len(p):
                    return True
                lastp = indexp
                lasts = indexs
            elif lastp >= 0 and lasts >= 0:
                indexp, indexs = lastp, lasts + 1
                lasts += 1
                if lasts >= len(s):
                    return False
            else:
                return False

        while indexp < len(p) and p[indexp] == '*':
            indexp += 1
        return indexp == len(p)

print Solution().isMatch('aa', 'a*a')


