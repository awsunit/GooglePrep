/*
Bucket is planning to make a very long journey across the countryside 
by bus. Her journey consists of N bus routes, numbered from 1 to N 
in the order she must take them. 

The buses themselves are very fast, but do not run often. 
The i-th bus route only runs every Xi days.

More specifically, she can only take the i-th bus on day 
Xi, 2Xi, 3Xi and so on. 
Since the buses are very fast, she can take multiple buses on the 
same day.

Bucket must finish her journey by day D, but she would like to start 
the journey as late as possible. 

What is the latest day she could take the first bus, 
and still finish her journey by day D?

It is guaranteed that it is possible for Bucket to finish her 
journey by day D.

Input
The first line of the input gives the number of test cases, T. 
T test cases follow. 
Each test case begins with a line containing the two integers N and D. 
Then, another line follows containing N integers, 
the i-th one is Xi.

*/

#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>

using namespace std;

int main() 
{

    string name = "rb_t.txt";
    // ifstream cin(name);

    int testcases;
    int testcase = 1;

    cin >> testcases;
    cin.ignore();

    while (testcase <= testcases)
    {
        string line, word;
        getline(cin, line);

        istringstream ss(line);

        long N, D;
        ss >> N;
        ss >> D;

        getline(cin, line);
        vector<long> routes;

        ss = istringstream(line);

        while (ss >> word)
        {
            auto it = routes.begin();
            routes.insert(it, stol(word));
        }

        auto it = routes.begin();
        while (it != routes.end())
        {
            // cout << *it << " ";
            it++;
        }
        // cout << endl;
        long startingday = D;
        for (int i = 0; i < routes.size(); ++i)
        {

            long cur = routes[i];  // first == actual_last

            if (cur > startingday) 
            {
                // startingday = cur;
            } 
            else
            {
                long remainder = startingday % cur;
                startingday -= remainder;
            }
          
        }
        cout << "Case #" << testcase << ": " << startingday << endl;
        testcase++;
    }


    return 0;
}