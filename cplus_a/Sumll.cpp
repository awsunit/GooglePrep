#include <vector>
#include <iostream>
#include <stdlib.h>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <map>
// #include <string>

using std::cout;
// using std::cin;
using std::endl;
using std::vector;
using std::set;
using std::map;
using std::ifstream;
using std::string;
using std::istringstream;
using std::stoi;
using std::getline;
using std::pair;

struct TreeNode {
     int val;
     TreeNode* left;
     TreeNode* right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
 };


class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        return recurse(root, false);
    }

    int recurse (TreeNode* root, bool left) {
        if (root == nullptr) return 0;

        if (root->left == nullptr && root->right == nullptr) {
            if (left) return root->val;
            return 0;
        }

        return recurse(root->left, true) + recurse(root->right, false); 

    }
};

int main () {
    cout << "buhbye" << endl;
}