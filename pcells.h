/*
    There are 8 prison cells in a row, and each cell is 
    either occupied or vacant.

    Each day, whether the cell is occupied or vacant changes
    according to the following rules:

    If a cell has two adjacent neighbors that are 
    both occupied or both vacant, then the cell becomes occupied.

    Otherwise, it becomes vacant.

    (Note that because the prison is a row, 
    the first and the last cells in the row 
    can't have two adjacent neighbors.)
*/

#include <iostream>
#include <vector>

using std::vector;
using std::cout;
using std::endl;
using std::cin;

class Solution
{
public:

    vector<int> prisonAfterNDays(vector<int>& cells, int N)
    {
        // turn it into a reg array
        int tcells[8] = {}; 
        int ncells[8];
        int place = 0;
        for (auto it = cells.begin(); it != cells.end(); ++it)
        {
            cout << *it << ", ";
            tcells[place] = *it;
            place++;
        }
        cout << endl;
        while (N > 0)
        {
            // skip first & last somehow
            ncells[0] = 0;
            ncells[7] = 0;
            int prev = 0;
            auto next = 2;

            while (next < 8)
            {
                ncells[prev+1] = (tcells[prev] == tcells[next] ? 1 : 0);
                prev++;
                next++;
            }

            for (int i = 0; i < 8; i++)
            {
                // cout << ncells[i] << ", ";
                tcells[i] = ncells[i];
            }
            // cout << endl;
            N--;
        }
        vector<int> v (tcells, tcells + sizeof(tcells)/sizeof(int));
        return v;
    }  

    void silly(vector<int> v)
    {
        cout << "hi" << endl;
        // while (n > 0)
        // {
        //     n--;
        // }
        return;
    }  
};

        // while (N > 0)
        // {
        //     vector<int> temp = vector<int>();
        //     // iterate
        //     // skip first & last somehow
        //     temp.push_back(0);
        //     auto prev = cells.begin();
        //     auto next = cells.begin();
        //     next += 2;
        //     int count = 0;
        //     while(count < 6)
        //     {
        //         if (*prev == *next)
        //         {
        //             temp.push_back(1);
        //         } else {
        //             temp.push_back(0);
        //         } 
        //         prev++;
        //         next++;
        //         count++;
        //     }
        //     temp.push_back(0);
        //     int i = 0;
        //     for (auto it = temp.begin(); it != temp.end(); ++it)
        //     {
        //         // cout << *it << ", ";
        //         cells[i] = *it;
        //         i++;
        //     }
        //     // cout << endl;
        //     // temp.erase(temp.begin(), temp.end());
        //     N--;
        // }