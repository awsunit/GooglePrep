package src;

import java.util.*;
import java.util.stream.IntStream;

public class ListParser {


    public NestedInteger deserialize(String s) {
        // want a recursive method or a stack

        NestedInteger rere = new NestedInteger();
        Stack<Character> stk = new Stack<>();

        char[] cr = s.toCharArray();
        stk.push(cr[0]);

        int spot = 1;

        while (!stk.empty()) {
            Character c = stk.pop();
            if (c.equals("[")) {
                // want to find our match
            } else if (c.equals("]")) {
                // we've matched, lets pop the champagne

            } else if (c.equals(",")) {
                // this is a list we should....
            }
        }

    }


  // This is the interface that allows for creating nested lists.
  // You should not implement it, or speculate about its implementation
  public interface NestedInteger {
    // Constructor initializes an empty nested list.
    // public NestedInteger();

    // Constructor initializes a single integer.
    // public NestedInteger(int value);

    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    public boolean isInteger();

    // @return the single integer that this NestedInteger holds, if it holds a single integer
    // Return null if this NestedInteger holds a nested list
    public Integer getInteger();

    // Set this NestedInteger to hold a single integer.
    public void setInteger(int value);

    // Set this NestedInteger to hold a nested list and adds a nested integer to it.
    public void add(NestedInteger ni);

    // @return the nested list that this NestedInteger holds, if it holds a nested list
    // Return null if this NestedInteger holds a single integer
    public List<NestedInteger> getList();
}
}

