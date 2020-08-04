import java.util.regex.Pattern;

/*
Given a word, you need to judge whether the usage of capitals in it
is right or not.

We define the usage of capitals in a word to be right when one 
of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a 
right way.
*/
class DetCap {

    public boolean detectCapitalUse(String word) {
        // everything capital?
        // nothing capital?
        // only first letter capital?
        if (word.matches("[A-Z]+") || 
            word.matches("[a-z]+") ||
            word.matches("[A-Z][a-z]*")) {
            return true;
        }
        return false;
        
    }

    public static void main(String[] args) {
        String s;
        DetCap self = new DetCap();

        s = "USA";
        System.out.println(self.detectCapitalUse(s));
        s = "FlaG";
        System.out.println(self.detectCapitalUse(s));


    }
}
