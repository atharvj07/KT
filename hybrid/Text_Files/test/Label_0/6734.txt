#include <bits/stdc++.h>

#define long long long int
static const long MOD = 998244353;
using namespace std;

// @author: pashka

int main() {
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<vector<vector<int>>> g(3, vector<vector<int>>(n));
    for (int t = 0; t < 3; t++) {
        int m;
        cin >> m;
        for (int i = 0; i < m; i++) {
            int x, y;
            cin >> x >> y;
            x--;
            y--;
            if (x > y) swap(x, y);
            g[t][x].push_back(y);
        }
    }
    vector<vector<int>> gr(3, vector<int>(n));
    int mx = 0;
    for (int t = 0; t < 3; t++) {
        vector<int> z(n + 1);
        int zz = 0;
        for (int i = n - 1; i >= 0; i--) {
            zz++;
            for (int j : g[t][i]) {
                z[gr[t][j]] = zz;
            }
            while (z[gr[t][i]] == zz) gr[t][i]++;
            mx = max(mx, gr[t][i]);
        }
    }
    vector<vector<long>> ss(3, vector<long>(mx + 1));
    vector<long> pw(n + 1);
    pw[0] = 1;
    for (int i = 0; i < n; i++) {
        pw[i + 1] = pw[i] * 716070898 % MOD;
    }
    for (int t = 0; t < 3; t++) {
        for (int i = 0; i < n; i++) {
            ss[t][gr[t][i]] += pw[i + 1];
            ss[t][gr[t][i]] %= MOD;
        }
    }
    long res = 0;
    for (int i = 0; i <= mx; i++) {
        for (int j = 0; j <= mx; j++) {
            if ((i ^ j) > mx) continue;
            long s = ss[0][i];
            s *= ss[1][j];
            s %= MOD;
            s *= ss[2][i ^ j];
            s %= MOD;
            res += s;
            res %= MOD;
        }
    }
    cout << res << "\n";
    return 0;
}