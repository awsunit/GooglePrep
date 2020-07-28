/*
    You have a total of n coins that you want to form in a 
    staircase shape, where every k-th row must have exactly k coins.

    Given n, find the total number of full staircase rows 
    that can be formed.

    n is a non-negative integer and fits within the range of a 32-bit signed integer.
*/
#include <iostream>

using std::cout;
using std::endl;
using std::cin;


class Solution 
{
    private:
        int arrangeCoins(unsigned int coins, int step, int count)
        {
            if (step > coins)
            {
                return count;
            }
            coins -= step;
            step++;
            count++;
            return arrangeCoins(coins, step, count);
        }

    public:
    int arrangeCoins(int coins)
    {
        return arrangeCoins(coins, 1, 0);
    }

};
