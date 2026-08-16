#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
using ll = long long int;
ll binpow(ll a, ll b) {
  ll res = 1;
  while (b > 0) {
    if (b & 1) {
      res = res * a;
    }
    a = a * a;
    b >>= 1;
  }
  return res;
}
void solve() {
  ll n;
  cin >> n;
  ll ar[n + 1];
  for (ll i = 0; i < n; i++) {
    cin >> ar[i];
  }
  ll mn[n + 1];
  ll mx[n + 1];
  mn[0] = 0;
  for (ll i = 1; i < n; i++) {
    if (ar[i] < ar[mn[i - 1]]) {
      mn[i] = i;
    } else {
      mn[i] = mn[i - 1];
    }
  }
  mx[n - 1] = n - 1;
  for (ll i = (n - 2); i >= 0; i--) {
    if (ar[i] > ar[mx[i + 1]]) {
      mx[i] = i;
    } else {
      mx[i] = mx[i + 1];
    }
  }
  for (ll i = 0; i < n; i++) {
    if ((ar[i] + ar[mn[i]] <= ar[mx[i]]) && (i != mn[i]) && (i != mx[i])) {
      cout << mn[i] + 1 << " " << i + 1 << " " << mx[i] + 1 << "\n";
      return;
    }
  }
  cout << -1 << "\n";
  return;
}
int main() {
  ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
  ll t = 1;
  cin >> t;
  while (t--) {
    solve();
  }
}
