class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        n1, n2 = len(word1), len(word2)
        result = [
            [
                n1 + n2 for i in xrange(n2 + 1)
            ] for j in xrange(n1 + 1)
        ]
        for i in xrange(n2):
            result[0][i] = i
        for i in xrange(n1):
            result[i][0] = i

        for i in xrange(1, n1 + 1):
            curr = word1[i - 1]
            for j in xrange(1, n2 + 1):
                if curr == word2[j - 1]:
                    result[i][j] = min(result[i][j], result[i - 1][j - 1])
                else:
                    result[i][j] = min(
                        result[i][j],
                        result[i - 1][j] + 1,   # delete word1[i]
                        result[i][j - 1] + 1,   # add word2[j]
                        result[i - 1][j - 1] + 1    # exchange
                    )
        return result[n1][n2]

