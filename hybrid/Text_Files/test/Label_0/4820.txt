#include <bits/stdc++.h>
using namespace std;
using ll = long long int;

signed main() {
  int N;
  cin >> N;
  vector<ll> A(N);
  for (auto &x : A) {
    cin >> x;
  }
  map<ll, ll> mp;
  for (auto x : A) {
    for (ll a = 1; a*a <= x; a++) {
      if (x % a) continue;
      if (a != 1)
        mp[a] += x;
      if (x/a != a)
        mp[x/a] += x;
    }
  }
  ll res = 0;
  for (auto x : mp) {
    res = max(res, x.second);
  }
  cout << res << endl;
  return 0;
}
