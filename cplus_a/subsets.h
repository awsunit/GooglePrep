#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::cin;
using std::vector;

class Solution
{
public:

    vector<vector<int>> subsets(vector<int>& nums)
    {
        vector<vector<int>> sets;
        sets.push_back(vector<int>()); // emtpy set

        for (auto it = nums.begin(); it != nums.end(); ++it)
        {
            vector<vector<int>> t_sets;
            // add ourselves to every set already in existence
            for (auto c_set = sets.begin(); c_set != sets.end(); ++c_set)
            {
                t_sets.push_back(*c_set);  // add the current subset -> not including cur val
                vector<int> old_set = *c_set; // copy?
                old_set.push_back(*it);  // add current val
                t_sets.push_back(old_set);

            }
            // add just ourselves as a singleton set -> NO, handled 
            sets = t_sets;
        }
        return sets;
    }

};


        // vector<vector<int>> rv;

        // // empty set
        // rv.push_back(vector<int>());
        
        // int left_bumper = 0;

        // while (left_bumper < nums.size())
        // {

        //     // handle singleton
        //     vector<int> v(nums.size(), 0);
        //     v[left_bumper] = 1;
        //     vector<int> singleton = {v[left_bumper]};
        //     rv.push_back(singleton);

        //     int l2f = left_bumper;
        //     while (l2f > 0)
        //     {
        //         int spot = left_bumper - l2f;

        //         while (spot < left_bumper)
        //         {
        //             // walk the dog -> not yet!!!!!!!
        //             v[spot] = 1;
        //             // push the new vector
        //             vector<int> t;
        //             for (int i = 0; i < v.size(); ++i)
        //             {
        //                 if (v[i] != 0)
        //                 {
        //                     t.push_back(v[i]);
        //                 }
        //             }
        //             rv.push_back(t);
        //             // reset, increment
        //             v[spot] = 0;
        //             spot++;
        //         }    

        //         // fill spot
        //         v[left_bumper - l2f] = 1;
        //         l2f--;
        //     }
        //     left_bumper++;
        // }