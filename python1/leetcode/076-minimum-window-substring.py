class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        d = {}
        for c in t:
            if c not in d:
                d[c] = 0
            d[c] += 1
        current = {c: 0 for c in d}
        start, end, num = 0, 0, 0
        ans = ''
        while end < len(s):
            if s[end] in t:
                current[s[end]] += 1
                if current[s[end]] <= d[s[end]]:
                    num += 1
            while num >= len(t) and start <= end:
                if not ans or end - start < len(ans):
                    ans = s[start: end + 1]
                if s[start] in t:
                    current[s[start]] -= 1
                    if current[s[start]] < d[s[start]]:
                        num -= 1
                start += 1
            end += 1
        return ans

print Solution().minWindow('ab', 'b')