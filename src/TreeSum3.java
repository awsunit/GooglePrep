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
    public int pathSum(TreeNode root, int sum) {
        if (root == null) {
            return 0;
        }
        return recurse(root, new ArrayList<Integer>, sum, 0);        
    }
 
    public int recurse(TreeNode n, List<Integer> sums, int sum, int count) {
        if (n.val == sum) {
            count++;
        }
        
        
    }
}