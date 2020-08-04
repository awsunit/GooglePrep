/*
Apollo is playing a game involving polyominos. A polyomino is a shape made by joining together one or more squares edge to edge to form a single connected shape. 

The game involves combining N polyominos into a single rectangular shape without any holes. Each polyomino is labeled with a unique character from A to Z.

Apollo has finished the game and created a rectangular wall containing R rows and C columns. He took a picture and sent it to his friend Selene. 
Selene likes pictures of walls, but she likes them even more if they are stable walls. 

A wall is stable if it can be created by adding polyominos one at a time to the wall so that each polyomino is always supported. 

A polyomino is supported if each of its squares is either on the ground, or has another square below it.

Apollo would like to check if his wall is stable and if it is, prove that fact to Selene by telling her the order in which he added the polyominos.

example walls:

ZOAAMM
ZOAOMM
ZOOOOM
ZZZZOM

XXOO
XFFO
XFXO
XXXO

*/

import java.io.*;
import java.util.*;

public class StableWall {
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


            int R = Integer.parseInt(rc[0]);
            int C = Integer.parseInt(rc[1]);

            // dependencies 
            HashMap<Character,List<Character>> keyComesFirst = 
                        new HashMap<Character, List<Character>>();

            // counts of incoming vertices
            HashMap<Character,Integer> counts = new HashMap<>();

            
            // get first row
            String top = stdin.readLine();

            // what about the first row asshole
            top.chars().forEach(c -> counts.put((char)c,0));
            top.chars().forEach(c -> keyComesFirst.put((char) c, new ArrayList<Character>()));
  

            for (int row = 1; row < R; row++) {
                boolean brk = false;
                String bottom = stdin.readLine();
                for (int c = 0; c < bottom.length(); c++) {               
                    Character tc = top.charAt(c);
                    Character bc = bottom.charAt(c);
                    // check that top doesn't come before bottom
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


// // package src;
// import java.io.*;
// import java.util.*;

// // import jdk.internal.jline.internal.InputStreamReader;


// public class StableWall {
//     public static void main(String[] args) throws IOException {
//         BufferedReader stdin = 
//         // new BufferedReader(new InputStreamReader(System.in));
//         new BufferedReader(new InputStreamReader(new FileInputStream("src/test_stablewall.txt")));
    
//         String input;
//         input = stdin.readLine();
//         int testcases = Integer.parseInt(input);
//         int testcase = 1;

//         while (testcase <= testcases) {
//             String output = "yup";

//             String[] rc = stdin.readLine().split(" ");
//             for (String s: rc) {
//                 System.out.println(s);
//             }

//             int R = Integer.parseInt(rc[0]);
//             int C = Integer.parseInt(rc[1]);

//             // dependencies 
//             HashMap<Character,List<Character>> keyComesFirst = 
//                         new HashMap<Character, List<Character>>();

//             // counts of incoming vertices
//             HashMap<Character,Integer> counts = new HashMap<>();

//             // get first row
//             String top = stdin.readLine();
//             System.out.println("top " + top);
//             for (int row = 1; row < R; row++) {
//                 boolean brk = false;
//                 String bottom = stdin.readLine();
//                 for (int c = 0; c < bottom.length(); c++) {               
//                     Character tc = top.charAt(c);
//                     Character bc = bottom.charAt(c);
//                     // check that top doesn't come before bottom
//                     if (!keyComesFirst.containsKey(tc)) {
//                         // top doesn't come before anyone
//                         keyComesFirst.put(tc, new ArrayList<Character>());
//                     } else if (tc != bc && keyComesFirst.get(tc).contains(bc)) {
//                         // top is supposed to come before bottom -> fail
//                         brk = true;
//                         break;
//                     } else {
//                         List<Character> l;
//                         if (!keyComesFirst.containsKey(bc)){
//                             l = new ArrayList<Character>();
//                             keyComesFirst.put(bc, l);
//                         } else {
//                             l = keyComesFirst.get(bc);
//                         }
//                         l.add(tc);
//                     }
//                 }
//                 if (brk) {
//                     // get all input
//                     while (row++ < R - 1) {
//                         stdin.readLine();
//                     }
//                     output = "-1";
//                     break;
//                 }
//                 top = bottom;
//             }

//             System.out.println(String.format("Case #%d: %s", testcase, output));
//             testcase++;
//         }
    
//     }

// }