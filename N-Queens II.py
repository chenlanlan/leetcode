#!/usr/bin/python

class Solution:
    # @param {integer} n
    # @return {integer}
    def __init__(self):
        self.ans = 0
        
    def queens(self, board, n, curLevel):
        if curLevel == n:
            self.ans += 1
            return
        for i in range (n):
            valid = True
            for j in range(curLevel):
                if board[j] == i:
                    valid = False
                    break
                if abs(board[j] - i) == curLevel - j:
                    valid = False
                    break
            if valid:
                board[curLevel] = i
                self.queens(board, n, curLevel + 1)
        return
        
    def totalNQueens(self, n):
        board = [-1 for i in range (n)]
        self.queens(board, n, 0)
        return self.ans

test = Solution()
print(test.totalNQueens(4))
