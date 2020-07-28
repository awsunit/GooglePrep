#include <iostream> 
#include <vector>
#include <map>
#include <queue>

using namespace std;


typedef pair<int, int> PAIR;

struct cmp {
    bool operator()(const PAIR &a, const PAIR &b)
    {
        return a.second < b.second;
    };
};


class Solution {
public:


    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> m;

        for (int i : nums)
        {
            m[i] += 1;
        }

        // make priority q
        // compare is based on map values
        priority_queue<PAIR, vector<PAIR>, cmp> q(m.begin(), m.end());

        // while (!q.empty()) 
        // {
        //     PAIR t = q.top();
        //     cout << t.first << ", " << t.second << endl;
        //     q.pop();
        // }
        vector<int> r;
        
        while (k-- > 0)
        {
            PAIR p = q.top();
            r.push_back(p.first);
            q.pop();
        }


        return r;
    }
};


int main()
{

    Solution s;

    int k = 2;

    vector<int> v = {1,1,1,2,2,3};
    vector<int> r = s.topKFrequent(v, k);
    for(int i : r)
    {
        cout << i << " ";
    }

    cout << endl;
    cout << "all done boss" << endl;
}