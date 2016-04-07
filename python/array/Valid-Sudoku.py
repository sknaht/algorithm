"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):

        for i in xrange(9):
            for j in xrange(9):
                if not self.check(i, j, board):
                    return False
        return True

    def check(self, i, j, board):
        if board[i][j] == '.': return True
        t, board[i][j] = board[i][j], '.'
        for x in xrange(9):
            if board[x][j] == t or board[i][x] == t:
                return False
        for x in xrange((i/3)*3, (i/3)*3+3):
            for y in xrange((j/3)*3, (j/3)*3 + 3):
                if board[x][y] == t:
                    return False
        board[i][j] = t
        return True