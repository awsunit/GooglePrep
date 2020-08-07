// package src;


// s = "bcdbcdbcdbcd"
// t = "bcdbcd"

// a = "bcd"



public class StringDiv {

    public static int findSmallestDivisor(String s, String t) {
        String temp = s;
        // check divisibility
        while (temp.startsWith(t)) {
            temp = temp.replaceFirst(t, "");
        }
        if (temp.length() != 0) {
            // not divisible
            return -1;
        }

        // O(s.length*t.length) 
        // for (int c = t.length(); c >= 0; c--) {
        for (int c = 0; c <= t.length(); c++) {
            // next substring
            String pre = t.substring(0, c);
            String ts = s;
            String tt = t;
            // t <= s
            tt = tt.replaceAll(pre, "");
            if (tt.length() == 0) {
                ts = ts.replaceAll(pre, "");
                if (ts.length() == 0) {
                    return pre.length();
                }
            }
        }
        // default -> should never be triggered
        return -1;
    }
    public static void main(String[] args) {
        String s = "bcdbcdbcdbcd";
        String t = "bcdbcd";
        // String s = "f";
        // String t = "lrbb";
        System.out.println(StringDiv.findSmallestDivisor(s, t));
    }
}