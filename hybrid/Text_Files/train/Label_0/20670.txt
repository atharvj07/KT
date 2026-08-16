#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for (int i=0;i<(n);i++)
#define REP2(i,m,n) for (int i=m;i<(n);i++)
typedef long long ll;

const ll MOD = 1000000007;
ll hoge[10];

void solve() {
    ll M;
    string C;
    cin >> M >> C;
    int N = C.size();
    ll CM = 0;

    ll base = 1;
    REP(i, N) {
        int idx = N - i - 1;
        (hoge[C[idx]-'0'] += base) %= MOD;
        (CM += base * (C[idx] - '0') % MOD) %= MOD;
        base = base * 10 % MOD;
    }

    vector<int> fuga = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    do {
        if (N != 1 && fuga[C[0]-'0'] == 0) continue;
        ll D = CM;
        REP(i, 10) (D += (fuga[i] - i) * hoge[i] % MOD) %= MOD;
        D = (D % MOD + MOD) % MOD;
        if (D == M) {
            REP(j, N) cout << fuga[C[j]-'0'];
            cout << endl;
            return;
        }
    } while (next_permutation(fuga.begin(), fuga.end()));

    cout << -1 << endl;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    solve();
}

