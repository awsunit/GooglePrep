/*
Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). 

In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 
and the smaller integer moves to the end of the array. 

The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.
*/
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
    int getWinner(vector<int>& arr, int k) {
        int curk = k;
        int back = 0;
        int front = 1;
        while (curk > 0) {
            // searched entire array
            if (front >= arr.size()) {
                return arr.at(back);
            }
            if (arr.at(back) < arr.at(front)) {
                // count is restarting
                curk = k - 1;
                back = front;
            } else {
                curk--;
            }
            front++;      
        }
        return arr.at(back);
    }
};

int main() {
    vector<int> v = {28,779,346,302,257,535,906,981,
    313,163,384,395,891,881,332,656,652,84,22,718,953,117,912};
    int k = 5;
    Solution s;
     cout << s.getWinner(v, k) << endl;

    return 0;

}
