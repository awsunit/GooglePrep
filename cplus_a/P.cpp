#include <vector>
#include <iostream>
#include <stdlib.h>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <map>
#include <algorithm>
// #include <string>

using std::cout;
// using std::cin;
using std::endl;
using std::vector;
using std::set;
using std::map;
using std::ifstream;
using std::string;
using std::istringstream;
using std::stoi;
using std::getline;
using std::pair;
using std::reverse;


class A {
public:
    A(int a) : aint(a) {cout << "A has: " << aint << endl;}
    ~A() {cout << "A shutting down" << endl;}
    A& operator=(const A &somea) {
        aint = somea.aint;
        return *this;
    }
    void sayhi() {cout << "A here, saying I love " << aint << endl;}
private:
int aint;
};

class B : public A {
public:
    B(int i) : A(i - 100), bint(i) {}
    ~B() {cout << "B is shutting down" << endl;}
    void sayhi() {cout << "B here saying I love " << bint << endl;}
    B& operator=(const B b) {bint = b.bint; return *this;}

private:
int bint;
};
int main () {
    cout << "here we go" << endl;

    A *a = new A(820);
    // B *b = new B(520);
    B *b = new B(420);
    b->sayhi();
    a->sayhi();
    b->sayhi();
    *a = *b;
    a->sayhi();
    // *b = *a;
    delete a;
    delete b;

    cout << "all done boss" << endl;
}
class C : B {
public:

private:
int cint;
};