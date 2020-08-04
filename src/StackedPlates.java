import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// In order to tackle this test set, we use Dynamic Programming along with some precomputation.

// First, let's consider an intermediate state dp[i][j] which denotes the maximum sum that can be obtained using the first i stacks 
// when we need to pick j plates in total. 

// Therefore, dp[N][P] would give us the maximum sum using the first N stacks if we need to pick P plates in total. 
// In order to compute dp[][] efficiently, we need to be able to efficiently answer the question: 
// What is the sum of the first x plates from stack i? We can precompute this once for all N stacks. 

// Let sum[i][x] denote the sum of first x plates from stack i.

// Next, we iterate over the stacks and try to answer the question: 
// What is the maximum sum if we had to pick j plates in total using the i stacks we've seen so far? 

// This would give us dp[i][j]. However, we need to also decide, among those j plates, how many come from the i-th stack?
// i.e., Let's say we pick x plates from the i-th stack, then dp[i][j] = max(dp[i][j], sum[i][x]+dp[i-1][j-x]). 

// Therefore, in order to pick j plates in total from i stacks, we can pick anywhere between [0, 1, ..., j] plates from the i-th stack
//  and [j, j-1, ..., 0] plates from the previous i-1 stacks respectively. 
//  Also, we need to do this for all values of 1 ≤ j ≤ P.

// for i [1, N]:
//  for j [0, P]:
//   dp[i][j] := 0
//    for x [0, min(j, K)]:
//     dp[i][j] = max(dp[i][j], sum[i][x]+dp[i-1][j-x])


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
                int P = Integer.parseInt(sv[2]);  // # plates to take

                int[][] dp = new int[N+1][P + 1];

                int[][] sum = new int[N+1][K];

                // make sum

                for (int stack = 1; stack < N + 1; stack++) {
                    for (int vspot = 0; vspot <= P; vspot++) {
                        dp[stack][vspot] = 0;
                        for (int x = 0; x < Math.min(vspot, K); x++) {
                            dp[stack][vspot] = Math.max(dp[stack][vspot], sum[stack][x] + dp[stack - 1][vspot - x]);
                        }
                    }
                }

                for (int[] row : dp) {
                    for (int c: row) {
                        System.out.print(c + " ");
                    }
                    System.out.println();
                }


                

                System.out.println(String.format("Case #%d, %d", i, total));
            }
        } catch (IOException e){

        }

    }
}
