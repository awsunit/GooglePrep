package src;
class Palinv1 {

    public boolean isPalin(String s) {
        s = s.toLowerCase();
        String ns = s.replaceAll("[^a-z0-9]", "");
    
        int start = 0;
        int end = ns.length() - 1;

        while (start < end) {
            if (ns.charAt(start) != ns.charAt(end)) {
                return false;
            }
        }
            
         return true;
    }

    public static void main(String[] args) {
        System.out.println(new Palinv1().isPalin("race a car"));
    }
}