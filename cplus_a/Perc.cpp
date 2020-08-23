// Given an array of positive integers w. where w[i] describes the weight of ith index (0-indexed).

// We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. 

// pickIndex() should return the integer proportional to its weight in the w array. 

// For example, for w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) 
// while the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

// More formally, the probability of picking index i is w[i] / sum(w).

#include <vector>
#include <iostream>
#include <stdlib.h>
#include <set>
#include <map>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::set;
using std::map;

class Solution {
public:

    vector<int> prevPermOpt1(vector<int>& A) {
        map<int, int> m;  // int -> i : A[i] == int
        int i = 0;
        int j = 0;

        for (int back = A.size() - 1; back > -1; --back) {
            int v = A.at(back);
            for (auto it = m.rbegin(); it != m.rend(); ++it) {
                if (it->first < v) {
                    // swapping these
                    i = back;
                    j = it->second;
                    int t = A.at(back);
                    A.at(back) = A.at(j);
                    A.at(j) = t;
                    return A;                  
                }
            }
            m[A.at(back)] = back;
        }
        return A;
    }
};
int main () {
    // vector<int> v({3,2,1});
    vector<int> v({3,1, 1, 1,3});
    Solution solution;
    v = solution.prevPermOpt1(v);

    for (auto i : v) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}

// template <typename t>
// void printv(vector<t> v) {
//     for (auto i : v) {
//         cout << i << " ";
//     }
//     cout << endl;
// }

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */