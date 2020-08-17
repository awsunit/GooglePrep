import java.util.HashSet;
import java.util.Set;

// Given a matrix consists of 0 and 1, 
// find the distance of the nearest 0 for each cell.

// The distance between two adjacent cells is 1.

class DistToZero {
    public int[][] updateMatrix(int[][] matrix) {
        
        HashSet<String> ones = new HashSet<>();
        Set<String> zeros = new HashSet<>();
        int[][] r = new int[matrix.length][matrix[0].length];
        int[][] directions = {{1,0}, {0, 1}, {-1,0}, {0,-1}};
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    zeros.add("" + i + j);
                } else {
                    ones.add("" + i + j);
                }
            }
        }

        while (ones.size() > 0) {
            Set<String> changed = new HashSet<>();

            for (String s : zeros) {
                int i = s.charAt(0) - '0';
                int j = s.charAt(1) - '0';

                for (int[] direction : directions) {
                    int ni = direction[0] + i;
                    int nj = direction[1] + j;

                    if (ones.contains("" + ni + nj)) {
                        ones.remove("" + ni + nj);
                        changed.add("" + ni + nj);
                    }
                }
            }
            if (changed.size() == 0) {
                return r;
            }
            zeros = changed;
        }
        return r;
    }
}