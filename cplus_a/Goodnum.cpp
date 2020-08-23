// X is a good number if after rotating each digit individually by 
// 180 degrees, we get a valid number that is different from X.  

// Each digit must be rotated - we cannot choose to leave it alone.

// A number is valid if each digit remains a digit after rotation. 0, 1, 
// and 8 rotate to themselves; 

// 2 and 5 rotate to each other (on this case they are 
// rotated in a different direction, in other words 2 or 5 gets mirrored);

// 6 and 9 rotate to each other, 

// and the rest of the numbers do not rotate to any other number and 
// become invalid.

// Now given a positive number N, how many numbers X from 1 to N are good?
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
    int rotatedDigits(int N) {
        vector<int> ok = {0,1,8};
        vector<int> good = {2,5,6,9};
        vector<int> bad {3, 4, 7};

        if (N < 10) {
            int s = 0;
            int c = 0;
            while (c < N) {
                c += good.at(s);
                s++;
            }
            
        }
    }
};