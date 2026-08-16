#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = (int)s.size();
    
    if ((s.at(0) == '0') || (s.at(n - 1)) == '1') {
        cout << -1 << endl;
        return 0;
    }
    for (int i = 0; i < n / 2; i++) {
        if (s.at(i) != s.at(n - i - 2)) {
            cout << -1 << endl;
            return 0;
        }
    }
    
    int p = 1;
    int v = 2;
    for (int i = 0; i < n - 1; i++) {
        cout << p << " " << v << endl;
        if (s.at(i) == '1') p = v;
        v++;
    }
}