class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board), len(board[0])
        def dfs(i,j,w,match):
            if i<0 or i>=rows or j<0 or j>=cols or board[i][j] != word[w] :
                return False
            
            if w == len(word)-1:
                return True
            temp = board[i][j]
            board[i][j]='#'
            dir = [ (0,1),(1,0),(0,-1),(-1,0)]
            for dr, dc in dir:
                if dfs(i+dr, j+dc, w+1, match):
                    board[i][j]=temp
                    return True
                    
            board[i][j]=temp
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0,""):
                        return True
        
        return False