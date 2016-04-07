# coding=utf-8
"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):

        weight = [1]
        for i in xrange(1, n):
            weight.append(i * weight[i-1])
        weight.reverse()
        ans = []
        k -= 1
        for i in xrange(n):
            ans.append(k / weight[i])
            k = k % weight[i]
        used = [False] * n
        r = ''
        for i in xrange(n):
            t = ans[i]
            for i in xrange(n):
                if not used[i]:
                    if t == 0:
                        break
                    t -= 1
            used[i] = True
            r += chr(ord('1') + i)
        return r

print Solution().getPermutation(4,11)