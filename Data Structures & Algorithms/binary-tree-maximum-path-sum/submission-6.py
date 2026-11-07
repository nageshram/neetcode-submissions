# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        def dfs(node):
            nonlocal max_path
            if node is None:
                return 0
            
            max_left = max(dfs(node.left), 0)
            max_right = max(dfs(node.right),0)
            max_path = max(max_path, node.val+max_left+max_right)
            return node.val + max(max_left, max_right)
            
        dfs(root)

        return max_path if max_path != float('-inf') else 0

        