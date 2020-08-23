// In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

// There is at least one empty seat, and at least one person sitting.

// Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

// Return that maximum distance to closest person.
#include <vector>
#include <iostream>
#include <unordered_map> 
#include <algorithm> 
#include <string>
#include <math.h>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::string;
using std::unordered_map;
using std::max_element;
using std::pair;

bool comp (const pair<int, int> i, const pair<int, int> j) {return i.second < j.second;}

class Solution {

public:
    int maxDistToClosest(vector<int>& seats) {
        int max = 0;
        // int curmax = 0;
        unordered_map<int, int> seat_to_neigbor;
        // zip forward
        for (int i = 0; i < seats.size();) {
            int cur = 0;
            int t = i;
            while (t < seats.size() && seats.at(t) == 0) {
                cur++;
                t++;
            }
            // t == 1 or t == size
            for (int v = i; v < t; v++) {
                seat_to_neigbor[v] = cur;
                cur--;
            }
            i = t + 1;
        }
        // zip backwards
        for (int i = seats.size() - 1; i >= 0;) {
            int cur = 0;
            int t = i;
            while (t >= 0 && seats.at(t) == 0 ){
                cur++;
                t--;
            }
            for (int v = i; v > t; v--) {
                if (seat_to_neigbor[v] > cur) {
                    seat_to_neigbor[v] = cur;
                    cur--;
                }
            }
            i = t - 1;
        }
        return (*max_element(seat_to_neigbor.begin(), seat_to_neigbor.end(), comp)).second;
    }
};

int main() {
    Solution s;
    // vector<int> v = {1,0,0,0};
    vector<int> v = {1,0,0,0,1,0,1};
    cout << s.maxDistToClosest(v) << endl;
}