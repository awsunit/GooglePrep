
// package src;
/*

Given a non-empty string s and a dictionary wordDict 
containing a list of non-empty words, add spaces in s 
to construct a sentence where each word is a valid dictionary word. 

Return all such possible sentences.

*/
// emoji -> window + . 

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class WB2 {

    List<String> dict;
    Map<String,List<String>> mapp;

    public List<String> wordBreak(String s, List<String> wordDict) {
        // lets create hashmap
        // letter -> words in dict which begin with
        List<String> characters = IntStream.rangeClosed('a','z')
                                .mapToObj(c -> Character.toString(c))
                                .collect(Collectors.toCollection(ArrayList::new));

        Map<String, Integer> counts = characters.stream().collect(Collectors.toMap(Function.identity(),x -> 0));
        // count occurences of letters in s

        // count occurences of letters in all words

        // find if there is occurence of letter in words which doesn't occur in s
        // return empty if that is case


        // HashMap<Character, List<String>> mp = new HashMap<>();
        // WB2 wb = new WB2();
        this.dict = wordDict;
        Map<String, List<String>> mp = characters.stream()
                                        .collect(Collectors.toMap(
                                            Function.identity(), this::findWords));
        this.mapp = mp;
        

        // start the recursive process
        return this.recurse(s, "", new ArrayList<String>());

    }

    public List<String> recurse(String s, String constr, List<String> accum) {
        
        // base case is s == one of words

        String firstChar = Character.toString(s.charAt(0));
        List<String> matchingWords = this.mapp.get(firstChar);

        if (matchingWords.size() == 0) {
            // cannot begin this process -> return empty list
            return new ArrayList<String>();
        }

        // iterate over this words and see if anything matches
        for (String word : matchingWords) {
            // base case
            if (word.equals(s)) {
                String temp = constr + word;
                accum.add(temp);
                // return accum;
            } else if (s.startsWith(word)) {
                // add word + space to 
                // constr (a string we are constructing)
                // String nxt = s;
                // String temp = constr;
                // while (nxt.startsWith(word) && !nxt.equals(word)) {
                //     temp += (word + " ");
                //     int start = nxt.indexOf(word);
                //     nxt = nxt.substring(start + word.length());
                // }
                // if (nxt.equals("")) {
                //     accum.add(nxt)
                // }
                String temp = constr + word + " ";
                int start = s.indexOf(word);
                String nxt = s.substring(start + word.length());
                this.recurse(nxt, temp, accum);
            }
        }
        return accum;
    }

    public List<String> findWords(String s) {
        List<String> r = new ArrayList<>();
        for (String str : dict) {
            if (str.startsWith(s)) {
                r.add(str);
            }
        }   
        return r;
    }


    public static void main (String[] args) throws IOException{

        // List<String> characters = IntStream.rangeClosed('a','z')
        // .mapToObj(c -> Character.toString(c)).collect(Collectors.toCollection(ArrayList::new));
        // List<String> lst = Arrays.asList("fox","hole","trot");
        // WB2 wb = new WB2();
        // wb.dict = lst;

        // Map<String, List<String>> mp = characters.stream().collect(Collectors.toMap(Function.identity(), wb::findWords));

        // String s = "cats";
        // String t = s.substring(4);
        // print(t.equals(""));
        // print(t == null);

        print(Math.log(2)/Math.log(2));


        // .collect(Collectors.joining()).;
        int count = 0;
        int m = 1;
        int n = 3;
        while (n > 0) {

            if (n - 1 >= 0) {
                int t = (int)(Math.log(m) / Math.log(2));
                count += t;
                if (n - 2 >= 0) {
                    count += 2;
                    m*=2;
                    n -= 2;
                } else {
                    count += 1;
                    break;
                }
            }
        }
        print(count);

        // String path = "testcases/WB2.txt";
        // FileReader fr = new FileReader(path);
        // BufferedReader stdin = new BufferedReader(fr);

        // String input;
        // // lets do some string manipulation
        // WB2 wb = new WB2();
        // while ((input = stdin.readLine()) != null){
        //     // Arrays.asList is FIXED SIZE
        //     List<String> l = new ArrayList<>(Arrays.asList(input.split(" ")));
        //     String s = l.remove(0);  // first entry is our starting string
        //     print("Looking at word: " + s);
          
        //     List<String> r = wb.wordBreak(s, l);
        //     for (String h : r) {
        //         print(h);
        //     }
        //     // r.stream().forEach(WB2::print);
        // }

        // stdin.close();

    }

    static void print (Object o) {
        System.out.println(o);
    }
}