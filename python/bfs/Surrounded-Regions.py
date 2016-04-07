"""
 Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

"""

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        curr, m, n = [], len(board), len(board[0])
        visited = [[False for j in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            if board[i][0] == 'O':
                curr.append((i, 0))
            if n > 1 and board[i][n-1] == 'O':
                curr.append((i, n-1))
        for j in xrange(n):
            if board[0][j] == 'O':
                curr.append((0, j))
            if m > 1 and board[m-1][j] == 'O':
                curr.append((m-1, j))
        while curr:
            for (x, y) in curr:
                visited[x][y] = True
            next = []
            for (x, y) in curr:
                for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    tx, ty = x + dx, y + dy
                    if 0 <= tx < m and 0 <= ty < n and board[tx][ty] == 'O' and not visited[tx][ty]:
                        next.append((tx, ty))
            curr = next
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j]:
                    board[i][j] = 'X'


a = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
]
a = [['O', 'O'], ['O', 'O']]
Solution().solve(a)
print a