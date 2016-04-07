"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):

        if not matrix:
            return 0

        curr = [0 for _ in xrange(len(matrix[0]))]
        result = 0

        for m in matrix:
            for i in xrange(len(m)):
                if m[i] == 0:
                    curr[i] = 0
                else:
                    curr[i] += 1

            increasing = []
            i = 0
            tmp = 0
            while i < len(m) + 1:
                if not increasing or (i < len(m) and curr[i] > curr[increasing[-1]]):
                    increasing.append(i)
                    i += 1
                else:
                    last = increasing.pop()
                    if not increasing:
                        tmp = max(tmp, curr[last] * i)
                    else:
                        tmp = max(tmp, curr[last] * (i - increasing[-1] - 1))

            if tmp > result:
                result = tmp

        return result


m = [
    [1,1,0,1],
    [1,1,0,1],
    [1,1,1,1]
]
print Solution().maximalRectangle(m)


