import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within the list (including duplicates).  

For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.

You may return the answer in any order.
*/
 

 class CommonChars{
    public List<String> commonChars(String[] A) {
        // first lets count the occurrances of letters in
        // each string

        // take chars whose counts all ==
        
        HashMap<String, HashMap<Character, Long>> m = new HashMap<>();

        for (String s : A) {
            HashMap<Character, Long> counts = new HashMap<>();

            IntStream chars = s.chars();
            chars.forEach(action);
        }
    }
}