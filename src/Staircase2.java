// package src;

// On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

// Once you pay the cost, you can either climb one or two steps. You need to find minimum cost 
// to reach the top of the floor, and you can either start from the step with index 0, 
// or the step with index 1.

public class Staircase2 {
    public static void main(String[] args) {
        int[] c = {10, 15, 20};
        Staircase2 s = new Staircase2();

        System.out.print(s.minCostClimbingStairs(c));
    }
    public int minCostClimbingStairs(int[] cost) {
        int spot = 0;
        
        for (; spot < cost.length; spot++) {
            if (spot == 0 || spot == 1) {
                continue; // cheapest spot is just the val
            }
            int v = cost[spot];
            cost[spot] = Math.min(cost[spot - 1] + v, cost[spot - 2] + v);
        }

        return Math.min(cost[spot - 1], cost[spot - 2]);
    } 
    
}