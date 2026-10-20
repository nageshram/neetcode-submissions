# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        st=[]
        def preorder(root):
            if not root:
                st.append('#')
                return
            st.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return ",".join(st)



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        st = data.split(',')
        i=0
        def dfs():
            nonlocal i
            if st[i]=='#':
                i+=1
                return None
            
            node=TreeNode(val=int(st[i]))
            i+=1
            node.left = dfs()
            node.right= dfs()

            return node

        root=dfs()
        return root if len(data)>0 else None




             

