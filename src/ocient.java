package src;

// Ocient is building a brand new in-memory database.
// Your task is to write the storage engine of the database.
//
// The storage engine is responsible for the following:
//
//    1. Insert a row conforming to some schema of integers
//    2. Retrieve an arbitrary row previously inserted
//    3. Update an arbitrary column of an arbitrary row
//    4. Efficiently delete an arbitrary row
//    5. Explain how your storage engine would hypothetically perform on the following queries.
//       Compare/contrast performance and how you could optimize for one or all of the queries.
//        SELECT * FROM table;
//        SELECT a, z FROM table;
//        SELECT AVG(a) FROM table;
//
// High level example:
//   Insert 54, 78, 0
//   Insert 67, -23, 4
//   Insert 123, 5656, 2343
//   Retrieve 2nd row -> 67, -23, 4
//   Update 1st column of 3rd row to be 100
//   Retrieve 3rd row -> 100, 5656, 2343
//

import java.util.*;
// should be ocient
public class Database {
    private ArrayList<ArrayList<Integer>> db = new ArrayList<>();
    private int numCols;
    
    public Database(int numCols) {
        this.numCols = numCols;
    }
    
    public int insert(ArrayList<Integer> row) {
        // check schema contract
        if (row.size() != numCols) {
            System.out.println("row must have " + numCols + " cols");
            return -1;
        }
        db.add(row);   
        return db.size() - 1;
    }
    
    public ArrayList<Integer> retrieve(int index) {
        if (index > db.size() - 1) {
            System.out.println("index out of range");
            return null;
        }
        return db.get(index);
    }
    
    public boolean update(int index, int col, int value) {
        if (index > db.size() - 1) {
            System.out.println("index out of range");
            return false;
        }
        if (col > numCols - 1) {
            System.out.println("col out of range");
            return false;
        }
        ArrayList<Integer> l = db.get(index);
        l.set(col, value);
        return true;
    }

    public static void main (String [] args) {
        Database db = new Database(3);
        ArrayList<Integer> spots = new ArrayList<>();
        
        
        ArrayList<Integer> l = new ArrayList<>();
        for (int i = 1; i < 4; i++) {
            l.add(i);
        }
        int spot = db.insert(l);
        spots.add(spot);
        
        ArrayList<Integer> rl = db.retrieve(spot);
        for (Integer i : rl) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        db.update(spot, 2, 100);
        ArrayList<Integer> nl = db.retrieve(spot);
        for (Integer i : nl) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        for (int i = 0; i < 5; i++) {
            ArrayList<Integer> tl = new ArrayList<>();
            for (int j = 1; j < 4; j++) {
                l.add(i + j);
            }
            int s_i = db.insert(tl);
            spots.add(s_i);
        }
        
    }
    
}