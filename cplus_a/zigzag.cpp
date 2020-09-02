#include <vector>
#include <iostream>
#include <stdlib.h>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <map>
#include <algorithm>
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
using std::reverse;



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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> v =  recurse(root, false);
        // bool right = false;
        // vector<vector<int>> fin;
        // for (auto vect = v.rbegin(); vect < v.rend(); ++vect) {
        //     vector<int> v_i = *vect;
        //     if (right) {
        //         reverse(v_i.begin(), v_i.end());
        //         // for (auto t: v_i) {
        //         //     cout << t << " ";
        //         // }
        //         // cout << endl;
        //     }
        //     if (v_i.size() != 0) fin.push_back(v_i);
        //     right = !right;
        // }
        // return fin;
        return v;
    }

    vector<vector<int>> recurse(TreeNode *root,  bool goright) {
        
        if (root == nullptr) {
            vector<vector<int>> v;
            vector<int> empty;
            v.push_back(empty);
            return v;
        }

        vector<vector<int>> fin;
        goright = !goright;
        vector<vector<int>> l = recurse(root->left, goright);
        vector<vector<int>> r = recurse(root->right, goright);
        
        for (int vect = 0; vect < l.size(); ++vect) {
            vector<int> l_i = l.at(vect);
            vector<int> r_i = r.at(vect);

            if (goright) {
                r_i.insert(r_i.end(), l_i.begin(), l_i.end());
                fin.push_back(r_i);
            } else {
                l_i.insert(l_i.end(), r_i.begin(), r_i.end());
                fin.push_back(l_i);
            }
            goright = !goright;

            // l_i.insert(l_i.end(), r_i.begin(), r_i.end());
            // fin.push_back(l_i);
        }
        vector<int> us;
        us.push_back(root->val);
        fin.push_back(us);
        return fin;
    }
};

int main () {
    TreeNode one(1);
    TreeNode two(2);
    TreeNode three(3);
    TreeNode four(4);
    TreeNode nine(9, &one, &two);
    TreeNode twenty(20, &three, &four);
    TreeNode eight(8, &nine, &twenty);

    Solution s;
    vector<vector<int>> v = s.zigzagLevelOrder(&eight);

    for (auto outer : v) {
        for (auto inner : outer) {
            cout << inner << " ";
        }
        cout << endl;
    }

    cout << "buhbye" << endl;
}