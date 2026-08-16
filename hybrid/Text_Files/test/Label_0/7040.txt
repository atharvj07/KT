#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int (i)=(0);(i)<(int)(n);++(i))
using ll = long long;
using P = pair<int, int>;
using namespace std;


int main() {
    int N;
    cin >> N;
    int p[4], t[4];
    rep(i, 4) cin >> p[i];
    rep(i, 4) cin >> t[i];

    int ans = 1e8;
    rep(a, 101) rep(b, 101) rep(c, 101) rep(d, 101) {
        if (a*t[0] + b*t[1] + c*t[2] + d*t[3] >= N) {
            ans = min(ans, a*p[0] + b*p[1] + c*p[2] + d*p[3]);
        }
    }
    cout << ans << endl;

    return 0;
}

