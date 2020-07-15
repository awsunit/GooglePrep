
import java.io.*;
import java.util.*;


public class Solution {
    public static void main(String[] args) {
//        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
        BufferedReader stdin = null;
        try {
            String path = "src/kCD.txt";
            FileInputStream fis = new FileInputStream(path);

            stdin = new BufferedReader(new InputStreamReader((fis)));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        Boolean k = true;
        String input;

        try {
            // test cases
            input = stdin.readLine();
            int numCases = Integer.parseInt(input);

            for (int testCase = 0; testCase < numCases; testCase++) {
                int kCountdowns = 0;

                input = stdin.readLine();
                String[] nk = input.split(" ");
                int N = Integer.parseInt(nk[0]);
                int K = Integer.parseInt(nk[1]);

                input = stdin.readLine();
                String[] integers = input.split(" ");

//                System.out.println(String.format("Checking out %d integers, for runs of %d", N, K));

                // base case is array of 1
                for (int cur_i = N - 1; cur_i >= 0; ) {

                    // find a one or what?
                    while (cur_i > 0 && Integer.parseInt(integers[cur_i]) != 1) {
                        cur_i--;
                    }
                    if (Integer.parseInt(integers[cur_i]) != 1) {
                        // odd check for case of index == 0
                        break;
                    }

                    int breakAtZero = K - 1;
                    cur_i--;
                    while (cur_i >= 0 && breakAtZero > 0 && Integer.parseInt(integers[cur_i]) - Integer.parseInt(integers[cur_i + 1]) == 1) {
                        breakAtZero--;
                        cur_i--;
                    }

                    if (breakAtZero == 0) {
                        kCountdowns++;
                    }
                }

                // comma here??
                System.out.println(String.format("Case #%d: %d", testCase + 1, kCountdowns));
            }

        } catch (IOException e) {

        }
    }
}
