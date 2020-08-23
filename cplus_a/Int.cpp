
#include <vector>
#include <iostream>
#include <stdlib.h>
#include <unordered_map>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::string;
using std::unordered_map;
class Solution {
public:

    

    bool isInterleave(string s1, string s2, string s3) {
        string smallest = s1.size() > s2.size() ? s2 : s1;
        string largest = s1.size() <= s2.size() ? s2 : s1;  
        int s = 0;
        int l = 0;
        int f = 0;

        return recurse(smallest, largest, s3, s, l, f);
    }
    bool a() {
        cout << "a was here" << endl;
        return true;
    }

    bool b() {
        int i = abs(-1);
        cout << "b was here" << endl;
        return false;
    }

    bool recurse(string smallest, string largest, string s3, int s, int l, int f) {
        if (f >= s3.size()) {
            return true;
        }
        // do we bifurcate?
        if (s < smallest.size() && l < largest.size() && smallest.at(s) == largest.at(l) && smallest.at(s) == s3.at(f)) {
            return recurse(smallest, largest, s3, s + 1, l, f + 1) || recurse(smallest, largest, s3, s, l + 1, f + 1);
        } else if (s < smallest.size() && smallest.at(s) == s3.at(f)) {
            // smallest matches
            return recurse(smallest, largest, s3, s + 1, l, f + 1);
        } else if (l < largest.size() && largest.at(l) == s3.at(f)) {
            //largest matches
            return recurse(smallest, largest, s3, s, l + 1, f + 1);
        } else {
            // need at least one of these letters to match
            return false;
        }
    }

};

int main() {
    // string s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac";
    string s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc";
    Solution s;
    // cout << "yes? " << s.isInterleave(s1, s2, s3) << endl;
    if (s.b() || s.a()) {
        cout << "doneski" << endl;
    }
    return 0;
}