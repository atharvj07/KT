#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll oo = 0x3f3f3f3f3f3f3f3fLL;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  ll H, n;
  cin >> H >> n;
  vector<ll> d(n);
  for (auto &a : d) cin >> a;
  vector<ll> p(n + 1);
  for (ll i = 1; i <= n; i++) p[i] = d[i - 1] + p[i - 1];
  ll fr = H;
  for (ll i = 0; i < n; i++) {
    fr += d[i];
    if (fr <= 0) return cout << i + 1 << endl, 0;
  }
  if (p[n] >= 0) return cout << -1 << endl, 0;
  ll res = oo;
  cerr << p[n] << endl;
  for (ll i = 1; i <= n; i++) {
    ll q = -p[i];
    ll k = (q - H + p[n] + 1) / p[n];
    res = min(n * k + i, res);
  }
  cout << res << endl;
}
