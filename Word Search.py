#!/usr/bin/python

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def isInBoard(self, i, j, board):
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
            return False
        return True
        
    def find(self, board, word, visit, wi, i, j, temp):
        if wi + 1 == len(word) and temp[-1] == word[wi]:
            return True
        if temp[-1] == word[wi]:
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for h in range(4):
                ni = i + dx[h]
                nj = j + dy[h]
                if self.isInBoard(ni, nj, board):
                    if visit[ni][nj]:
                        temp += board[ni][nj]
                        visit[ni][nj] = False
                        if self.find(board, word, visit, wi + 1, ni, nj, temp):
                            return True
                        else:
                            temp = temp[ : -1]
                            visit[ni][nj] = True
        return False
        
    def exist(self, board, word):
        row = len(board)
        col = len(board[0])
        visitR = [True for i in range(col)]
        visit = [visitR[:] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:                    
                    temp = word[0]
                    visit[i][j] = False
                    if col == 1 and len(word) == 1:
                        return True
                    elif self.find(board, word, visit, 0, i, j, temp):
                        return True
                    visit[i][j] = True
        return False

test = Solution()
print(test.exist(
  ["CAA","AAA","BCD"],
 'AAB'))
                
