
class B {

    // static int n2 = getVal();
    static int n1 = 10;
    static int n2 = getVal();
    static int getVal(){return n1;}

    static int doSum(){return n1+n2;}
    static int doM(){return n1-n2;}


    public static void main (String[] args) 
    {
   
        // System.out.println(n2);
        int x = B.doSum();
        System.out.println(B.doSum());
        System.out.println(B.doSum());

    }
}