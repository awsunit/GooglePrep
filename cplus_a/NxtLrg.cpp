/**
 Definition for singly-linked list.
/
*/
#include <vector>
#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::vector;

 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> r;
        int spot = 0;
        ListNode* thead = head;
        while(thead != nullptr) {
            ListNode* mb = thead->next;
            int v = 0;
            while (mb != nullptr && mb->val <= thead->val) {
                mb = mb->next;
            }
            if (mb != nullptr) {
                v = mb->val;
            }
            r.push_back(v);
            thead = thead->next;
        }
        return r;
    }
};