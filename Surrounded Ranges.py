class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def bfs(self, x, y, board):
        m = len(board)
        n = len(board[0])
        if board[x][y] != '0': return
        board[x][y] = '*'
        queue = [(x, y)]
        d = [[-1, 0], [1, 0], [0, 1],[0, -1]]
        while queue:
            x, y = queue.pop()
            for i in range(4):
                nx = x + d[i][0]
                ny = y + d[i][1]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and board[nx][ny] == '0':
                    board[nx][ny] = '*'
                    queue.append((nx, ny))
    
    def solve(self, board):
        m = len(board)
        if m <= 2 or board is None: return
        n = len(board[0])
        if n <= 2: return
        for i in range(m):
            self.bfs(i, 0, board)
            self.bfs(i, n - 1, board)
        for i in range(n):
            self.bfs(0, i, board)
            self.bfs(m - 1, i, board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = '0'
                elif board[i][j] == '0':
                    board[i][j] = 'X'
        return board

test = Solution()
board = [['X', 'X', 'X', 'X'],
         ['X', '0', '0', 'X'],
         ['X', 'X', '0', 'X'],
         ['X', '0', 'X', 'X']]
print(test.solve(board))
