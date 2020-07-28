/*
    given string containing variable white space between words and on ends:
    reverse string s.t. whitespace is only between words
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iterator>


using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        istringstream ss(s);
        vector<string> results(istream_iterator<string>{ss},
                istream_iterator<string>());


        reverse(results.begin(), results.end());
        for (auto p : results)
        {
            cout << p << endl;
        }

        string r("");

        for (auto it = results.begin(); it != results.end(); )
        {
            string ov = *it;
            it++;
            r += ov;
            if (it != results.end())
            {
                r += " ";
            }
        }
        
        return r;
    }
};


int main()
{
    string line;
    getline(cin, line);
    cout << "given: " << line << endl;

    Solution s;
    string word = s.reverseWords(line);
    cout << (word) << endl;

    




    return 0;
}
