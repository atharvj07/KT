#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  ll n, m;
  cin >> n >> m;
  vector<ll> ar(n);
  vector<ll> br(n);
  map<ll, ll> a, b;
  for (auto &x : ar) {
    cin >> x;
    a[x]++;
  }
  for (auto &x : br) {
    cin >> x;
    b[x]++;
  }
  ll res = 1.01e18;
  for (int i = 0; i < n; ++i) {
    ll x = (br[i] - ar[0] + m) % m;
    bool can = true;
    for (auto ex : a) {
      can &= (ex.second == b[(ex.first + x) % m]);
    }
    if (can) res = min(res, x);
  }
  cout << res << '\n';
  return 0;
}
