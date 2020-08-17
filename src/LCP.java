// package src;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;

class LCP {

    /*
     * Complete the 'autocomplete' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts STRING_ARRAY command as parameter.
     */

    public static List<Integer> autocomplete(List<String> command) {
        // return list, HashMap<prefix, locations>, prefix location
        ArrayList<Integer> rl = new ArrayList<>();
        HashMap<String, Integer> hm = new HashMap<>();
        int location = 0;

        // Directed Graph via HashMap -> Currently too slow
        // Attempted:
        //      modify for-loop to start with largest substring and stop when LCP found
        // Problem:
        //      need to iterate over every char to ensure full reprsentation of graph
        
        for (int c = 0; c < command.size(); c++) { 
            String cur_com = command.get(c);
            int prev_loc = c;  // default to current string
            String sub = "";
            for (int cur_char = 0; cur_char < cur_com.length(); cur_char++) {
                sub += cur_com.charAt(cur_char);
                Integer pq;
                if ((pq = hm.get(sub)) != null) {
                    // get max then append
                    prev_loc = pq + 1;              
                } 
                hm.put(sub, location);
                // else {
                //     // create mapping for this particular substring
                    
                //     hm.put(sub, location);
                // }
                // // add our current location
                // pq.add(location);
            }
            rl.add(prev_loc);
            location += 1;
        }
        return rl;
    }
        public static void main(String[] args) {
        List<String> l = Arrays.asList("000", "1110", "01", "001", "110", "11");
        List<Integer> rl = autocomplete(l);
        rl.forEach(System.out::println);
    }

}


// class LCP {

//     /*
//      * Complete the 'autocomplete' function below.
//      *
//      * The function is expected to return an INTEGER_ARRAY.
//      * The function accepts STRING_ARRAY command as parameter.
//      */

//     public static List<Integer> autocomplete(List<String> command) {
//         // return list, HashMap<prefix, locations>, prefix location
//         ArrayList<Integer> rl = new ArrayList<>();
//         HashMap<String, PriorityQueue<Integer>> hm = new HashMap<>();
//         int location = 0;

//         // Directed Graph via HashMap -> Currently too slow
//         // Attempted:
//         //      modify for-loop to start with largest substring and stop when LCP found
//         // Problem:
//         //      need to iterate over every char to ensure full reprsentation of graph
        
//         for (int c = 0; c < command.size(); c++) { 
//             String cur_com = command.get(c);
//             int prev_loc = c;  // default to current string
//             String sub = "";
//             for (int cur_char = 0; cur_char < cur_com.length(); cur_char++) {
//                 sub += cur_com.charAt(cur_char);
//                 PriorityQueue<Integer> pq;
//                 if ((pq = hm.get(sub)) != null) {
//                     // get max then append
//                     prev_loc = pq.peek() + 1;              
//                 } else {
//                     // create mapping for this particular substring
//                     pq = new PriorityQueue<>((Integer i1, Integer i2) ->
//                             -i1.compareTo(i2));
//                     hm.put(sub, pq);
//                 }
//                 // add our current location
//                 pq.add(location);
//             }
//             rl.add(prev_loc);
//             location += 1;
//         }
//         return rl;
//     }
//         public static void main(String[] args) {
//         List<String> l = Arrays.asList("000", "1110", "01", "001", "110", "11");
//         List<Integer> rl = autocomplete(l);
//         rl.forEach(System.out::println);
//     }
    
// // }

// }
