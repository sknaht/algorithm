"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
"""

class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        r = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    r += 1
                    self.mark(grid, i, j)
        return r

    def mark(self, g, x, y):
        g[x][y] = 0
        for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if x + i < len(g) and y + j < len(g[0]) and x + i >= 0 and y + j >= 0:
                 if g[x+i][y+j] == 1:
                     self.mark(g, x+i, y+j)

t = Solution()
print t.numIslands([[1, 0, 1, 1]])