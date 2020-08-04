
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class NumHouses {
    public static void main (String[] args) {
        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));

        String input;

        try {
            // test cases
            input = stdin.readLine();
            int cases = Integer.parseInt(input);

            for (int i = 0; i < cases; i++) {

                // N & B
                input = stdin.readLine();
                String[] nb = input.split(" ");
                int N = Integer.parseInt(nb[0]);
                int B = Integer.parseInt(nb[1]);

                // prices
                input = stdin.readLine();
                String[] sprices = input.split(" ");

                // O(NLogN)
                PriorityQueue<Integer> prices = new PriorityQueue<Integer>();
                for (int price = 0; price < sprices.length; price++) {
                    prices.add(Integer.parseInt(sprices[price]));
                }

                int sum = 0;
                int canBuy = 0;
                while (true) {
                    int temp = sum + prices.remove();
                    if (temp > B) break;
                    sum = temp;
                    canBuy++;
                }

                System.out.println(String.format("Case #%d: %d", i + 1, canBuy));
            }
        } catch (IOException e) {
            //
        }
    }
}