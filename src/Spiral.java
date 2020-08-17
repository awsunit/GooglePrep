// package src;


class Spiral {
    enum DIRECTION {
          NORTH, SOUTH, EAST, WEST  
    }

    public static void main(String[] args) {
        Spiral s = new Spiral();
        int[][] ss = s.generateMatrix(2);

        for (int[] r : ss) {
            for (int i : r) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }
    public int[][] generateMatrix(int n) {
        
        // center of n X n matrix 
        int row = n/2;
        int col = n/2;
        int[][] result = new int[n][n];

        // bounds of iteration
        
        DIRECTION[] directions = 
            {DIRECTION.SOUTH, DIRECTION.NORTH};
        int direction = 0;
        int num_adding = 0;


        // for 2 times
        // go direction for 2*num_adding + 1
        // turn left


        for (int val = n*n; val >= 1;) {
            // go direction 2 * num_adding + 1
            int going = (num_adding == 0) ? 1 : (2 * num_adding);
            int t = going;
            if (directions[direction].equals(DIRECTION.SOUTH)) {           
                while (going-- > 0 && val >= 1) {
                    result[row][col--] = val--;
                }
                while (t-- > 0 && val >= 1) {
                    result[row++][col] = val--;
                }
                if (row == n) row = n - 1;
            } else {
                while (going-- > 0 && val >= 1 && col < n) {
                    result[row][col++] = val--;
                }
                while (t-- > 0 && val >= 1) {
                    result[row--][col] = val--;
                }
            } 
            num_adding += 1;
            direction = (direction + 1) % 2;
        }
        return result;
    }
}