// package src;
import java.io.*;
import java.util.*;

public class TT {

    int a, c, m;
    long xn;

    public TT(int a, long xn, int c, int m) {
        this.a = a;
        this.xn = xn;
        this.c = c;
        this.m = m;
    }

    public long nxtV() {
        long l = ((this.a * this.xn) + this.c) % this.m;
        l = l & ((1 << (long)Math.pow(2, 64)) - 1);
        this.xn = l;
        return l;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader stdin = 
            // new BufferedReader(new InputStreamReader(System.in));
            new BufferedReader(new InputStreamReader(new FileInputStream("src/TT_test.txt")));


        String input;
        input = stdin.readLine();
        int entries = Integer.parseInt(input);
        int entry= 1;

        int a = Integer.parseInt(stdin.readLine());
        long xn = Long.parseLong(stdin.readLine());
        int c = Integer.parseInt(stdin.readLine());
        int m = Integer.parseInt(stdin.readLine());

        TT tt = new TT(a, xn, c, m);

        while (entry++ <= entries) {
            System.out.print(tt.nxtV() + " ");
        }
    }
    
}