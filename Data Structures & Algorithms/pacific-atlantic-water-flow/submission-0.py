class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i, j, visited):

            visited.add((i,j))

            for dx, dy in directions:

                x, y = i + dx, j + dy

                if (x < 0 or x >= rows or
                    y < 0 or y >= cols):
                    continue

                if (x,y) in visited:
                    continue

                if heights[x][y] >= heights[i][j]:
                    dfs(x, y, visited)

        # Pacific: top row and left column
        for j in range(cols):
            dfs(0, j, pacific)

        for i in range(rows):
            dfs(i, 0, pacific)

        # Atlantic: bottom row and right column
        for j in range(cols):
            dfs(rows-1, j, atlantic)

        for i in range(rows):
            dfs(i, cols-1, atlantic)

        return [list(cell) for cell in pacific & atlantic]