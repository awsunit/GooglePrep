
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


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0) return 0;
        int mx = 0;
        bool allower = true;
        for (int i = 0; i < prices.size() - 1; ++i) {
            if (prices.at(i) < prices.at(i + 1)) {
                allower = false;
                break;
            }
        }
        
        if (allower) return 0;

        for (int outer = 0; outer < prices.size(); ++outer) {
            int cost = 0;
            int cur = prices.at(outer);
            for (int inner = outer + 1; inner < prices.size(); ++inner) {
                if (prices.at(inner) > cur) {
                    cost = (prices.at(inner) - cur) > cost ? (prices.at(inner) - cur) : cost;
                }
            }
            mx = mx > cost ? mx : cost;
        }

        return mx;
        
    }
};

int main () {
    Solution s;
    vector<int> v = {};

    cout << s.maxProfit(v) << endl;
}