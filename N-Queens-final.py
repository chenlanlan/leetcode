#!/usr/bin/python

class Solution:
    # @return a list of lists of string
    def __init__(self):
        self.final = []
        
    def solve(self, n, currQueenNum, board):
            if currQueenNum == n:
                a = ['.' for i in range(n)]
                res = [a[:] for i in range(n)]
                for l in range(n):
                    res[l][board[l]] = 'Q'
                    res[l] = ''.join(res[l])
                self.final.append(res[:])
                return
            
            for i in range(n):
                valid = True
                for k in range(currQueenNum):
                    # check column
                    if board[k] == i:
                        valid = False; 
                        break
                    # check diagonal
                    if abs(board[k] - i) == currQueenNum - k: 
                        valid = False;
                        break
                if valid:
                    board[currQueenNum] = i
                    self.solve(n, currQueenNum + 1, board)
                    
    def totalNQueens(self, n):
        # output frame
        board = [-1 for i in range(n)]
        self.solve(n, 0, board)
        return self.final
    
x = Solution()
print(x.totalNQueens(4))
