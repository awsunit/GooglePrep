
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Solution {
    public static void main(String[] args) {
        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
        Boolean k = true;
        String input;

        try {
            // test cases
            input = stdin.readLine();
            int numCases = Integer.parseInt(input);

            for (int i = 0; i < numCases; i++) {
                stdin.readLine();

                input = stdin.readLine();
                int numItems = Integer.parseInt(input);

                Map<String, List<Integer>> map = new HashMap<String, List<Integer>>();

                for (int item = 0; item < numItems; item++) {
                    input = stdin.readLine();
                    String[] pair = input.split(" ");
                    String name = pair[0];
                    int price = Integer.parseInt(pair[1]);

                    if (map.containsKey(name)) {
                        List<Integer> entry = map.remove(name);
                        entry.add(price);
                        map.put(name, entry);
                    } else {
                        ArrayList<Integer> list = new ArrayList<Integer>();
                        list.add(price);
                        map.put(name, list);
                    }
                }
                System.out.println(String.format("Case #%d: ", i + 1));

                for (Map.Entry<String, List<Integer>> e : map.entrySet()) {
                    String curItem = e.getKey();
                    List<Integer> prices = e.getValue();
                    Collections.sort(prices);

                    int size = prices.size();
                    int lowest = prices.get(0);
                    int highest = prices.get(size - 1);
                    int sum = 0;
                    for (Integer p : prices) {
                        sum += p;
                    }
                    int avg = sum / size;
                    System.out.println(String.format("%s %d %d %d", curItem, lowest, highest, avg));
                }
            }


        } catch (IOException e) {

        }


    }
}



//
//    public static void main (String[] args) {
//        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
//
//        String input;
//
//        try {
//            // test cases
//            input = stdin.readLine();
//            int cases = Integer.parseInt(input);
//
//            for (int i = 0; i < cases; i++) {
//
//                // N & B
//                input = stdin.readLine();
//                String[] nb = input.split(" ");
//                int N = Integer.parseInt(nb[0]);
//                int B = Integer.parseInt(nb[1]);
//
//                // prices
//                input = stdin.readLine();
//                String[] sprices = input.split(" ");
//
//                // O(NLogN)
//                PriorityQueue<Integer> prices = new PriorityQueue<Integer>();
//                for (int price = 0; price < sprices.length; price++) {
//                    prices.add(Integer.parseInt(sprices[price]));
//                }
//
//                int sum = 0;
//                int canBuy = 0;
//                while (true) {
//                    int temp = sum + prices.remove();
//                    if (temp > B) break;
//                    sum = temp;
//                    canBuy++;
//                }
//
//                System.out.println(String.format("Case #%d: %d", i + 1, canBuy));
//            }
//        } catch (IOException e) {
//            //
//        }
//    }
//}
