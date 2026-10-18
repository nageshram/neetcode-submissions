# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]

        def bfs(root):
            q=deque()
            if root:
                    q.append(root)
                    while q:
                        level=[]

                        for i in range(len(q)):
                            node=q.popleft()
                            if node.left != None:
                                q.append(node.left)
                            if node.right != None:
                                q.append(node.right)
                            level.append(node.val)
                        res.append(level.copy())

            return res

        return bfs(root)


        
        