public class KCountDown {
}





// k runs
//int curCountDown = K - 1;
//                for (int cur_int = 0; cur_int < N; ) {
//        int temp_l = cur_int;
//
//        while (curCountDown > 0 && temp_l + 1 < N && (Integer.parseInt(integers[temp_l]) - Integer.parseInt(integers[temp_l + 1]) == 1)) {
//        curCountDown--;
//        temp_l++;
//        }
//        cur_int++;
//        // way to avoid double counting here -> check the streak baby
//        if (curCountDown == 0) {
//        // initial score
//        kCountdowns++;
//        // temp is where we want it
//        while (temp_l + 1 < N ){
//        if (Integer.parseInt(integers[temp_l]) - Integer.parseInt(integers[temp_l + 1]) == 1) {
//        kCountdowns++;
//        temp_l++;
////                                cur_int++;
//        } else {
//        break;
//        }
//        }
//        cur_int = temp_l + 1;
//        }
//
//        curCountDown = K - 1;
//        }


// k runs end


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
