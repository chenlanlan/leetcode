class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        def isValid(x,y):
            tmp=board[x][y]; board[x]= board[x][:y] + 'D' + board[x][y + 1:]
            for i in range(9):
                if board[i][y]==tmp: return False
            for i in range(9):
                if board[x][i]==tmp: return False
            for i in range(3):
                for j in range(3):
                    if board[(x//3)*3+i][(y//3)*3+j]==tmp: return False
            board[x]= board[x][:y] + tmp + board[x][y + 1:]
            return True
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in '123456789':
                            board[i] = board[i][:j] + k + board[i][j + 1:]
                            if isValid(i,j) and dfs(board):
                                return True
                            board[i] = board[i][:j] + '.' + board[i][j + 1:]
                        return False
            return True
        dfs(board)
        return board

test = Solution()
print(test.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]))
