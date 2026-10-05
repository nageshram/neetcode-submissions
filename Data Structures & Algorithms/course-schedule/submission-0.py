class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path=set()
        adj={}
        for i in range(numCourses):
             adj[i]=[]
        for i, val in prerequisites:
            adj[i].append(val)
        
        def dfs(node):
            if node in path:
                return False
            if adj[node] == []:
                return True
            
            path.add(node)
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            path.remove(node)
            adj[node]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


