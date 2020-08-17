package src;

import java.util.ArrayList;
import java.util.List;

// Given a non-negative index k where k ≤ 33, 

// return the kth index row of the Pascal's triangle.

// Note that the row index starts from 0.

public class KPasc {

    public static void main(String[] args) {
        KPasc k = new KPasc();

        System.out.println(k.getRow(3));
    }

    public List<Integer> getRow(int rowIndex) {
        ArrayList<Integer> l = new ArrayList<Integer>();
        l.add(1);
        return recurse(l, rowIndex);
    }
    public List<Integer> recurse(List<Integer> l, int index) {
        if (index == 0) return l;
        // make our new list
        ArrayList<Integer> nl = new ArrayList<>();
        nl.add(1);

        for (int i = 0; i < l.size() - 1; i++) {
            nl.add(l.get(i) + l.get(i + 1));
        }
        nl.add(1);
        List<Integer> r = this.recurse(nl, index - 1);
        return r;
    }
}