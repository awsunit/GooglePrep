/*

The first line of the input gives the number of test cases, T. 
T test cases follow. 
The first line of each test case contains the two integers N and Q. 
The second line contains N-1 integers, describing the locked doors.
The i-th integer (starting from 1) is Di. 
Then, Q lines follow, describing the queries. 
The i-th of these lines contains the two integers Si and Ki.

*/
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{

    int testcases;
    cin >> testcases;
    cin.ignore();

    int testcase = 1;
    while ( testcase <= testcases)
    {
        vector<int> positions;
        string line;

        getline(cin, line);
        istringstream ss(line);
        int N, Q;
        ss >> N;  // # elements
        ss >> Q;  // # queries

        cout << N << " " << Q << endl;

        getline(cin, line);
        ss = istringstream(line);

        string word;
        vector<int> og_costs;
        while(ss >> word)
        {   
            std::string::size_type sz;
            int v = stoi(word, &sz);
            cout << v << " ";                  
            og_costs.push_back(v);
        }
        cout << endl;


        vector<int> known;

        while (Q > 0)
        {
            getline(cin, line);
            ss = istringstream(line);
            int S, K;
            ss >> S;
            ss >> K;
            cout << S << " " << K << endl;

            // remember to fill out info as query is being processed
            


            Q--;
        }




        // printing time
        cout << "Case: #" << testcase << ": ";
        for (auto it = positions.begin(); it != positions.end(); ++it)
        {
            cout << *it << " ";
        }
        cout << endl;
        testcase++;
    }
    return 0;
}