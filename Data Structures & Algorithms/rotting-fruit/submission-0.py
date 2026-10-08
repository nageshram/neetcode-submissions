class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        rows, cols= len(grid),len(grid[0])
        fresh = 0 
        mins = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        
        while q and fresh > 0: #BFS

            for _ in range(len(q)): # freezing the len(q) means one level 

                directions = [(-1, 0),(1,0), (0,1), (0,-1)]
                r,c = q.popleft()
                for dr, dc in directions:
                    nr,nc = r + dr, c+dc
                    if 0<= nr < rows and 0<= nc < cols:

                        if grid[nr][nc]==1:
                            grid[nr][nc]=2
                            fresh-=1
                            q.append((nr,nc)) # append it for next rotten also we can use it as visited
                #level completed 
            mins+=1
        
        return mins if fresh==0 else -1
            
                    




                    

        return mins if grid else 0




        