class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n, m = len(board), len(board[0])

        circum = []
        if board:
            circum += [(0, i) for i in xrange(m)]
            circum += [(n - 1, i) for i in xrange(m)]
            circum += [(i, 0) for i in xrange(1, n - 1)]
            circum += [(i, m - 1) for i in xrange(1, n - 1)]

        for (x, y) in circum:
            if board[x][y] == 'O':
                curr = [(x, y)]
                board[x][y] = '.'
                while curr:
                    next = []
                    for (xx, yy) in curr:
                        for (dx, dy) in d:
                            if 0 <= dx + xx < n and 0 <= dy + yy < m:
                                if board[dx + xx][dy + yy] == 'O':
                                    board[dx + xx][dy + yy] = '.'
                                    next.append((dx + xx, dy + yy))
                    curr = next

        for x in xrange(n):
            for y in xrange(m):
                board[x][y] = 'O' if board[x][y] == '.' else 'X'


a = ["XOOOOOOOOOOOOOOOOOOO","OXOOOOXOOOOOOOOOOOXX","OOOOOOOOXOOOOOOOOOOX","OOXOOOOOOOOOOOOOOOXO","OOOOOXOOOOXOOOOOXOOX","XOOOXOOOOOXOXOXOXOXO","OOOOXOOXOOOOOXOOXOOO","XOOOXXXOXOOOOXXOXOOO","OOOOOXXXXOOOOXOOXOOO","XOOOOXOOOOOOXXOOXOOX","OOOOOOOOOOXOOXOOOXOX","OOOOXOXOOXXOOOOOXOOO","XXOOOOOXOOOOOOOOOOOO","OXOXOOOXOXOOOXOXOXOO","OOXOOOOOOOXOOOOOXOXO","XXOOOOOOOOXOXXOOOXOO","OOXOOOOOOOXOOXOXOXOO","OOOXOOOOOXXXOOXOOOXO","OOOOOOOOOOOOOOOOOOOO","XOOOOXOOOXXOOXOXOXOO"]
board = [list(x) for x in a]
Solution().solve(board)
for i in xrange(len(board)):
    print ''.join(board[i])