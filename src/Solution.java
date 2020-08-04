// package src;
import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader stdin = 
        // new BufferedReader(new InputStreamReader(System.in));
        new BufferedReader(new InputStreamReader(new FileInputStream("src/test_stablewall.txt")));
    
        String input;
        input = stdin.readLine();
        int testcases = Integer.parseInt(input);
        int testcase = 1;

        while (testcase <= testcases) {
            String output = "";

            String[] rc = stdin.readLine().split(" ");
            for (String s: rc) {
                System.out.println(s);
            }

            int R = Integer.parseInt(rc[0]);
            int C = Integer.parseInt(rc[1]);

            // dependencies 
            HashMap<Character,List<Character>> keyComesFirst = 
                        new HashMap<Character, List<Character>>();

            // counts of incoming vertices
            HashMap<Character,Integer> counts = new HashMap<>();

            // get first row
            String top = stdin.readLine();

            for (int row = 1; row < R; row++) {
                
                String bottom = stdin.readLine();
                for (int c = 0; c < bottom.length(); c++) {               
 
                    Character tc = top.charAt(c);
                    Character bc = bottom.charAt(c);

                    keyComesFirst.computeIfAbsent(tc, x -> new ArrayList<Character>());
                    keyComesFirst.computeIfAbsent(bc, x -> new ArrayList<Character>());

                    // bc must come before tc
                    if (tc != bc) {
                        keyComesFirst.get(bc).add(tc);
                        // incoming vertices for tc
                        counts.computeIfAbsent(bc, x -> 0);
                        counts.computeIfAbsent(tc, x -> 0);
                        int i = counts.get(tc);
                        counts.put(tc, i + 1);
                    }

            }
                top = bottom;
            }

            // okay counts and dependencies are finished
            // DBS needs a stack
            Stack<Character> stk = new Stack<>();
            counts.forEach((k,v) -> {
                if (v == 0) {
                    stk.push(k);
                }
            });

            // keep going till the end buddy
            while (!stk.empty()) {
                Character c = stk.pop();
                output += c;
                // decrease our inherited bitches
                List<Character> children = keyComesFirst.get(c);
                children.forEach(ch -> {
                    int cnt = counts.get(ch);
                    cnt -= 1;
                    counts.put(ch, cnt);
                    if (cnt == 0) {
                        stk.push(ch);
                    }
                    
                });
            }

            if (output.length() != counts.keySet().size()) {
                // not every key was found
                output = "-1";
            }

            System.out.println(String.format("Case #%d: %s", testcase, output));
            testcase++;
        }
    
    }

}





//OLD below


// import java.io.*;
// import java.util.*;


// public class Solution {
//     public static void main(String[] args) {
// //        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
//         BufferedReader stdin = null;
//         try {
//             String path = "src/kCD.txt";
//             FileInputStream fis = new FileInputStream(path);
//             stdin = new BufferedReader(new FileReader(path));
//             // stdin = new BufferedReader(new InputStreamReader((fis)));
//         } catch (FileNotFoundException e) {
//             e.printStackTrace();
//         }

//         Boolean k = true;
//         String input;

//         try {
//             System.out.println("bye");
//             // test cases
//             input = stdin.readLine();
//             int numCases = Integer.parseInt(input);

//             for (int testCase = 0; testCase < numCases; testCase++) {
//                 int kCountdowns = 0;

//                 input = stdin.readLine();
//                 String[] nk = input.split(" ");
//                 int N = Integer.parseInt(nk[0]);
//                 int K = Integer.parseInt(nk[1]);

//                 input = stdin.readLine();
//                 String[] integers = input.split(" ");

// //                System.out.println(String.format("Checking out %d integers, for runs of %d", N, K));

//                 // base case is array of 1
//                 for (int cur_i = N - 1; cur_i >= 0; ) {

//                     // find a one or what?
//                     while (cur_i > 0 && Integer.parseInt(integers[cur_i]) != 1) {
//                         cur_i--;
//                     }
//                     if (Integer.parseInt(integers[cur_i]) != 1) {
//                         // odd check for case of index == 0
//                         break;
//                     }

//                     int breakAtZero = K - 1;
//                     cur_i--;
//                     while (cur_i >= 0 && breakAtZero > 0 && Integer.parseInt(integers[cur_i]) - Integer.parseInt(integers[cur_i + 1]) == 1) {
//                         breakAtZero--;
//                         cur_i--;
//                     }

//                     if (breakAtZero == 0) {
//                         kCountdowns++;
//                     }
//                 }

//                 // comma here??
//                 System.out.println(String.format("Case #%d: %d", testCase + 1, kCountdowns));
//             }

//         } catch (IOException e) {

//         }
//     }
// }
