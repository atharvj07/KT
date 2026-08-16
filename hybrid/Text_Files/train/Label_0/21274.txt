#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;
// Welcome to my source code!

int main() {
    int d, l;
    cin >> d >> l;
    int t = d - (d / l) * l;
    int ans = t + (d / l);
    cout << ans << endl;
}
