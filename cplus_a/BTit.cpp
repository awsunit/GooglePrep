/**
Definition for a binary tree node.
 */
#include <vector>
#include <iostream>
#include <queue>
#include <functional>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::priority_queue;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class BSTIterator {
public:
    // auto compare = [] (const int i, const int j){return i < j;};
    priority_queue<int, std::less<int>> tree;
    int spot;

    BSTIterator(TreeNode* root) {
        populatetree(root);
        spot = 0;
    }
    void populatetree(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        tree.push(root->val);
        populatetree(root->left);
        populatetree(root->right);

    }
    /** @return the next smallest number */
    int next() {
        return tree.top();
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return tree.size() > 0;
    }
};

/**
Your BSTIterator object will be instantiated and called as such:
BSTIterator* obj = new BSTIterator(root);
int param_1 = obj->next();
bool param_2 = obj->hasNext();
 */