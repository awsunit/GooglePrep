// Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
// followed by all the odd elements of A.

// You may return any answer array that satisfies this condition.
#include <vector>
#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::vector;

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> evens;
        vector<int> odds;

        for (auto i: A) {
            if (i % 2) {
                odds.push_back(i);
            } else {
                evens.push_back(i);
            }
        }
        evens.insert(evens.end(), odds.begin(), odds.end());
        return evens;
    }
};