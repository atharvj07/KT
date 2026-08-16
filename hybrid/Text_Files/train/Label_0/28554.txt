#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 998244353;
struct Two {
  ll mat[2][2] = {};
  ll &operator()(ll i, ll j) { return mat[i][j]; }
  ll operator()(ll i, ll j) const { return mat[i][j]; }
  Two operator*(const Two &rhs) {
    Two res;
    for (ll i = 0; i < 2; i++) {
      for (ll j = 0; j < 2; j++) {
        for (ll k = 0; k < 2; k++) {
          res.mat[i][j] = (res.mat[i][j] + mat[i][k] * rhs.mat[k][j]) % MOD;
        }
      }
    }
    return res;
  }
};
inline ll f(ll a) { return a + 1; }
inline ll f(ll a, ll b) {
  if (a != 1) {
    return 0;
  }
  return max<ll>(19 - (10 * a + b), 0);
}
const ll N = 5e5;
ll digits[N + 2];
Two seg[4 * N];
void build(ll v, ll vl, ll vr) {
  if (vl == vr) {
    seg[v](0, 0) = f(digits[vl + 1]);
    seg[v](0, 1) = f(digits[vl + 1], digits[vl]);
    seg[v](1, 0) = 1;
    return;
  }
  const ll vm = (vl + vr) >> 1;
  build(2 * v, vl, vm);
  build(2 * v + 1, vm + 1, vr);
  seg[v] = seg[2 * v + 1] * seg[2 * v];
}
void update(ll v, ll vl, ll vr, ll idx) {
  if (vl > vr) {
    return;
  }
  if (vl == idx && vr == idx) {
    seg[v](0, 0) = f(digits[vl + 1]);
    seg[v](0, 1) = f(digits[vl + 1], digits[vl]);
    return;
  }
  const ll vm = (vl + vr) >> 1;
  if (idx <= vm) {
    update(2 * v, vl, vm, idx);
  } else {
    update(2 * v + 1, vm + 1, vr, idx);
  }
  seg[v] = seg[2 * v + 1] * seg[2 * v];
}
int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false), cin.tie(nullptr);
  ll n, m;
  cin >> n >> m;
  string s;
  cin >> s;
  digits[n + 1] = 0;
  for (ll i = 1; i <= n; i++) {
    digits[i] = s[n - i] - '0';
  }
  build(1, 1, n);
  for (ll i = 1; i <= m; i++) {
    ll x, d;
    cin >> x >> d;
    const ll idx = n + 1 - x;
    digits[idx] = d;
    update(1, 1, n, idx);
    if (idx > 1) {
      update(1, 1, n, idx - 1);
    }
    ll result = (seg[1](1, 0) * f(digits[1]) + seg[1](1, 1)) % MOD;
    cout << result << "\n";
  }
  return 0;
}
