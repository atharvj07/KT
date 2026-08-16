#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, a, b) for (int i = (a); i < (b); i++)
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...) 0
#endif

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    if (n == 1) {
        string s, t = "! BR";
        cout << "? 1" << endl;
        cin >> s;
        if (s[0] == 'R') swap(t[2], t[3]);
        cout << t << endl;
        return 0;
    }
    vector<char> c(2 * n + 1);
    int l = 1, r = n + 1;
    cout << "? ";
    rep(i, l, r) cout << i << " ";
    cout << endl;
    string s;
    cin >> s;
    char t = s[0];
    while (r - l > 1) {
        int m = (r + l) / 2;
        cout << "? ";
        rep(j, 0, n) cout << m + j << " ";
        cout << endl;
        cin >> s;
        if (s[0] == t)
            l = m;
        else
            r = m;
    }
    r += n - 2;
    l++;
    rep(i, 1, 2 * n + 1) {
        if (l <= i && i <= r) continue;
        cout << "? ";
        rep(j, l, r + 1) cout << j << " ";
        cout << i << endl;
        cin >> s;
        c[i] = s[0];
    }
    set<int> red, blue;
    rep(i, 1, 2 * n + 1) {
        if (c[i] == 'R' && red.size() != n / 2) {
            red.insert(i);
        } else if (c[i] == 'B' && blue.size() != n / 2) {
            blue.insert(i);
        }
    }
    rep(i, l, r + 1) {
        cout << "? ";
        for (int r : red) cout << r << " ";
        for (int b : blue) cout << b << " ";
        cout << i << endl;
        cin >> s;
        c[i] = s[0];
    }
    cout << "! ";
    rep(i, 1, 2 * n + 1) cout << c[i];
    cout << endl;
    return 0;
}