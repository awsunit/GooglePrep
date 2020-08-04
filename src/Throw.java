class Throw {
    public int climbStairs(int n) {
        // 0th stair = 1
        // 2 stairs = 4th fib
        if (n < 1) {
            return 1;
        } 
        int t1 = 1;
        int t2 = 1;     
        // return 1 + recurse(n, 1);
        while (n-- > 0) {
            int sum = t1 + t2;
            t1 = t2;
            t2 = sum;
        }
        return t1;
    }
    
    public int recurse(int n, int stair) {
        if (stair >=  n) {
            return 0;
        }

        return 1 + recurse(n, stair + 1) + recurse(n, stair + 2);
        
    }


    public static void main (String[] args) {

        Throw t = new Throw();
        for (int i = 1; i < 15; i++) {
            System.out.println(t.climbStairs(i));
        }


    }
}