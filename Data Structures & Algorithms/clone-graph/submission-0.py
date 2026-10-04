"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node or node==None: 
            return None
        if len(node.neighbors)<=0:
            return Node(node.val)
        
        visited = {}
        def dfs(cur_node):
            if not node:
                return
            if  cur_node in visited:
                return visited[cur_node]
            
            copy_node = Node(cur_node.val)
            visited[cur_node]=copy_node
            for n in cur_node.neighbors:
                copied_neighbor = dfs(n)
                copy_node.neighbors.append(copied_neighbor)
            
            return copy_node

        return dfs(node)


        


        