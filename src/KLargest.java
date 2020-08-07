// package src;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class KLargest {
    public static List<Integer> recurse(int[] nums, int start, int end, int k, boolean going_left) {
        // end never included
        if (end - start < 1) {
            return new ArrayList<Integer>();
        }
        if (end - start == 1) {
            // base case
            return new ArrayList<Integer>(Arrays.asList(nums[start]));
        }

        // get middle
        int mid = (end + start)/2;
        List<Integer> l = recurse(nums, start, mid, k, true);

        l.add(nums[mid]);
        l.addAll(recurse(nums, mid + 1, end, k, false));
        if (l.size() >= k) {
            l.sort((Integer i1, Integer i2) -> -i1.compareTo(i2));
            return l.subList(0, k);
        }
        return l;
    }
    public static int findKthLargest(int[] nums, int k) {
        // divide and conquer 

        return recurse(nums, 0, nums.length, k, false).get(k-1);


        //  works!
        // PriorityQueue<Integer> pq = new PriorityQueue<>(
        //     (Integer i1, Integer i2) -> -(i1.compareTo(i2))
        // );
        // for (int i : nums) {
        //     pq.add(i);
        // }
        // int i = k;
        
        // while (i-- > 1) {
        //     pq.remove();
        // }
        // return pq.remove();
    }

    public static void main(String[] args) {
        int[] l = new int[]{3,2,1,5,6,4};
        System.out.println(findKthLargest(l, 2));
    }

}                                   