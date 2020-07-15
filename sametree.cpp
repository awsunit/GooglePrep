/**
 * Definition for a binary tree node.

 */
#include <iostream>

using namespace std;

 struct TreeNode 
 {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // null case?
        if (p == nullptr || q == nullptr)
        {
            if (q == nullptr && p == nullptr) return true;
            return false;
        }
        // non null
        return (p->val == q->val) && isSameTree(p->right, q->right) && isSameTree(p->left, q->left);

    }
};

int main()
{

    cout << "all done boss" << endl;
    return 0;
}