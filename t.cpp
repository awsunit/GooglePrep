#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>

using namespace std;

int main()
{

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

        int best = 0;
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

            // if (!(cur > best)) continue;
            if (!(add)) continue;
            best = cur;
            auto temp = outer;
            temp++;
            if (temp != record.end() && !(cur > *temp)) continue;
            rbd++;
        }
        cout << "Case #" + to_string(curcase) + ": " + to_string(rbd) << endl;
        curcase++;
    }



    return 0;
}