#include <vector>
#include <iostream>
#include <unordered_set> 
#include <algorithm> 
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::string;

class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string ns(s.length(), 'a');
        int c = 0;
        for (auto i : indices) {
            ns.at(i) = s.at(c);
            c++;
        }
        return ns;
    }
};