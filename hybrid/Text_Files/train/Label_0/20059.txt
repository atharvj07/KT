#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n;
    while (cin >> n, n) {
        vector<int> v(n);
        for (int i=0; i<n; ++i) {
            cin >> v[i];
        }
        int res = 0;
        for (int i=0; i<n-1; ++i) {
            for (int j=0; j<n-1; ++j) {
                if (v[j] > v[j+1]) {
                    swap(v[j], v[j+1]);
                    res ++;
                }
            }
        }
        cout << res << endl;
    }
    return 0;
}