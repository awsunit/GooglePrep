// Given a paragraph and a list of banned words, 

// return the most frequent word that is not in the list of banned words.  

// It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

// Words in the list of banned words are given in lowercase, and free of punctuation.  
// Words in the paragraph are not case sensitive.  The answer is in lowercase.

// hey google
#include <vector>
#include <iostream>
#include <stdlib.h>
#include <set>
#include <map>

#include <sstream>
#include <map>
#include <algorithm>
#include <string>
#include <cctype>
#include <regex>

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
using std::reverse;
using std::max_element;
using std::regex;

class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        // break up paragraph
        istringstream ss(paragraph);
        string word;

        // use a set for faster access time -> wrong??
        set<string> sbanned;
        for (string &s : banned) {
            sbanned.insert(s);
        }

        
        map<string, int> m;
        using pair_type = decltype(m)::value_type;
        while(ss >> word) {
            transform(word.begin(), word.end(), 
                    word.begin(),  
                [](unsigned char c) {
                    return std::tolower(c);
                });
                regex rgx("[^a-z ]");
                word = std::regex_replace(word, rgx, "");
                // cout << word << endl;
            if (sbanned.find(word) == sbanned.end()){
                m[word]++;
            }
        }
        // map word.lowercase -> count
        auto pr = max_element(m.begin(), m.end(),
            [](const pair_type &p1, const pair_type &p2){
                return p1.second < p2.second;
            });
        cout << pr->first << ", " << pr->second << endl;
        // return max count
        return pr->first;
    }
};

int main () {

    Solution s;
    string p("this. is. a. paragraph. Paragraph and and");
    // regex r("[^a-z ]");
    // p = std::regex_replace(p, r, "");
    // cout << p << endl;
    vector<string> banned = {"and"};
    cout << s.mostCommonWord(p, banned) << endl;

    return 0;
}