// Find the sum of all left leaves in a given binary tree.

/**
 Definition for a binary tree node.

 */
class Solution {




    public int sumOfLeftLeaves(TreeNode root) {
        return recurse(root, false);     
    }

    int recurse (TreeNode root, boolean left) {
        // base 1
        if (root == null) {
            return 0;
        }
        // base 2
        if (left && root.left == null && root.right == null) {
            return root.val;
        }
        int l = recurse(root.left, true);
        int r = recurse(root.right, false);
        return l + r;
    }
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

}