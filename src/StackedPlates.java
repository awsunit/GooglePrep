import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class StackedPlates {

    public static void main(String[] args) {
        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));

        try {
            String input = stdin.readLine();

            int cases = Integer.parseInt(input);

            for(int i = 0; i < cases; i++) {
                int total = 0;

                input = stdin.readLine();
                // N, K, P
                String[] sv = input.split(" ");
                int N = Integer.parseInt(sv[0]);  // # stacks
                int K = Integer.parseInt(sv[1]);  // # plates/stack
                int P = Integer.parseInt(sv[2]);  // limit





                // misunderstood question code
//                for (int stack = 0; stack < N; stack++) {
//                    int temp = 0;
//                    // get stack, k plates
//                    input = stdin.readLine();
//                    String[] plates = input.split(" ");
//                    int plate = 0;
//                    while (plate < P && plate < K) {
//                        // plate value
//                        temp += Integer.parseInt(plates[plate]);
//                        plate++;
//                    }
//                    if (temp > total) {
//                        total = temp;
//                    }
//                }
                System.out.println(String.format("Case #%d, %d", i, total));
            }
        } catch (IOException e){

        }

    }
}
