"""
 Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):

        begin, end, n, length = 0, 0, len(s), len(t)
        minwide, min_begin, min_end = n + 1, 0, 0
        setoft = set(t)
        curr = {c: 0 for c in setoft}
        need = {c: 0 for c in setoft}
        for c in t:
            need[c] += 1
        count = 0
        while begin < n and s[begin] not in t:
            begin += 1
            end += 1
        while end < n:
            x = s[end]
            if x in setoft:
                curr[x] += 1
                if curr[x] <= need[x]:
                    count += 1
                if count == length:
                    if end - begin + 1 < minwide:
                        minwide, min_begin, min_end = end - begin + 1, begin, end
                    flag = False
                    while begin <= end and not flag:
                        cc = s[begin]
                        if cc in curr and curr[cc] >= need[cc]:
                            curr[cc] -= 1
                            if curr[cc] < need[cc]:
                                count -= 1
                                flag = True
                        begin += 1
                        if count == length and end - begin + 1 < minwide:
                            minwide, min_begin, min_end = end - begin + 1, begin, end
            end += 1
        if minwide > n:
            return ''
        print min_end, min_begin
        return s[min_begin: min_end + 1]

print Solution().minWindow('bancbbcaa', 'abc')


