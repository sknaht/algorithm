"""
 You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if not words:
            return []

        need, curr = {}, {}
        for w in words:
            curr[w] = 0
            if w not in need:
                need[w] = 1
            else:
                need[w] += 1

        wl = len(words[0])
        ans = []
        for start in xrange(0, len(s) - wl * len(words) + 1):
            for w in curr:
                curr[w] = 0

            valid = True
            for count in xrange(len(words)):
                w = s[start + count * wl: start + (count + 1) * wl]
                if w in words and curr[w] < need[w]:
                    curr[w] += 1
                else:
                    valid = False
                    break
            if valid:
                ans.append(start)

        return ans

t = Solution()
print t.findSubstring("barfoothefoobarman", ["foo", "bar"])