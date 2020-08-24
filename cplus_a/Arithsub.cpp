// Problem
// An arithmetic array is an array that contains at least two integers and the differences between consecutive integers are equal. 

// For example, [9, 10], [3, 3, 3], and [9, 7, 5, 3] are arithmetic arrays, 
// while [1, 3, 3, 7], [2, 1, 2], and [1, 2, 4] are not arithmetic arrays.

// Sarasvati has an array of N non-negative integers. The i-th integer of the array is Ai. 
// She wants to choose a contiguous arithmetic subarray from her array that has the maximum length. 
// Please help her to determine the length of the longest contiguous arithmetic subarray.

// Input
// The first line of the input gives the number of test cases, T. T test cases follow. 

// Each test case begins with a line containing the integer N. 

// The second line contains N integers. The i-th integer is Ai.

// Output
// For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and 
// y is the length of the longest contiguous arithmetic subarray.

// Limits
// Time limit: 20 seconds per test set.
// Memory limit: 1GB.
// 1 ≤ T ≤ 100.
// 0 ≤ Ai ≤ 109.

// Test Set 1
// 2 ≤ N ≤ 2000.

// Test Set 2
// 2 ≤ N ≤ 2 × 105 for at most 10 test cases.
// For the remaining cases, 2 ≤ N ≤ 2000.


#include <vector>
#include <iostream>
#include <stdlib.h>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
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


int finish(vector<int> v) {
    int length = 0;
    for (int i = 0; i < v.size() - 1; ) {
        int nxt = i + 1;
        int diff = v.at(i) - v.at(nxt);
        int t = 2;
        ++nxt;
        while (nxt < v.size() && v.at(i) - v.at(nxt) == diff) {
            nxt++;
            t++;
        }
        length = length > t ? length : t;
        cout << "here" ;
        i = nxt - 1;
    }
    return length;
}


int main() {
    ifstream cin;
    cin.open("testcases/Arithsub.txt");

    int testcases, testcase, N;
    string input;

    std::getline(cin, input);
    testcases = stoi(input);
    testcase = 1;

    while (testcase <= testcases) {
        int length = 0;

        std::getline(cin, input);
        N = stoi(input);
        

        std::getline(cin, input);
        istringstream ss(input);
        vector<int> v;
        for(string s; ss >> s; ){
            v.push_back(stoi(s));
        }


        for (int i = 0; i < v.size() - 1; ) {
            int nxt = i + 1;
            int diff = v.at(i) - v.at(nxt);
            int t = 2;
            ++nxt;
            while (nxt < v.size() && v.at(nxt - 1) - v.at(nxt) == diff) {
                nxt++;
                t++;
            }
            length = length > t ? length : t;
            // cout << "here" ;
            i = nxt - 1;
        }

        cout << "Case #" << testcase << ": " << length << endl;
        testcase++;
    }

    cin.close();
    return 0;
}
