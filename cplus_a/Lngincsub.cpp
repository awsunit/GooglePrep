#include <iostream>

int LIS (int arr[], int n) {
    int L[n] = {0};

    L[0] = 1;

    for (int i = 1; i < n; ++i) {

        for (int j = 0; j < i; ++j) {
            if (arr[j] < arr[i] && L[j] > L[i]) {
                L[i] = L[j];
            }
        }
        L[i]++;
    }
    int m = 0;
    for (int x : L) {
        m = std::max(m, x);
    }
    return m;
}

int main() {
    int arr[] = {0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15};

    std::cout << LIS(arr, 16) << std::endl;
    return 0;
}