#include <cmath>
#include <iostream>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {

        if (x == 0) return 0;
        if (x == 1 || n == 0) return 1;
        if (x == 2)
        {
            int val1 = n;
            cout << "val1 first: " << val1 << endl;

            if (n < 0)
            {
                cout << "less than babe" << endl;
                val1 = val1 * (-1);
            }
            cout << "val1 after: " << val1 << endl;        

            double val = 1 << val1;
            cout << "inside val: " << val << endl;
            val = n < 0 ? 1.0/val : val;
            return val; 
        }

        // reg way
        if (n > 0)
        {
            double val = 1;
            while (n-- > 0)
            {
                val *= x;
            }
            return val;
        }

        double val = 1;
        while (n++ < 0)
        {
            val *= x;
        }

        return 1.0 / val;
    }

};

int main()
{

    Solution s;
    double yup = -2147483648;

    double v = s.myPow(2.0, yup);

    cout << "v: " << v << endl;

    return 0;
}
