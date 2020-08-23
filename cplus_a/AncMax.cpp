// Given the root of a binary tree, find the maximum value V for which 
// there exists different nodes A and B where V = |A.val - B.val|
//  and A is an ancestor of B.

// (A node A is an ancestor of B if either: any child of A is equal to B,
//  or any child of A is an ancestor of B.)

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        
    }
};