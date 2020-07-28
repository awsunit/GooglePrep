/*
Li has planned a bike tour through the mountains of Switzerland. 
His tour consists of N checkpoints, numbered from 1 to N 
in the order he will visit them. 

The i-th checkpoint has a height of Hi.

A checkpoint is a peak if:
It is not the 1st checkpoint or the N-th checkpoint, and
The height of the checkpoint is strictly greater than the checkpoint
immediately before it and the checkpoint immediately after it.

Please help Li find out the number of peaks.

Input
The first line of the input gives the number of test cases, T. 
T test cases follow. 
Each test case begins with a line containing the integer N. 
The second line contains N integers. The i-th integer is Hi.
*/
#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
using namespace std;

int main ()
{
    string name = "rb_t.txt";
    // ifstream cin(name);

    int testcases;
    int testcase = 1;

    cin >> testcases;

    // std::cout << "testcases: " << testcases << endl;

    while (testcase <= testcases)
    {
        int N;
        cin >> N;
        cin.ignore();

        vector<int> peaks;
        string line, word;
        getline(cin, line);

        istringstream ss(line);

        while (ss >> word)
        {
            std::string::size_type sz;
            int V = stoi(word, &sz);   
            // std::cout << V;        
            peaks.push_back(V);
        }

        // std::cout << endl;

        int numpeaks = 0;
        for (int p = 0; p < peaks.size(); p++)
        {
            bool not_first_or_last = p != 0 && p != peaks.size() -1;
            bool checks = peaks[p] > peaks[p - 1] && peaks[p] > peaks[p+ 1];

            if (not_first_or_last && checks)
            {
                numpeaks++;
            }
        }

        std::cout << "Case #" << testcase << ": " << numpeaks << endl;
        testcase++;
    }

    return 0;
}