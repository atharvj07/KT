#include <bits/stdc++.h>
using namespace std;

#define rep(i, N) for (int i = 0; i < (N); i++)
#define all(a) (a).begin(), (a).end()
#define pb push_back

using ll = long long;
using i_i = tuple<int, int>;

using B = bitset<1000>;

tuple<B, B> f(vector<B> a, vector<B> b, vector<int> msb, B x) {
    int N = a.size();
    B y;
    rep(i, N) if (x[msb[i]]) {
        x ^= a[i];
        y ^= b[i];
    }
    return make_tuple(x, y);
}

int main() {
    int N, M;
    cin >> M >> N;
    vector<B> v(N);
    rep(j, M) {
        string s; cin >> s;
        rep(i, N) v[i].set(j, s[i] - '0');
    }
    vector<B> a, b;
    vector<int> msb;
    vector<bool> cocircuit(N, true);
    rep(i, N) {
        B x, y;
        tie(x, y) = f(a, b, msb, v[i]);
        if (x.any()) {
            int j;
            for (j = 0; !x[j]; j++);
            int k = lower_bound(all(msb), j) - msb.begin();
            a.insert(a.begin() + k, x);
            y.set(i, 1);
            b.insert(b.begin() + k, y);
            msb.insert(msb.begin() + k, j);
        }
        else {
            y.set(i, 1);
            rep(i, N) if (y[i]) cocircuit[i] = false;
        }
    }
    vector<string> ans(M, string(N, ' '));
    rep(j, M) {
        B e;
        e.set(j, 1);
        B x, y;
        tie(x, y) = f(a, b, msb, e);
        rep(i, N) {
            if (cocircuit[i]) ans[j][i] = (x.none() && y[i]) ? '-' : '0';
            else ans[j][i] = x.any() ? '+' : '0';
        }
    }
    rep(j, M) cout << ans[j] << endl;
}

