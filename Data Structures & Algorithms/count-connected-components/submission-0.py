class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        visited = set()
        adj = { i:[] for i in range(n)}
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        def dfs(node):
            if node is None:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                dfs(node)
                count+=1

        return count if n>0 else 0
            


        