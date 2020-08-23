#include <vector>
#include <iostream>
#include <algorithm>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::string;
using std::min;

class Levenshtein {
public:
    void populateS1(vector<int>& m, string s1) 
    {
        for (int col = 1; col < s1.length() + 1; ++col) {
            m.at(col) = col;
            
        }
    }
    void populateS2(vector<vector<int>>& m, string s2) {
        int col = 0;
        for (int row = 1;row <= s2.length(); row++) {
            m.at(row).at(col) = row;

        }
    }
    void print(vector<vector<int>>& v) {
        cout << "here" << endl;
        for (auto outer: v) {
            for (auto inner: outer) {
                cout << inner << " ";
            }
            cout << endl;
        }
    }

    int distance(string s1, string s2) {
        int dist = 0;
        // get our matrix
        vector<vector<int>> m;
        for (int i = 0; i < s2.length() + 1; i++) {
            vector<int> v(s1.length() + 1, 0);
            m.push_back(v);
        }
        populateS1(m.at(0), s1);
        populateS2(m, s2);
        dist = calculate(s1, s2, m);
        return dist;
    }

    int calculate(string s1, string s2, vector<vector<int>>& m) {
        int dist = 0;

        for (int row = 1; row <= s2.length(); row++) {
            for (int col = 1; col <= s1.length(); col++) {
                int i = min(
                m.at(row - 1).at(col - 1),
                min(m.at(row).at(col - 1),
                m.at(row - 1).at(col))
                );
                int add = m.at(row-1).at(col-1) == i && 
                s1.at(col-1) == s2.at(row-1) ? 0 : 1;
                m.at(row).at(col) = add + i;           
            }
            
        }
        print(m);
        return m.at(s2.length()).at(s1.length());
    }
};

int main (int argc, char** argv) {
    Levenshtein l;
    int i = l.distance("honda", "hyundai");
    cout << i << endl;
    cout << "all done boss" << endl;
}