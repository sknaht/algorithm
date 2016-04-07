class Solution:
    # @param word1, a string
    # @param word2, a string
    # @return an integer
    def minDistance(self, word1, word2):

        n1, n2 = len(word1), len(word2)
        result = [[n1 + n2 for i in xrange(n2 + 1)] for _ in xrange(n1 + 1)]
        for i in xrange(n2 + 1):
            result[0][i] = i
        for i in xrange(n1 + 1):
            result[i][0] = i

        for i in xrange(1, n1 + 1):
            curr = word1[i - 1]
            for j in xrange(1, n2 + 1):

                if curr == word2[j - 1]:
                    result[i][j] = min(result[i][j], result[i-1][j-1])
                else:
                    # result[i-1][j] + 1  : delete current char
                    # result[i][j-1] + 1  : add word2[j - 1] char
                    # result[i][j] + 1    : replace current char
                    result[i][j] = min(result[i][j], result[i-1][j] + 1, result[i][j-1] + 1, result[i-1][j-1] + 1)

        return result[n1][n2]

t = Solution()

print t.minDistance('a', 'aaa')
