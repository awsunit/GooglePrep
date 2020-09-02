// You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

// 0 represents the obstacle can't be reached.
// 1 represents the ground can be walked through.
// The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
// In one step you can walk in any of the four directions top, bottom, left and right also when standing in a point 
// which is a tree you can decide whether or not to cut off the tree.

// You are asked to cut off all the trees in this forest in the order of tree's height - 
// always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

// You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. 
// If you can't cut off all the trees, output -1 in that situation.

// You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.
#include <vector>
#include <iostream>
#include <stdlib.h>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <map>
#include <algorithm>
#include <string>
#include <cctype>

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
class Solution {
public:
    int cutOffTree(vector<vector<int>>& forest) {
        // need to map tree positions 
        map<int, vector<int>> locations;
        map<int, vector<int>> banned;

        for (int v = 0; v < forest.size(); ++v) {
            for (int i = 0; i < forest.at(v).size(); ++i) {
                if (forest.at(v).at(i) > 1) {
                    locations[i] = {v, i};
                } else if (forest.at(v).at(i) == 0){
                    banned[i] = {v, i};
                }
            }
        }

        // start at lowest value found -> add cost to get there initially

        // iterate through map (already in order) calculating steps


        
    }
};