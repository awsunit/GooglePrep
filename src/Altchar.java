/*
You are given a string containing characters x and y only. 
Your task is to change it into a string such that there are no 
matching adjacent characters. 

To do this, you are allowed to delete zero or more characters in 
the string.

Your task is to find the minimum number of required deletions.

For example, given the string s = AABAAB , remove an A at positions 0
and 3 to make s = ABAB in 2 deletions.
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.regex.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;


class Altchar 
{

    public interface Inner {
        public void JerkOff(String s);
    }

    public static void main (String[] args) throws IOException
    {
        BufferedReader stdin = null;
        try {
            String path = "src/s.txt";
            FileInputStream fis = new FileInputStream(path);
            stdin = new BufferedReader(new InputStreamReader(fis));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        
        // List<Integer> l = Arrays.asList(1,2,3,4);
        // Stream<Integer> i = l.stream().map(x -> x + 5);
        // i.forEach(System.out::println);

        

        // Function<String, Stream<Character>> kk = t -> 
        // {
        //     return t.chars().mapToObj(c -> (char) c);
        // };
        // Stream<Character> ss = kk.apply("Hello");
        // ss.forEach(System.out::println);


        // Predicate<String> isHello = t -> t.equals("hello");
        // System.out.println(isHello.test("hello"));

        List<Shit1> shitties = new ArrayList<>();
        int i = 5;
        Shit1 s = new Shit1(420);
        while (i-- > 0)
        {
            s = new Shit1(i);
            shitties.add(s);
        }

        List<Integer> rl = s.calc(shitties, new Function<Shit1, Integer>()
        {
            public Integer apply(Shit1 s){
                return s.getMyShit();
            }
        });
        rl.stream().forEach(System.out::println);

        // rl = s.calc(shitties, st -> st.getMyShit());
        // rl.stream().forEach(System.out::println);

        // rl = s.calc(shitties, Shit1::getMyShit);
        // rl.stream().forEach(System.out::println);

        Altchar alt = new Altchar();
        Altchar.Car c = alt.new Car(5);
        Altchar.Mechanic m = alt.new Mechanic();

        execute(c, new Consumer<Car>() 
        {
            public void accept(Car ca)
            {
                m.fix(ca);
            }
        });

        execute(c, car -> m.fix(car));
        execute(c, m::fix);

    }

    static void execute(Car c, Consumer<Car> consumer)
    {
        consumer.accept(c);
    }
   
    class Car {
        int id;

        public Car(int i)
        {
            id = i;
        }
    }
    class Mechanic
    {
        public void fix(Car c){
            System.out.println("Fixing " + c.id);
        }
    }

    static class Shit1 {
        int myshit = 0;


        public List<Integer> calc(List<Shit1> l, Function<Shit1,Integer> f){
            List<Integer> r = new ArrayList<>();
            for (Shit1 s : l)
            {
                r.add(f.apply(s));
            }
            return r;
        }

        public int getMyShit(){
            return myshit;
        }

        public Shit1(int i){
            myshit = i;
        }
    }

    static void print(String s)
    {
        System.out.println(s);
    }
}