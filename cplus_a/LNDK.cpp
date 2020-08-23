// Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

// Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

// You may return the answer in any order.

#include <vector>
#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::vector;



class Solution {
public:
    void populate(vector<vector<int>>& t, int K) {
        int first = 1;
        while (first + K < 10) {
            // while there are digits that we can add K to
            // and still be a single digit
            vector<int> f1, f2;;
            f1.push_back(first);
            f2.push_back(first + K);
            t.insert(t.end(), {f1, f2});                    
            first++;
        }

    }
    vector<int> numsSameConsecDiff(int N, int K) {
        vector<int> r;
        // want a vector<vector<int>>
        vector<vector<int>> t;
        // build our vector up one number at a time?
        for (int num = 1; num <= N; ++num) {
            if (num == 1) {
                populate(t, K);
                for (auto outer : t) {
                    for (auto inner: outer) {
                        cout << inner << " ";
                    }
                    cout << endl;
                }
            } else {
                cout << "nah" << endl;
                // adding another digit
                // for (auto& cn: r) {
                //     // take last digit added, subtract or add K
                    
                // }
            }
        }
        return r;
    }

    int main (int argc, char** argv) {

    Solution s;
    int N = 3;
    int K = 7;
    vector<int> r = s.numsSameConsecDiff(N, K);

    for (auto i = r.begin(); i != r.end(); ++i) {
        cout << *i << ' ';
    }
    cout << endl << "buhbye" << endl;
    return 0;
    }
};
