class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):

        if not dungeon: return 0

        n = len(dungeon)
        m = len(dungeon[0])
        minhp = [[0 for i in range(m)] for i in range(n)]

        minhp[n-1][m-1] = 0 - min(0, dungeon[n-1][m-1])
        for i in xrange(m-1, 0, -1):
            minhp[n-1][i-1] = max(0, minhp[n-1][i] - dungeon[n-1][i-1])
        for i in xrange(n-1, 0, -1):
            minhp[i-1][m-1] = max(0, minhp[i][m-1] - dungeon[i-1][m-1])

        for i in xrange(n-2, -1, -1):
            for j in xrange(m-2, -1, -1):
                minhp[i][j] = max(min(minhp[i][j+1], minhp[i+1][j]) - dungeon[i][j], 0)

        return minhp[0][0] + 1
