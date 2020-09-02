// In a country popular for train travel, you have planned some train travelling one year in advance.  

// The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

// Train tickets are sold in 3 different ways:

// a 1-day pass is sold for costs[0] dollars;
// a 7-day pass is sold for costs[1] dollars;
// a 30-day pass is sold for costs[2] dollars.
// The passes allow that many days of consecutive travel.  

// For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

// Return the minimum number of dollars you need to travel every day in the given list of days.

#include <vector>
#include <iostream>
#include <stdlib.h>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <map>
#include <algorithm>
#include <math.h>
#include <unordered_set>
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
using std:: unordered_set;

class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        // always look at cheapest option
        int leftover = 0;
        int cost = costs.at(0);

        for (int v = 0; v < days.size() - 1; ++v) {
            // base case where we can ignore this day?
            int cur = costs.at(0);  // have to at least purchase a single pass
            // how far away?
            int dist = days.at(v + 1) - days.at(v);
            if (leftover >= dist) {
                leftover -= dist;
                // no need to purchase a ticket
                continue;
            }
            int daypass = dist * costs.at(0);
            int weekpass = ceil(dist/7) * costs.at(1);
            int months = ceil(dist/30) * costs.at(2);
            
        }


        return cost;
    }
};

int main () {
    vector<int> v = {1, 4, 5, 7, 9};
    unordered_set<int> t(v.begin(), v.end());

    for (auto i : t) {
        cout << i << " ";
    }
    cout << endl;
}