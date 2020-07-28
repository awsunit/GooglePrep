#include <iostream>
#include <vector>

using namespace std;



class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {

        int perimeter = 0;

        for (int row = 0; row < grid.size(); ++row)
        {
            vector<int> currow = grid[row];
            for (int col = 0; col < currow.size(); ++col)
            {
                if (currow[col] == 1)
                {
                    int val = 4;
                    // check out neighbors
                    // left
                    val -= (col != 0 && currow[col -1] == 1) ? 1 : 0;
                    // right
                    val -= (col != currow.size() - 1 && currow[col + 1] == 1) ? 1 : 0;
                    // top 
                    val -= (row != 0 && grid[row - 1][col] == 1) ? 1 : 0;
                    // bottom
                    val -= (row != grid.size() -1 && grid[row + 1][col] == 1) ? 1 : 0;

                    perimeter += val;
                }

            }
        }
        
    }
};

int main()
{




}