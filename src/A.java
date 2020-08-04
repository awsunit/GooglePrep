import java.util.Arrays;
import java.util.Formatter;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Supplier;

import javax.lang.model.element.Element;
class FUC{

}
class A {

    class Y<J>{
        J s;
        public Y(J s){
            this.s = s;
        }
    }
    class Shape{

    }
    class Q extends Shape{

    }
    class T extends Shape{

    }
    public enum E {
        HELIUM("HE","GAS");
        String chem;
        String naty;
        private E(String n, String nat){
            chem = n;
            naty = nat;
        }
        String cs() {return chem;}
    }



    public static void main (String[] args)
    {

        
        String a = "A";
        String b = "B";
        String n = null;

        StringBuilder bb = new StringBuilder("C");
        Formatter fmt = new Formatter(bb);

        fmt.format("%s%s",a,b);
        System.out.println(fmt);

        fmt.format("%-2s", b);
        System.out.println(fmt);

        fmt.format("%b", n);
        System.out.println(fmt);

        // String f = "f";
        // String s = new String("f");
        // System.out.println(f.equals(s));
        // System.out.println(f==s);
        // System.out.println(f.equals("fs"));
        // System.out.println(s=="f");
        // Integer x = 3;
        // Integer y = null;
        // try {
        //     System.out.println(Integer.compareUnsigned(x, 3)==0 ||
        //     Integer.compare(y, 0)== 0);
        // } catch (Exception e) {
        //     System.out.println(e.getClass().toString());
        // }
        // try{
        //     System.out.println(y.compareTo(null)==0 || true);
        // } catch (Exception e) {
        //     System.out.println(e.getClass().toString());
        // }


        // A a = new A();
        // Y<> yy = a.new Y<>("hi");
        // Shape s = a.new Q();
        // Q q1 = a.new Q();
        // // T t = (T) q1;  fail
        // // T t = (T)s;
        // s = q1;


        // Double d = null;
        // boolean b = false;
        // System.out.println((b = true) ? "true" : "false");

        // System.out.println(Math.round(Math.random()*10));
        // System.out.println(Math.round(Math.random() % 10));
        // System.out.println(Math.random() *10);


        // System.out.println(E.HELIUM.toString());

        // Supplier<String> i = () -> "Car";
        // Consumer<String> c = x -> System.out.print(x.toLowerCase());
        // Consumer<String> d = x -> System.out.print(x.toUpperCase());
        // c.andThen(d).accept(i.get());
        // System.out.println();
        
        // List<String> l = Arrays.asList("dog","over","good");
        // System.out.println(l.stream().reduce(new String(), (x1,x2) -> 
        // {if (x1.equals("dog"))return x1;return x2;}));

        // l.stream().reduce((x1,x2) -> x1.length() == 3? x1:x2).ifPresent(System.out::println);

        // l.stream().reduce
        int[] r = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        // System.out.println("Bye)0");
        // System.out.println(maxSubAarray(r));
    }

    public static void main() {
        System.out.println("Hi");
    }
}