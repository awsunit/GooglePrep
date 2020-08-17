// package src;

import java.util.ArrayList;

// Say you have an array for which the ith element is the price of a given stock on day i.

// If you were only permitted to complete at most one transaction 
// (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

// Note that you cannot sell a stock before you buy one.

class WhenBS{
    public static void main(String[] args) {
        WhenBS w = new WhenBS();
        int[] prices = {7,1,5,3,6,4};
        // int[] prices = {7,6,4,3,1};
        System.out.println(w.maxProfit(prices));
    }
    public int maxProfit(int[] prices) {
        ArrayList<Integer> l = new ArrayList<Integer>(prices.length);
        // int[] if_we_started_here = new int[prices.length];
        
        for (int loc = 0; loc < prices.length; loc++){
            l.add(loc, 0);
            // what is the best price we can get for starting here
            for (int inner = loc + 1; inner < prices.length; inner++) {
                int v = prices[inner] - prices[loc];
                if (v > l.get(loc)) {
                    l.set(loc, v);
                }
            }
        }

        return l.stream().max((x1, x2) -> x1.compareTo(x2)).get();
    }
}