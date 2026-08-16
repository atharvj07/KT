#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    int plus[n];
    for (int i=0; i<n; i++) {
        int pi;
        cin >> pi;
        plus[pi-1] = i;
    }
    for (int i=0; i<n; i++) 
        cout << n * i       + plus[i] + 1 << (i < n-1 ? ' ' : '\n');
    for (int i=0; i<n; i++) 
        cout << n * (n-i-1) + plus[i] + 1 << (i < n-1 ? ' ' : '\n');
    return 0;
}