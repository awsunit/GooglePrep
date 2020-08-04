// package src;
import java.util.HashMap;

/*
Balanced strings are those who:
have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of 
balanced strings.

Return the maximum amount of splitted balanced strings.
*/

class LR {
    public static int balancedStringSplit(String str) {
        int count = 0;
        final String s = str;
        HashMap<Character, Integer> m = new HashMap<>();
        m.put('L', 0);
        m.put('R', 0);
        for (int out = 0; out < s.length(); out++) {
            final int outer = out;
            m.computeIfPresent('L', (k,v) -> 
                v += ((Character)s.charAt(outer)) == 'L' ? 1 : 0);
            m.computeIfPresent('R', (k,v) ->
                v += ((Character)s.charAt(outer)) == 'R' ? 1 : 0);

            if (m.get('L').equals(m.get('R'))) {
                // new word found
                count++;
            }
        }
        return count;
    }


    public static void main(String[] args) {
        String $s = "";
        String s = "RLRRLLRLRL";
        System.out.println(LR.balancedStringSplit(s));
        
    }
}