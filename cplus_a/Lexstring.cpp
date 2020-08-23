// # Return the lexicographically smallest subsequence of text that 
// # contains all the distinct characters of text exactly once.

// # Input: "cdadabcc"
// # Output: "adbc"
#include <vector>
#include <iostream>
#include <queue>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <map>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::priority_queue;
using std::string;
using std::unordered_map;
using std::pair;
using std::unordered_set;
using std::set;
using std::map;



class Solution {
public:
    void makemap (map<char, set<int>> &m, string text) {
        for (int i = 0; i < text.size(); i++) {
            auto it = m.find(text[i]);
            if (it != m.end()) {
                cout << "appending" << endl;
                it->second.insert(i);//push_back(i);
            } else {
                set<int> v;
                v.insert(i);
                pair<char, set<int>> p(text[i], v);
                m.insert(p);
            }
        }
    }

    bool greaterspot(char c, int nxt, set<int> &v) {
        for (auto it = v.begin(); it != v.end(); ++it) {
            if (*it > nxt) {
                v.erase(it);
                return true;
            }
        }
        return false;
    }
    string smallestSubsequence(string text) {
        string s;
        // first lets map from letter to locations
        map<char, set<int>> m;
        unordered_set<char> seen;
        makemap(m, text);
        for (int spot = 0; spot < text.size(); spot++) {
            // have we seen this?
            if (seen.find(text[spot]) != seen.end()) {
                continue;
            }
            if (spot == text.size() - 1) {
                // guaranteed largest letter
                s += text[spot];
            } else {
                if (text[spot + 1] < text[spot]) {
                    // possible better letter
                    bool found = false;
                    for (auto it = m[text[spot]].begin(); it != m[text[spot]].end(); ++it) {
                        if (*it > spot) {
                            // we can add this letter later, skip
                            m[text[spot]].erase(it);
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        s += text[spot];
                        seen.insert(text[spot]);
                    }
                } else {
                    for (auto it = m[text[spot]].begin(); it != m[text[spot]].end(); ++it) {
                        
                    }
                    if (m[text[spot]].size() == 1) {
                    s += text[spot];
                    seen.insert(text[spot]);
                }
            }
        }
        return s;
    }
};
int main () {
    Solution s;
    cout << s.smallestSubsequence("cdadabcc");
    return 0;
}

        // for(auto it = m.begin(); it != m.end(); ++it) {
        //     cout << it->first << " size is " << it->second.size() << endl;
        //     for (auto i : it->second) {
        //         cout << i << " ";
        //     } 
        //     cout << endl;
        // }