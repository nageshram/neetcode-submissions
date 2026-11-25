class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        visited = set()
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or (i,j) in visited:
                return
            
            visited.add((i,j))
            for col in range(n):
                if matrix[i][col] == 0:
                    continue
                else:
                    matrix[i][col] = 0
                    visited.add((i,col))

            for row in range(m):
                if matrix[row][j] ==0:
                    continue
                else:
                    matrix[row][j] = 0
                    visited.add((row,j))

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0 and (i,j) not in visited:
                    dfs(i,j)

                
            





                

        