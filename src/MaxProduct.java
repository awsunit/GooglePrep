import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.BinaryOperator;
import java.util.stream.IntStream;

public class MaxProduct {
    public static void main(String[] args) {
        IntStream is = IntStream.rangeClosed(1, 2);
 
        int x1 = -1;
        int x2 = -1;
        MaxProduct mp = new MaxProduct();
        In i = mp.new In();
        int ii = is.reduce(0,mp.new In()::apply); 
        System.out.println("we have a: " + ii);
    }

    public class In implements BinaryOperator<Integer> {

        @Override
        public Integer apply(Integer t, Integer u) {

            return t + u;
        }

    }
}