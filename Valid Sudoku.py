#!/usr/bin/python

class Solution:
    # @param {character[][]} board
    # @return {boolean}        
    def check(self, str, d):
        if str != '.' and str in d:
            return True
        d[str] = 1
        return False
    
    def isValidSudoku(self, board):
        #check the rows
        for i in range(9):
            d = {}
            for j in range(9):
                if self.check(board[i][j], d):
                    return False
        #check the columns
        for i in range(9):
            d = {}
            for j in range(9):
                if self.check(board[i][j], d):
                    return False
        #check the grid
        for x in range(1, 8, 3):
            for y in range(1, 8, 3):
                d = {}
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if self.check(board[x + i][y + j], d):
                            return False
        return True

test = Solution()
print(test.isValidSudoku(["......5..",".........",".........","93..2.4..","..7...3..",".........","...34....",".....3...",".....52.."]))
