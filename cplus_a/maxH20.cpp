#include <algorithm>
#include <map>
#include <vector>
#include <iostream> 

class Solution {
public:
    int maxArea1(std::vector<int>& height) {
        std::map<int, int> mappy;
        int size = height.size();
        
        for (int spot = 0;spot < size; spot++) {
            int currentHeight = height[spot];
            mappy.insert(std::pair<int, int>(spot, 0));
            for(int nextSpot = spot +1;nextSpot < size;nextSpot++) {
                int nextHeight = height[nextSpot];
                int area = std::min(currentHeight, nextHeight) * (nextSpot - spot);
                int greatestArea = mappy.at(spot);
                mappy[spot] = std::max(area, greatestArea);
            }
        }
        
        std::map<int,int>::iterator greatestArea = std::max_element(mappy.begin(), mappy.end(), [] (const std::pair<int, int>& a, const std::pair<int,int>& b) -> bool{return a.second < b.second;});
        
        return greatestArea->second;
    }

    int maxArea(std::vector<int>& heights) {
        int right = heights.size() - 1;
        int left = 0;
        int prevRightHeight = heights[right];
        int prevLeftHeight = heights[left];
        int maxArea = (right) * std::min(prevLeftHeight, prevRightHeight);

        // Loop Inv:
        //  heights at left and right have not been calculated/compared against maxArea
        // _ prevHL _ _ _ _ prevHR _ _ 
        while (left < right) {

            // need to check left and right separately
            int nextLeft = left + 1;
            int nextLeftHeight = heights[nextLeft];
            int area = (right - nextLeft) * std::min(nextLeftHeight, prevRightHeight);
            if (area > maxArea) {
                // left = nextLeft;
                prevLeftHeight = nextLeftHeight;
                maxArea = area;
            }
            int nextRight = right - 1;
            int nextRightHeight = heights[nextRight];
            area = (right - nextLeft) * std::min(nextRightHeight, prevLeftHeight);
            if (area > maxArea) {
                // right = nextRight;
                prevRightHeight = nextRightHeight;
                maxArea = area;
            }
            left++;
            right--;
        }

        return maxArea;
    }
};

int main(int argc, char *argv[]) {
    Solution s;
    // [1,8,6,2,5,4,8,25,7]
    // {1,8,6,2,5,4,8,3,7}
    int heights[] = {1,8,6,2,5,4,8,25,7};
    std::vector<int> v;
    v.assign(heights, heights + sizeof(heights)/sizeof(int));
    std::cout << "we have a max area of: " << s.maxArea(v) << std::endl;


    return 0;
}