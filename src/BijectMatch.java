
// package src;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

class BijectMatch {
    public static boolean wordPattern(String pattern, String str) {
        // map
        HashMap<Character, String> hm = new HashMap<>();

        int cur = 0;
        String[] words = str.split(" ");
        if (words.length != pattern.length()) {
            return false;
        }



        
        for (Character c : pattern.toCharArray()) {
            String word;
            if (cur > words.length) {
                // more chars than words?
                return false;
            }
            if ((word = hm.get(c)) == null) {
                // perhaps another mapping contains this words[cur]
                if (hm.containsValue(words[cur])) {
                    return false;
                }
                // never have seen this letter, map to cur word
                hm.put(c, words[cur]);
            } else {
                if (!word.equals(words[cur])) {
                    return false;
                }
            }
            cur++;
        }
        return true;
    }


    public static void main(String[] args) {
        String pattern = "abba";
        
        String s = "dog cat cat dog";
        System.out.println(BijectMatch.wordPattern(pattern, s));
        s = "dog cat cat fish";
        System.out.println(BijectMatch.wordPattern(pattern, s));
        s = "dog dog dog dog";
        System.out.println(BijectMatch.wordPattern(pattern, s));
        pattern = "aaa";
        s = "aa aa aa aa";
        System.out.println(BijectMatch.wordPattern(pattern, s));

    }
}