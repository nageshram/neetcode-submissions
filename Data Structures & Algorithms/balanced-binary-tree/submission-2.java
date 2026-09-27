/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    boolean isBalanced=true;
    public boolean isBalanced(TreeNode root) {
        if(root==null)
        return true;
        int h=dfs(root);
        return isBalanced;

    }
    public int dfs(TreeNode root)
    {
        if (root==null)
           return 0;
        int left=dfs(root.left);
        int right=dfs(root.right);
        if (Math.abs(left-right)>1)
        {
            this.isBalanced=false;
            return 0;
        }
        return 1+Math.max(dfs(root.left),dfs(root.right));
    }
}
