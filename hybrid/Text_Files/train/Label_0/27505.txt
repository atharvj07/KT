#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<int> a(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        a[i] = (int)abs(s[i] - s[i + 1]);
    }
    n--;
    vector<int> cnt(3, 0);
    for (int x : a) {
        cnt[x] += 1;
    }
    int coeff = 1;
    if (cnt[1] == 0) {
        coeff *= 2;
        for (int& x : a) {
            x >>= 1;
        }
    }
    int res = 0;
    for (int i = 0; i < n; ++i) {
        if (((n - 1) & i) == i) {
            res ^= a[i];
        }
    }
    cout << (res & 1) * coeff << endl;
    return 0;
}