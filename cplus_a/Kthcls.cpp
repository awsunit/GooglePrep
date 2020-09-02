// Design a class to find the kth largest element in a stream. 

// Note that it is the kth largest element in the sorted order, not the kth distinct element.

// Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, 
// which contains initial elements from the stream. 

// For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
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
class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : k_(k), kth(0), ks(k, 0){
        
        
        // get our first k items
        for (int k_i = 0; k_i < k; k_i++) {
            ks.push_back(nums.at(0));
            nums.erase(nums.begin());
        }
        
        for (int k_i = 0; k_i < nums.size(); k_i++) {
            int i = 0;
            while (i < ks.size() && ks.at(i) < nums.at(k_i)) {
                i++;
            }
            if (i != 0) {
                ks.at(i - 1) = nums.at(k_i);
            }
        }
        
    }
    
    int add(int val) {
        for (int k_i = 0; k_i < nums.size(); k_i++) {
            int i = 0;
            while (i < ks.size() && ks.at(i) < nums.at(k_i)) {
                i++;
            }
            if (i != 0) {
                ks.at(i - 1) = nums.at(k_i);
            }
        }
        return 0;
    }
private:
    int k_;
    int kth;
    vector<int> ks;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */