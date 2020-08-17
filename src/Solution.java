// package src;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
* Implement the required functionality, classes, and logic.
*/

public class Solution {
    long a, c, m;
    long xn;
    String[] pairs = {"AA", "AT", "AC", "AG", "TA", "TT",
     "TC", "TG", "CA", "CT", "CC", "CG", "GA", "GT", "GC", "GG"};
    long[] percs = {6, 15, 22, 25, 29, 33, 43, 55, 67, 69, 74, 79, 
            86, 97, 98, 100};

    public Solution(long a, long xn, long c, long m) {
        this.a = a;
        this.xn = xn;
        this.c = c;
        this.m = m;
    }

    public long nxtV() {
        long i = 1;
        long v = ((this.a * this.xn) + this.c) & (long)((i << (long)Math.pow(2, 64)) - 1);
        long l = v % this.m;
     
        this.xn = l;
        return l;
    }
    public long get() {
        long x;
        long v;
        do {
            x = this.nxtV();
            v = this.m - (this.m % 100);
        }
        while (x > v);

        return x % 100;
    }
     public String getSequence(long length) {
        String sequence = "";
        for (int i = 0; i < length; i += 2) {
            long x = this.get();
            // slowwww
            for (int v = 0; v < percs.length; v++) {
                if (x < percs[v]) {
                    sequence += pairs[v];
                    break;
                }
            }
        }
        return sequence;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader stdin = 
            // new BufferedReader(new InputStreamReader(System.in));
            new BufferedReader(new InputStreamReader(new FileInputStream("src/TT_test.txt")));
               
        long S = Long.parseLong(stdin.readLine());
        long L = Long.parseLong(stdin.readLine());
        float Z = Float.parseFloat(stdin.readLine());
        Solution s = new Solution(0, 0, 0, 0);
        Organism o = s.new Organism(S, L, Z);
        System.out.println(o.getSequence().toLowerCase());
    }
    public class Organism {
        Solution s;
        long length;
        float Z;
        public Organism(long seed, long length, float Z) {
            this.s = new Solution((long)48271, seed, 0, (long)Math.pow(2, 32) - 1);
            this.length = length;
            this.Z = Z;
        }

        public String getSequence() {
            String sequence = "";
            Random rn = new Random();
            int Zi = (int)(this.Z  * 100);
            int Zj = (int) ((1-this.Z) * 100);

            for (int i = 0; i < length; i += 2) {
                long x = this.s.get();
                // slowwww
                String genes = "";
                for (int v = 0; v < percs.length; v++) {
                    if (x < this.s.percs[v]) {
                        genes = this.s.pairs[v];
                        break;
                    }
                }
                int p = rn.nextInt(Zi + Zj) + 1;
                if (p < Zi) {
                    int mutation = rn.nextInt(4);
                    if (mutation == 0) {
                        // switch my chars
                        sequence += genes.charAt(1);
                        sequence += genes.charAt(0);
                    } else if (mutation == 1) {
                        // put me at front
                        int k = rn.nextInt(100) + 1;
                        if (k + 1> sequence.length()) {
                            sequence = genes + sequence;
                        } else {
                            int spot = sequence.length() - (k + 1);
                            sequence = sequence.substring(0, spot) 
                                    + genes 
                                    + sequence.substring(spot + 2, sequence.length());
                        }
                    } else if (mutation == 2) {
                        // add more of me
                        
                        int k = rn.nextInt(10) + 1;
                        k++;
                        sequence += genes;
                        while (k-- > 0) {
                            sequence += genes;
                        }
                            
                    }
                    // == 3 -> do not add                    
                } else {
                    sequence += genes;
                }
            }
            return sequence;
        }

    }

}