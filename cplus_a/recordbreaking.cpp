/*
    Isyana is given the number of visitors at her local theme park 
    on N consecutive days. The number of visitors on the i-th day is Vi. 
    A day is record breaking if it satisfies both of the following 
    conditions:
        The number of visitors on the day is strictly larger than 
        the number of visitors on each of the previous days.

        Either it is the last day, or the number of visitors on the 
        day is strictly larger than the number of visitors on the 
        following day.

        Note that the very first day could be a record breaking day!

Please help Isyana find out the number of record breaking days.
*/
#include <iostream>
#include <sstream>
#include <vector>
// #include <fstream>

using namespace std;

// int main()
// {

//     string name = "rb_t.txt";
//     // ifstream cin(name);

//     // # test cases
//     int testcases;
//     int curcase = 1;
//     cin >> testcases;

//     while (curcase <= testcases)
//     {
//         int days;  // N
//         int V;  // # visitors
//         int rbd = 0;  // number days
//         vector<int> record;

//         cin >> days;
//         cin.ignore();

//         // #days integers
//         string line;
//         string word;
//         getline(cin, line);

//         istringstream ss(line);

//         while(ss >> word)
//         {   
//             std::string::size_type sz;
//             V = stoi(word, &sz);           
//             record.push_back(V);
//         } 

//         int largest = 0;
//         for (auto outer = record.begin(); outer != record.end(); ++outer)
//         {
//             int cur = *outer;

//             if (cur <= largest) continue;

//             largest = cur;

//             auto temp = outer;
//             temp++;
//             if (temp != record.end() && (*temp >= cur)) continue;
//             rbd++; 
//         }
//         // 
//         cout << "Case #" + to_string(curcase) + ": " + to_string(rbd) << endl;
//         curcase++;
//     }

//     return 0;
// }


int main()
{

    string name = "rb_t.txt";
    // ifstream cin(name);

    // # test cases
    int testcases;
    int curcase = 1;
    cin >> testcases;

    while (curcase <= testcases)
    {
        int days;  // N
        int V;  // # visitors
        int rbd = 0;  // number days
        vector<int> record;

        cin >> days;
        cin.ignore();

        // #days integers
        string line;
        string word;
        getline(cin, line);

        istringstream ss(line);

        while(ss >> word)
        {   
            std::string::size_type sz;
            V = stoi(word, &sz);           
            record.push_back(V);
        } 
        for (auto outer = record.begin(); outer != record.end(); ++outer)
        {
            int cur = *outer;
            bool add = true;
            for (auto inner = record.begin(); 
                inner != outer && inner != record.end();
                ++inner)
            {
                // are we larger than
                if (*inner >= cur)
                {
                    // don't add
                    add = false;
                    break;
                }
            }

            if (!add) continue;
            auto temp = outer;
            temp++;
            if (temp != record.end() && (*temp >=  cur)) continue;
            rbd++;
        }

        cout << "Case #" + to_string(curcase) + ": " + to_string(rbd) << endl;
        curcase++;
    }

    return 0;
}
