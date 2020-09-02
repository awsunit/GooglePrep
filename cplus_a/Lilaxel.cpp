// Little Axel has N toys numbered from 1 to N. Each toy has two properties:

// Ei—enjoyment, which is the number of minutes Axel can play with 
// toy number i without getting bored with it;

// Ri—remembrance, which is the number of minutes it takes Axel to forget 
// toy number i after having played with it.

// The toys are arranged in a circle, from 1 to N clockwise. Axel plays with them one by one.

// When Axel reaches toy i which he has not played with yet, or which he has already forgotten about, 
// he plays with it for Ei minutes and then immediately moves to the next one (clockwise).

// If he reaches a toy that he has not forgotten yet (if less than Ri minutes have passed since the last 
// time he finished playing with it), he will stop and cry.

// We can define the time Axel spent playing as the sum of Ei of every toy Axel played with before stopping. 
// If Axel played with a toy several times, it should be counted that many times.

// Given the description of the toys, remove the smallest possible number of them in order to make Axel play 
// either an indefinitely long time, 
// or (if that is not possible) as long as possible before he stops.

// Note:

// Axel has never played with these toys before;
// he cannot be left without toys;
// he always starts with the toy that has the smallest number;
// after finishing playing with the toy that has the largest number, he will move to the toy that has the smallest number.
// Input
// The first line of the input gives the number of test cases, T. T test cases follow. 
// Each test case begins with a line containing the integer N. 

// Next N lines contain 2 integers each: Ei and Ri. The i-th line is describing the toy number i.

// Output
// For each test case, output one line containing Case #x: y z, where:

// x is the test case number (starting from 1);
// y is the minimal number of toys to remove so that Axel could play with the rest of them either indefinitely or as long as possible;
// z is the longest time Axel will play in minutes or "INDEFINITELY" (without quotes) if he will play indefinitely long time.
// Limits
// Time limit: 30 seconds per test set.
// Memory limit: 1GB.
// 1 ≤ T ≤ 100.
// 1 ≤ Ei ≤ 109.
// 1 ≤ Ri ≤ 109.

// Test Set 1
// 1 ≤ N ≤ 12.

// Test Set 2
// 1 ≤ N ≤ 105.

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
int main() {
    ifstream cin;
    cin.open("testcases/Lilaxel.txt");

    int testcase, testcases;
    string word;
    getline(cin, word);

    testcases = stoi(word);
    testcase = 1;

    while (testcase <= testcases) {
        map<int, pair<int, int>> toy_stats;
        map<int, int> time_left;

        int num = 0;
        int timespent = 0;
        int N;

        getline(cin, word);
        N = stoi(word);
        int toy = 1;

        while (N-- > 0) {
            int E, R;
            cin >> E;
            cin >> R;
            getline(cin, word);
            cout << E << " " << R << endl;
            pair<int,int> p(E, R);
            toy_stats[toy] = p;
            toy++;
        }




        cout << "Case #" << testcase << ": " << num << " " << timespent << endl;
        testcase++;
    }

    cin.close();
    
}