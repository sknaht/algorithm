class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.

    def solveSudoku(self, board):
        self.solve(board)

    def fill(self, board):
        poss, sure, filled = {}, [], []
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    poss[(i, j)] = set('123456789')
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] != '.':
                    self.mark((i, j, board[i][j]), poss, sure)
        while sure:
            t = sure.pop()
            filled.append(t)
            tmp = poss.pop(t)
            if not tmp:
                return filled, {}
            board[t[0]][t[1]] = tmp.pop()
            self.mark((t[0], t[1], board[t[0]][t[1]]), poss, sure)
        return filled, poss

    def solve(self, board):
        filled, poss = self.fill(board)
        if not poss:
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == '.':
                        for (x, y) in filled: board[x][y] = '.'
                        return False
            return True
        m = None
        for (x, y) in poss:
            if not m or (len(poss[(x,y)])<len(poss[m])):
                m = (x,y)
                if len(poss[m]) == 2: break
        x, y = m
        for t in poss[m]:
            board[x][y] = t
            if self.solve(board):
                return True
            board[x][y] = '.'
        for (x, y) in filled:
            board[x][y] = '.'


    def mark(self, position, poss, sure):
        i, j, t, tmp = (position[0] / 3) * 3, (position[1] / 3) * 3, position[2], []
        for x in xrange(i, i + 3):
            for y in range(j, j + 3):
                tmp.append((x, y))

        for x in xrange(9):
            tmp.append((position[0], x))
            tmp.append((x, position[1]))

        for (x, y) in tmp:
            if (x, y) in poss:
                poss[(x, y)] = poss[(x, y)].difference({t})
                if len(poss[(x, y)]) == 1 and (x, y) not in sure:
                    sure.append((x, y))


if __name__ == "__main__":
    tmp =  [".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]

    board = []
    for s in tmp:
        t = []
        for c in s:
            t.append(c)
        board.append(t)

    import time
    tttt = time.time()
    print Solution().solveSudoku(board)
    for s in board:
        print ''.join(s)
    print time.time() -tttt