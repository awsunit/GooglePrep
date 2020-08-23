
#include <vector>
#include <iostream>
#include <queue>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <map>

using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::priority_queue;
using std::string;
using std::unordered_map;
using std::pair;
using std::unordered_set;
using std::set;
using std::map;


int main () {
    vector<vector<int>> sets;
    vector<int> empty;
    sets.push_back(empty);

    // iterating over range
    // could be elements
    for (int num = 1; num <= 3; num++) {
        vector<vector<int>> nxtsets;
        for (auto v: sets) {
            vector<int> vi = v;
            vi.push_back(num);
            nxtsets.push_back(vi);
        }
        sets.insert(sets.end(), nxtsets.begin(), nxtsets.end());
    }
    for (auto v : sets) {
        for (auto i : v) {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}