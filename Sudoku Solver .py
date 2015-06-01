#!/usr/bin/python

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        self.internalSolveSudoku(board)
        return board

    def internalSolveSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for x in '123456789':
                        board[i] = board[i][:j] + x + board[i][j + 1:]
                        if self.isValidSudoku(board, i, j):
                            if self.internalSolveSudoku(board):
                                return True
                        board[i] = board[i][:j] + '.' + board[i][j + 1:]
                    return False
        return True
    
    
    def isValidSudoku(self, board, x, y):
        for i in range(9):
            if x != i and board[i][y] == board[x][y]: return False
        for i in range(9):
            if y != i and board[x][i] == board[x][y]: return False
        for i in range(3):
            for j in range(3):
                if x != (x // 3)* 3 + i and y != (y // 3)*3 + j and board[(x // 3)* 3 + i][(y // 3)*3 + j] == board[x][y]:
                    return False
        return True

test = Solution()
print(test.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]))

