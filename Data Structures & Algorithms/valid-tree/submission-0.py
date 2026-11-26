class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def bfs(node, parent=None):

            if node in visited:
                return False
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not bfs(nei, node):
                    return False

            return True
            

        return bfs(0,None) and len(visited) == n