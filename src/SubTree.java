import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;

public class SubTree {

    static int count = 0;
    public static void main(String[] args) {
        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
        String input;

        System.out.println("Begin");
        try {
            // depth
            input = stdin.readLine();
            int depth = Integer.parseInt(input);

            if (depth == 0) {
                System.out.println("1");
            }

            ArrayList<Integer> list = new ArrayList<>();

            // read into arraylist
            //
            for (int i = 0; i < depth + 1; i++) {
                // next line
                input = stdin.readLine();
                String[] nums = input.split(" ");
                for (int num = 0; num < nums.length; num++) {
                    list.add(Integer.parseInt(nums[num]));
                }
            }

            // populate tree
            int[] tree = new int[list.size() + 1];
            Iterator<Integer> it = list.iterator();
            int num = 1;
            while(it.hasNext()) {
                tree[num] = it.next();
                num++;
            }

            // useful for recursion
            tree[0] = tree[1];
            int location = 1; // first child
            int parent_location = 0;  // initial

            recurse(location, parent_location, depth, tree);

            System.out.print(String.format("We found %d matching subtrees", count));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static boolean recurse(int location, int parent_location, int depth, int[] tree) {
        if (depth == 0) {
            return (tree[location] == tree[parent_location]) ? true : false;
        }
        int leftChildl = 2 * location;
        int rightChildl = leftChildl + 1;

        // must compute!!! java not greedy
        boolean l = recurse(leftChildl, location, depth - 1, tree);
        boolean r = recurse(rightChildl, location, depth - 1, tree);
        if (l && r) {
            count++;
            return (tree[location] == tree[parent_location]) ? true : false;
        }
        return false;
    }
}
