# coding=utf-8
"""
 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
"""

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):

        result = []
        cands = {}
        for x in candidates:
            if x not in cands:
                cands[x] = 1
            else:
                cands[x] += 1
        indvs = sorted(cands.keys())

        def backtracking(curr, s):
            if s == 0:
                result.append([_ for _ in curr])
                return
            for x in indvs:
                if x <= s and cands[x] > 0 and (not curr or x >= curr[-1]):
                    cands[x] -= 1
                    backtracking(curr + [x], s - x)
                    cands[x] += 1

        backtracking([], target)
        return result

print Solution().combinationSum2([10,1,2,7,6,1,5], 8)

