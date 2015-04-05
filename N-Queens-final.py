#!/user/bin/python

def totalNQueens(self, n):
    # output frame
    global res
    final = []
    def solve(self, n, currQueenNum, board):
        
        if currQueenNum == n:
            res = []
            
            for i in range(n):
                a = []
                for j in range (n):
                    a.append('.')
                res.append(a)

            for l in range(n):
                res[l][board[l]] = 'Q'
                res[l] = ''.join(res[l])
            final.append(res[:])
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
                solve(self, n, currQueenNum + 1, board)
    
    board = []
    for i in range(n):
        board.append(-1)
    solve(self, n, 0, board)
    return final
     
    
    
self = 0
n = 4
print(totalNQueens(self, n))
