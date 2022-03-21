import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.Iterator;
import java.util.stream.Collectors;

class Solution1 {
    public static int game(List<Integer> p) {
        // WRITE YOUR BRILLIANT CODE HERE
        
        List<Integer> totals = new ArrayList<Integer>();
        
        Iterator<Integer> currentProbability = p.iterator();
        Integer runningSum = 0;
        while (currentProbability.hasNext()) {
            Integer probability = currentProbability.next();
            runningSum += probability == 0 ? -1 : 1;
            totals.add(runningSum);
        }    
        
        
        // compare vs k and  n - k
        Integer bestScore = 0;
        Integer totalsSize = totals.size();
        Integer finalTotal = totals.get(totalsSize-1);
        
        // edge case
        List<Integer> sorted = new ArrayList<Integer>(totals);
        Collections.sort(sorted);
        if (bestScore > sorted.get(sorted.size() -1) && bestScore > finalTotal) return 0;
        
        for (int spot = 0;spot < totalsSize;spot++) {

            // we need the running sum from the first task up to, including this one -> totals
            Integer currentTotal = totals.get(spot);
            Integer nMinusKTotal = finalTotal - currentTotal;
            
            if (currentTotal > nMinusKTotal) return spot;
        }
        
        return totalsSize;
    }

    public static List<String> splitWords(String s) {
        return s.isEmpty() ? List.of() : Arrays.asList(s.split(" "));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Integer> p = splitWords(scanner.nextLine()).stream().map(Integer::parseInt).collect(Collectors.toList());
        scanner.close();
        int res = game(p);
        System.out.println(res);
    }
}