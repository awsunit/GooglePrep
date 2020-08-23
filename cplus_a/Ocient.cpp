
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
#include <vector>
#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::vector;

// should be ocient
class Database {
public:
    vector<vector<int>> db;
    int numCols;
    
    Database(int numCols) : numCols(numCols) {};

    ~Database() {
        cout << "buhbye" << endl;
    }
    
    int insert(vector<int> row) {
        // check schema contract
        if (row.size() != numCols) {
            cout << "row must have " << numCols << " cols" << endl;
            return -1;
        }
        db.push_back(row);   
        return db.size() - 1;
    }
    
    vector<int> retrieve(int index) {
        if (index > db.size() - 1) {
            cout << "index out of range" << endl;
            return vector<int>(0);
        }
        return db.at(index);
    }
    
    bool update(int index, int col, int value) {
        if (index > db.size() - 1) {
            cout << "index out of range" << endl;
            return false;
        }
        if (col > numCols - 1) {
            cout << "col out of range" << endl;
            return false;
        }
        db.at(index).at(col) = value;
        
        return true;
    }    
};

int main () {
    Database db(3);
    vector<int> spots;
        
        
    vector<int> l;
    for (int i = 1; i < 4; i++) {
        l.push_back(i);
    }
    int spot = db.insert(l);
    spots.push_back(spot);
        
    vector<int> rl = db.retrieve(spot);
    for (int i : rl) {
        cout << i << " ";
    }
    cout << endl;
        
    db.update(spot, 2, 100);
    vector<int> nl = db.retrieve(spot);
    for (int i : nl) {
        cout << i << " ";
    }
    cout << endl;
        
    // for (int i = 0; i < 5; i++) {
    //     ArrayList<Integer> tl = new ArrayList<>();
    //     for (int j = 1; j < 4; j++) {
    //         l.add(i + j);
    //     }
    //     int s_i = db.insert(tl);
    //     spots.add(s_i);
    // }
    return 0;        
}