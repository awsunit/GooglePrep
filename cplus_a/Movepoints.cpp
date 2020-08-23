// On a plane there are n points with integer coordinates points[i] = [xi, yi]. 

// Your task is to find the minimum time in seconds to visit all points.

// You can move according to the next rules:

// In one second always you can either move vertically, horizontally by one unit or diagonally 
// (it means to move one unit vertically and one unit horizontally in one second).

// You have to visit the points in the same order as they appear in the array.
#include <vector>
#include <iostream>
#include <unordered_set> 
#include <algorithm> 
#include <string>
#include <math.h>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::string;

class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        // for each pair
        // compute pyth distance
        // add to sum
        int sum = 0;
        for (auto v = points.begin(); v != points.end() - 1; ++v) {
            auto t = v + 1;
            sum += pyth(*v, *t);
        }
        return sum;
    }

    int pyth(vector<int> a, vector<int> b) {
        int minx = std::min(a.at(0), b.at(0));
        int maxx = std::max(a.at(0), b.at(0));
        int miny = std::min(a.at(1), b.at(1));
        int maxy = std::max(a.at(1), b.at(1));

        int sum = 0;
        while (minx < maxx && miny < maxy) {
            sum++;
            minx++;
            miny++;
        }
        sum += (maxx - minx);
        sum += (maxy - miny);
        return sum;
    }
};