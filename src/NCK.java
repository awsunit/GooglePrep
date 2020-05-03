public class NCK {

    public static void main (String[] args) {
        int k = 3;
        int n = 5;
        int[] input = new int[]{0,1,2,3,4};
        int[] k_index = new int[]{0,1,2};

        // initial
        for (int i = 0; i < k; i++) {
            System.out.print(String.format("%d, ", input[k_index[i]]));
        }
        System.out.println();

        for (int cur_k = 0; cur_k < k_index.length; cur_k++) {
            int temp = k;
            while (temp < n){
                for (int i = 0; i < k; i++) {
                    if (i == cur_k){
                        System.out.print(input[temp] + ", ");
                    } else {
                        System.out.print(input[k_index[i]] + ", ");
                    }
                }
                System.out.println();
                temp++;
            }


        }


    }
}
