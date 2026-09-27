# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=collections.deque()#bfs
        q.append(root)
        li=[]
        while q:
            qlen=len(q)
            level=[]
            for i in range(qlen):
                pop=q.popleft()
                if pop:
                    level.append(pop.val)
                    q.append(pop.left)
                    q.append(pop.right)
            if level:
                li.append(level)
        return li
                

            
