class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        start, end, result, n = 0, 1, 1, len(s)
        curr = [s[0]]
        while end < n:
            if s[end] in curr:
                while start < end:
                    curr.remove(s[start])
                    start += 1
                    if s[start-1] == s[end]: break
            while end < n and s[end] not in curr:
                curr.append(s[end])
                end += 1
            result = max(result, end - start)
        return result

t = Solution()
print t.lengthOfLongestSubstring('aaaabbbfeef')