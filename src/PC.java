import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDate;
import java.time.Month;
import java.util.Calendar;
import java.util.Optional;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.stream.IntStream;
import java.util.stream.Stream;

class PC {
    // static int n2 = getVal();
    // static int n1 = 10;
    // static int getVal(){return n1;}

    // static int doSum(){return n1+n2;}
    // static int doM(){return n1-n2;}
    private static PC l = new PC();
    public synchronized static PC getI(){
        return l;
    }
    public static void main(String[] args) throws Exception {


    //     File f = new File("src/s.txt");
    //     FileWriter out = new FileWriter(f);
    //     // for (int i = 0; i < 5;i++){
    //     // out.write(String.valueOf(i));
    //     // }
    //     PrintWriter p = new PrintWriter(out);
    //     out.write(new char[] {'0','1','2','3','4'});
    //     out.flush();
    // }
    //    Calendar c = Calendar.getInstance();
    //    c.set(2000, Calendar.AUGUST, 30);
    //    c.roll(Calendar.MONTH, 7);
    //    System.out.println("" + c.get(Calendar.DATE) + - +
    //    c.get(Calendar.MONTH) + "-" + c.get(Calendar.YEAR));
    //    c.add(Calendar.MONTH, 11);
    //    System.out.println("" + c.get(Calendar.DATE) + - +
    //    c.get(Calendar.MONTH) + "-" + c.get(Calendar.YEAR));
    //    LocalDate d = LocalDate.of(2000, Month.AUGUST,30);
    //    d.plusMonths(6);
    //    System.out.println("" + d.getDayOfMonth() + " " + d.getMonthValue()
    //    + " " + d.getYear());
    // SortedSet<E> s = new TreeSet<E>();
    // s.add(new E(15));
    // s.add(new E(10));
    // s.add(new E(25));
    // s.add(new E(10));
    // System.out.println(s.first() + " " + s.size());
        String a = null;
        Optional<String> b = Optional.empty();
        // try{
        //     System.out.print(a.length());
        //     System.out.print(b.orElse("").length());
        // } catch (Exception e){
        //     System.out.print(a);
        // }
        // finally {
        //     a = "STring";
        //     System.out.print(a.length());
        //     b = Optional.ofNullable("");
        //     System.out.println(b.get().length());
        // }
        // int x = 3;
        // boolean b1 = true;
        // boolean b2 = false;
        // if ((b1 || b2) || (x++>4)){
        //     System.out.print(x++ + " ");
        // }
        // if ((!b1 & b2) && (++x<4))
        //     System.out.print(x);
        // ByteArrayOutputStream bb = new ByteArrayOutputStream(10);
        // System.out.println(bb.size());

        // Runnable r = () -> System.out.println("Hi");
        // new Thread(r).start();
        Stream.of("1red","2red","3red").findFirst().ifPresent(System.out::println);
        // IntStream.range(1,2).mapToObj(i -> i + "red").forEach(System.out::println);

    }
}

class M<T> {
    private Set<T> s;
    public Set<T> gc() {return this.s;}

    public void tc1(M<?> c){
        Set s = c.gc();
    }
}
// class E implements Comparable {

//     int id;
//     E(int i)
//     {
//         this.id = i;
//     }

//     public int compareTo(Object o){
//         E e = (E) o;
//         return this.id - e.id;
//     }

//     public String toString(){
//         return "" + this.id;
//     }
// }
// class C extends PC{
//     public C() {c++;}
//     public static void main(String[] args){
//         System.out.println("Count == " + getC());
//         C obj = new C();
//         System.out.println(getC());
//     }
// }