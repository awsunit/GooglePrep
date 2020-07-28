/*
The city of Circleburg has a large circular street with N 
consulates along it. 

The consulates are numbered 1, 2, ..., N in clockwise order.

Today G guests, numbered 1, 2, ..., G will drive along the circular 
street for M minutes. 

Each guest is either a clockwise guest (denoted by the character C)
 or an anti-clockwise guest (denoted by the character A).

The i-th guest starts at the consulate numbered Hi and at the end 
of each minute will drive to an adjacent consulate. 

The i-th guest starts at the j-th consulate. If that guest is:

    a clockwise guest, they will drive to the (j+1)-th consulate 
    (unless they are at the N-th consulate, then they will drive to the
    1st consulate).

    an anti-clockwise guest, they will drive to the (j-1)-th consulate 
    (unless they are at the 1st consulate, then they will drive to the
     N-th consulate).

Each consulate will only remember the guest that visited them last.
If there are multiple guests who visited last, then the consulate 
will remember all of those guests.

For each guest, determine how many consulates will remember them.

*/

#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <map>

using namespace std;



int main()
{
    int testcases, testcase = 1;
    string line;

    getline(cin, line);

    testcases = stoi(line);

    cout << " Starting with: " << testcases << " testcases" << endl;

    while (testcase <= testcases)
    {

        string word;
        int N, G, M;

        getline(cin, line);
        istringstream ss(line);
        ss >> word;
        N = stoi(word);
        ss >> word;
        G = stoi(word);
        ss >> word;
        M = stoi(word);

        // G lines follow
        int tg = G;

        // have a map of <int> -> list<pair<int, dir>>
        // where: 
        //      int == consulate location 
        // list contains pairs where:
        //      p.1 = id_visitor, p.2 = direction 
        map<int,vector<pair<int,char>>> cmap;

        while (tg <= G)
        {
            int consultate;
            char direction;
            // int, char
            getline(cin, line);
            ss = istringstream(line);
            ss >> word;
            consultate = stoi(word);
            ss >> direction;  // error?

            cout << "given char: " << direction << endl;

            // make pair, map to tg
            pair<int,char> p(consultate, direction);
            // this consultate already occupado?
            if (cmap.find(consultate) == cmap.end())
            {              
                vector<pair<int,char>> v;
                v.push_back(p);
                cmap[tg] = v;
            } else {
                // lump together
                cmap[tg].push_back(p);
            }
            tg++;
        }  // all visitors added to map

        while (M-- > 0)
        {
            map<int,vector<pair<int,char>>> nmap;
                       
        }
        
        // while (M-- > 0)
        // {
        //     // shift everyone
        //     map<int,vector<pair<int,char>>> nmap;
        // }
        
        testcase++;
    }


    // some known equations

    // take the initial value -> consultate, add 1
    
    // figure out slope, negative for a

    // if positive slope:
    //      want to make our addition negative

    // if negative slope:
    //      


    return 0;
}
