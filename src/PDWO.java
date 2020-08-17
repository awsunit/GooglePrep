import java.util.Arrays;

// Given an array nums of n integers where n > 1,  

// return an array output such that output[i] is equal to 
// the product of all the elements of nums except nums[i].

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class PDWO {
    public static void main(String[] args) {
        PDWO p = new PDWO();
        int[] nums = {1,2,3,4};
        int[] r = p.productExceptSelf(nums);
        for (int i : r) {
            System.out.print(i + " ");
        }
    }
    public int[] productExceptSelf(int[] nums) {
        
        int[] ptn = new int[nums.length];
        int[] results = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                ptn[0] = nums[0];
            } else {
                ptn[i] = nums[i] * ptn[i - 1];
            }     
        }
        int brs = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i == nums.length - 1) {
                results[i] = ptn[i -1];
                brs = nums[i];
            } else if (i == 0) {
                results[i] = brs;
            } else {
                results[i] = ptn[i - 1] * brs;
                brs *= nums[i];
            }

        }
        return results;
    }
}