// package src;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.IntStream;

// In a given grid, each cell can have one of three values:

// the value 0 representing an empty cell;
// the value 1 representing a fresh orange;
// the value 2 representing a rotten orange.

// Every minute, any fresh orange that is adjacent (4-directionally) 
// to a rotten orange becomes rotten.

// Return the minimum number of minutes that must elapse until no cell
// has a fresh orange.  If this is impossible, return -1 instead.


class RottingOranges {
    public static int orangesRotting(int[][] grid) {
        // 
        Set<String> fresh = new HashSet<String>();
        Set<String> rotten = new HashSet<String>();
        int days = 0;
        for (int outer = 0; outer < grid.length; ++outer) {
            for (int inner = 0; inner < grid[0].length; ++inner) {
                    if (grid[outer][inner] == 2) {
                        rotten.add("" + outer + inner);
                    } else if (grid[outer][inner] == 1) {
                        fresh.add("" + outer + inner);
                    }
               }
        }
        int[][] directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

        // simulate fresh oranges becoming infected
        while (fresh.size() > 0) {
            Set<String> infected = new HashSet<>();

            for (String s : rotten) {
                int i = s.charAt(0) - '0';
                int j = s.charAt(1) - '0';

                for (int[] direction: directions) {
                    int ni = direction[0] + i;
                    int nj = direction[1] + j;
                    if (fresh.contains("" + ni + nj)) {
                        fresh.remove("" + ni + nj);
                        infected.add("" + ni + nj);
                    }
                }
            }
            if (infected.size() == 0) {
                return -1;
            }
            rotten = infected;
            days++;
        }
        
        return days;
    }

    public static void main(String[] args) {
        int[][] nd = {{2,1,1}, {1,1,0}, {0,1,1}};
        System.out.println(RottingOranges.orangesRotting(nd));
    }
}