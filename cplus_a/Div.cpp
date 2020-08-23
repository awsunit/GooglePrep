#include <vector>
#include <iostream>
#include <stdlib.h>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0 || divisor == 0) {
            return 0;
        }
        int i = 0;
        unsigned int ndivisor = divisor > 0 ? divisor : -1 * divisor;
        unsigned int ndividend = dividend > 0 ? dividend : -1 * dividend;

        while (ndividend >= ndivisor) {
                ndividend -= ndivisor;
                i++;     
        }
        if ((dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0)) {
            return int(i);
        } else {
            return -i;
        }
        
    }
};


int main () {
    Solution s;
    cout << int(s.divide(2147483648, -1)) << endl;
}