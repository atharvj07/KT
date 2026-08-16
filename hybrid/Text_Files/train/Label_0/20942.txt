#include <bits/stdc++.h>
#define int long long
#define endl '\n'
#define FOR(i, a, n) for (int i = (a); i < (n); ++i)
#define REP(i, n) FOR(i, 0, n)
using namespace std;

void _main() {
    int H, W;
    cin >> H >> W;
    vector<string> c(H);
    vector<pair<int, int>> pos;
    REP (i, H) {
        cin >> c[i];
        REP (j, W) if (c[i][j] == 'B') {
            pos.emplace_back(i, j);
            break;
        }
        for (int j = W - 1; j >= 0; --j) if (c[i][j] == 'B') {
            pos.emplace_back(i, j);
            break;
        }
    }
    sort(pos.begin(), pos.end());
    pos.erase(unique(pos.begin(), pos.end()), pos.end());
    int ans = 0;
    for (int i = 0; i < pos.size(); ++i) {
        for (int j = 0; j < pos.size(); ++j) {
            ans = max(ans, abs(pos[i].first - pos[j].first) + abs(pos[i].second - pos[j].second));
        }
    }
    cout << ans << endl;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed << setprecision(10);
    _main();
    return 0;
}
