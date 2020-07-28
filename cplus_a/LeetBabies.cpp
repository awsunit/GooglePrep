// C++ baby
#include <iostream>

using std::cout;
using std::endl;
using std::cin;
int arrangeCoins(int coins);
int arrangeCoins_i(int coins, int step, int count);


int main ()
{
   cout << "Hola Hot Stuff, enter a number" << endl;
   int coins = 0;
   cin >> coins;
   cout << coins << endl;
   coins = arrangeCoins(coins);
   cout << "You can build: " << coins << " steps" << endl;

}

int arrangeCoins(int n) 
{
    // on kth step, k coins
    return arrangeCoins_i(n, 1, 0);
}
int arrangeCoins_i(int n, int step, int count)
{
    if (step > n) {
        return count;
    }
    cout << n << " " << step << " " << count << endl;
    n -= step;
    step++;
    count++;
    return arrangeCoins_i(n, step, count);
}