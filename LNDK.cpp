// Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

// Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

// You may return the answer in any order.

#include <vector>
#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::vector;


class Huh {
public:
    vector<int> numsSameConsecDiff(int N, int K) {
        vector<int> r;
        // want a vector<vector<int>>
        vector<vector<int>> t;
        // build our vector up one number at a time?
        for (int num = 1; num <= N; ++num) {
            if (num == 1) {
                populate(t, K);
            } else {
                addDigit(t, K);
            }
        }
        populater(r, t);
        return r;
    }
    void populate(vector<vector<int>>& t, int K) {
        int first = 9;
        while (first - K > -1) {
            // while there are digits that we can add K to
            // and still be a single digit
            vector<int> f1, f2;;
            f1.push_back(first);
            f2.push_back(first - K);
            t.push_back(f1);
            if (first - K != 0) {
                t.push_back(f2);
            }
            // t.insert(t.end(), {f1, f2});                    
            first--;
        }

    }
    void addDigit(vector<vector<int>>& t, int K) {
         for (auto& cn: t) {
            // take last digit added, subtract or add K
            int last = cn.back();
            // cout << "Last: " << last << endl;
            if (last + K < 10) {
                cn.push_back(last + K);
            } else {
                cn.push_back(last - K);
            }
                    
        }
    }

    void populater(vector<int>& r, vector<vector<int>> t) {
        for (vector<vector<int>>::const_iterator i = t.begin(); i != t.end(); ++i) {
            int val = 0;
            for (auto num : *i) {
                if (val == 0) {
                    val = num;
                } else {
                    int tt = val * 10;
                    val = tt + num;
                }
            }
            r.push_back(val);
        }
    }

};
int main (int argc, char** argv) {

    Huh s;
    int N = 3;
    int K = 7;
    vector<int> r = s.numsSameConsecDiff(N, K);

    for (auto i = r.begin(); i != r.end(); ++i) {
        cout << *i << ' ';
    }
    cout << endl << "buhbye" << endl;
    return 0;
}