#include <iostream>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::vector;

TreeNode* makeTree();
vector<vector<int>> levelOrderBottom(TreeNode *root);

class TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr){}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr){}
    TreeNode(int x, TreeNode *left, TreeNode *right) : 
        val(x), left(left), right(right){}

};

int main()
{
    cout << "Well Hi There" << endl;
    TreeNode *tree = makeTree();
    vector<vector<int>> lo = levelOrderBottom(tree);
}

TreeNode* makeTree()
{
    int nodes = 10;

    while 
}

vector<vector<int>> levelOrderBottom(TreeNode *root) 
{

}