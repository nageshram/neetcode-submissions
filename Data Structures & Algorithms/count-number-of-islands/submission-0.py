class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        count = 0
        def dfs(grid:List[List[str]], i , j):
            if (i<0 or j<0 or j>=cols or i>=rows or visited[i][j] or grid[i][j]=='0'):
                return
            if not visited[i][j]:
                visited[i][j]=True
                
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
                     # dfs will visite the nodes but still we have to manage the traversal
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and not visited[r][c]:
                    dfs(grid, r,c)
                    count=count+1

        return count




        