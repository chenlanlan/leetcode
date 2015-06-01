#!/usr/bin/python

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def isInBoard(self, x, y, board):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        return True
    
    def findnext(self, board, i, j, words, h, idx, visit, temp):
        if idx + 1 == len(words[h]) and temp[-1] == words[h][idx] :
            return True
        if temp[-1] == words[h][idx]:
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if self.isInBoard(ni, nj, board) and visit[ni][nj] == False:
                    temp += board[ni][nj]
                    visit[ni][nj] = True
                    if self.findnext(board, ni, nj, words, h, idx + 1, visit, temp):
                        return True
                    else:
                        temp = temp[: -1]
                        visit[ni][nj] = False
        return False           
        
    def findword(self, board, words, h, row, col):
        visitR = [False for i in range(col)]
        visit = [visitR[:] for i in range(row)]
        for i in range(row):
                for j in range(col):
                    if words[h][0] == board[i][j]:
                        temp = words[h][0]
                        visit[i][j] = True
                        if col == 1 and len(words[h]) == 1:
                            return True
                        if self.findnext(board, i, j, words, h, 0, visit, temp):
                            return True                       
                        visit[i][j] = False
        return False
    
    def findWords(self, board, words):
        row = len(board)
        col = len(board[0])
        res = []
        for h in range(len(words)):
            if self.findword(board, words, h, row, col):
                res.append(words[h])
        return res

test = Solution()
print(test.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"]))
                
