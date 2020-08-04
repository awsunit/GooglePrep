// package src;
/*
    Given an integer array nums, find the contiguous subarray 
    (containing at least one number) which has the largest sum and 
    return its sum.
*/



import java.util.stream.Stream;
import java.util.function.*;

class MaxSubr
{
    public static int maxSubAarray(int[] arr)
    {
        // there exists an O(n) solution
        int maxine = 0;
        int start = 0;
        int end = 0;
        // there exists a functional way of doing the following:
        maxine += arr[0];
        int sfS = maxine;
        for (int i = 1; i < arr.length; i++)
        {
            int cur = arr[i];
            int temp = sfS + cur;


            if (temp > maxine) {
                if (cur > temp && cur > maxine) {
                    // better alone?
                    maxine = cur;
                    sfS = cur;
                } else {
                    // new max
                    maxine = temp;
                    sfS = temp;               
                }
            } else if (cur > maxine) {
                // alone be best
                maxine = cur;
                sfS = cur;
            } else if (cur > temp && cur > 0) {
                // start over -> NOT greater than maxine
                sfS = cur;
            } else {
                // keep summing
                sfS = temp;
            }

        }

        return maxine;
    }

    public static void main (String[] args)
    {
        int[] r = new int[]{-2,-1};
        System.out.println(maxSubAarray(r));

        r = new int[]{-1,-2};
        System.out.println(maxSubAarray(r));

        r = new int[]{1,1};
        System.out.println(maxSubAarray(r));

        r = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(maxSubAarray(r));

        r = new int[]{8,-19,5,-4,20};
        System.out.println(maxSubAarray(r));
    }

    public static void main() {
        System.out.println("Hi");
    }
}